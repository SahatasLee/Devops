# NFS

## NFS Server

Friday, April 29, 2022
11:45 AM

พอเครื่องสร้างเสร็จ Login เข้าไป NFS Server เพื่อติดตั้ง NFS Service อัพเดท system package กันก่อนด้วย command

```bash
$ sudo apt update
```

เรียบร้อยแล้วเรามาติดตั้ง NFS Server กันครับ

```bash
$ sudo apt install nfs-kernel-server
```

หลังจากนั้นเรามาสร้าง Directory ที่จะแชร์ไปให้ Kubernetes Cluster ของเราใช้งาน

```bash
$ sudo mkdir -p /mnt/kube_data
```

กำหนดให้ Directory นี้สามารถเข้าถึง Shared Directory นี้ได้โดยไม่จำกัดสิทธิจาก NFS Client

```bash
$ sudo chown -R nobody:nogroup /mnt/kube_data/
```

ในกรณีของผม กำหนดให้ File ที่เกิดขึ้นขึ้นมาใน Directory นี้ ถูกกำหนดสิทธิให้เป็น Read Write และ Execute ซึ่งสามารถปรับเปลี่ยนได้ตามแต่ละกรณี

```bash
$ sudo chmod 777 /mnt/kube_data/
```

เสร็จแล้วเราไปกำหนดสิทธิให้ NFS Server อนุญาตให้ NFS Client เข้าใช้งาน Directory นี้กัน โดยการแก้ไข exports ไฟล์

```bash
$ sudo vim /etc/exports
```

กำหนด Shared Directory, Network ของ Client ที่จะเข้ามาใช้งานได้ และ Permission

```bash
/mnt/kube_data  10.88.1.0/24(rw,sync,no_subtree_check)
```

หลังจากนั้นทำการ Export Shared Directory ที่เราเตรียมเอาไว้ ตามด้วย Restart nfs-kernal-server

```bash
$ sudo exportfs -a
$ sudo systemctl restart nfs-kernel-server
```

Allow Firewall ของ Operating System ให้อนุญาต NFS Client วิ่งเข้ามาที่ NFS ของเราด้วย

```bash
$ sudo ufw allow from 10.88.1.0/24 to any port nfs
```

ตามด้วย Reload Firewall ที่เราได้แก้ไขไป

```bash
$ sudo ufw reload
```

เป็นอันเสร็จเรียบร้อยสำหรับ NFS Server 

## NFS Client

หลังจากนั้นเราไปที่ฝั่ง NFS Client นั่นเองซึ่งก็คือ Kubernetes Nodes ทั้งหมดของเรา อันดับแรก Install nfs-common to all nodes

```bash
$ sudo apt update
$ sudo apt install nfs-common
```

จากนั้นให้ลอง Mount Shared Directory โดยเริ่มจากการสร้าง Directory เพื่อเป็น Mount Point ของ Client เราก่อน

```bash
$ sudo mkdir -p /mnt/nfs_clientshare
```

Mount ไปที่ Shared Directory ของ NFS Server

```bash
$ sudo mount nfsserver01:/mnt/kube_data /mnt/nfs_clientshare
```

ถ้าสามารถ Mount ได้ ไม่ติดอะไรก็ Unmount ออกไปโดยใช้ umount ได้เลย

```bash
$ sudo umount nfsserver01:/mnt/kube_data
```

ขั้นตอนต่อไปเราจะทำการติดตั้ง Kubernetes NFS Subdir External Provisioner บน Kubernetes Cluster ของเรา อ้างอิง https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner

เพิ่มเติมเกี่ยวกับ NFS External Provisioner ทำหน้าที่บริการ NFS Storage บน Kubernetes ซึ่งจะเชื่อมต่อกับ NFS Server ของเรา เวลาเราต้องการ Persistent Volume เราไม่ต้องเข้าไปสร้างด้วยตัวเอง ทำผ่าน PVC ไปแล้ว NFS Provisioner จะไปสร้าง PV บน NFS Shared Directory ให้เอง หรือที่เรียกว่า Dynamic Provisioning นั่นเอง

ผมจะเลือกวิธีการติดตั้งผ่าน Helm ถ้าเรายังไม่เคยติดตั้งเอาไว้ เข้าไปที่ Kubernetes Master Node ของเราเพื่อ Install Helm กันก่อน

```bash
wget https://get.helm.sh/helm-v3.4.1-linux-amd64.tar.gz
tar xvf helm-v3.4.1-linux-amd64.tar.gz
sudo mv linux-amd64/helm /usr/local/bin
rm helm-v3.4.1-linux-amd64.tar.gz
rm -rf linux-amd64
helm version
```
เกี่ยวกับ Helm สักนิด Helm จัดการ Package ของ Kubernetes Application ช่วยให้เราสามารถ Deploy กลุ่มของ Application Resources ที่เราต้องการเอาไว้ในจุดเดียว คล้ายๆกับ yum หรือ apt นั่นเอง

จากนั้น Add repository และ Install NFS External Provisioner โดยใช้ Helm โดยการระบุ nfs.server และ nfs.path ที่เราได้เตรียมเอาไว้ด้วยนะครับ

```bash
$ helm repo add nfs-subdir-external-provisioner https://kubernetes-sigs.github.io/nfs-subdir-external-provisioner/
$ helm install nfs-subdir-external-provisioner nfs-subdir-external-provisioner/nfs-subdir-external-provisioner --set nfs.server=nfsserver01 --set nfs.path=/mnt/kube_data --set storageClass.volumeBindingMode=WaitForFirstConsumer
```

ลองตรวจสอบ NFS provisioner ของเราที่เป็น pod ว่าพร้อมใช้งานหรือเปล่า ลองดู Storageclass name ด้วย ถ้าเราปล่อย Default ของ helm จะได้ StorageClass ชื่อ nfs-client ซึ่งเราต้องเอาชื่อนี้ไประบุเวลาสร้าง PVC เพื่อให้สร้าง PV บน NFS ตามที่เราต้องการ

```bash
$ kubectl get pod -o wide
$ kubectl get sc
```

มาถึงตรงนี้เรามี NFS Service บน Kubernetes Cluster แล้วครับ เรามาลองสร้าง PVC และ Pod เพื่อใช้ Shared Persistent Volume กันเลย โดยเราจะสร้าง Pod จำนวน 2 Pods และ PVC ขึ้นมา 1 ก้อน เพื่อให้ Pods ทั้งสอง มาใช้งานร่วมกัน เราจะไม่สร้าง PV นะครับ จะสร้างแค่ PVC แล้วระบุ Storage Class เป็น nfs-client เพื่อให้ NFS Storage Provisioner ของเราไปสร้าง PV ให้เอง หรือเรียกว่า Dynamic Provisioning
สร้าง PVC

```
$ vi pvc-nfs.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-nfs
spec:
  storageClassName: nfs-client
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 1Gi
```

สร้าง 2 Pods จาก NginX image

```yaml
$ vi doublepod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod1
spec:
  containers:
  - name: nginx1
    image: nginx
    ports:
    - containerPort: 80
    volumeMounts:
    - name: myvolume
      mountPath: /usr/share/nginx/html
  volumes:
  - name: myvolume
    persistentVolumeClaim:
      claimName: pvc-nfs
---
apiVersion: v1
kind: Pod
metadata:
  name: mypod2
spec:
  containers:
  - name: nginx2
    image: nginx
    ports:
    - containerPort: 80
    volumeMounts:
    - name: myvolume
      mountPath: /usr/share/nginx/html
  volumes:
  - name: myvolume
    persistentVolumeClaim:
      claimName: pvc-nfs
```

เสร็จแล้วลองตรวจสอบดูว่า PVC และ Pod ของเราได้ถูกสร้างขึ้นมาสมบูรณ์หรือยัง รวมไปถึง PV ด้วยที่ Storage Provisioner สร้างให้เรา

จะเห็นได้ว่ามี Pod เกิดขึ้นมา 2 ตัว ซึ่งใช้งาน PVC ผ่านไปถึง PV เดียวกัน

เรามาลองตรวจสอบดููว่าทั้ง 2 Pod เข้าถึง PV เดียวกันหรือเปล่า โดยสร้างไฟล์ใน Volume ของ Pod ตัวที่หนึ่ง แล้วลองไปดู Pod ตัวสองว่ามีไฟล์เพิ่มมาหรือเปล่า

เข้าไปใน pod ที่หนึ่ง

```bash
$ kubectl exec -it mypod1 -- /bin/bash
```

จากนั้นสร้างไฟล์ขึ้นมา

```bash
$ echo hello > /usr/share/nginx/html/testnew.txt
```

ออกมาจากตัวแรกแล้ว จากนั้นเราลองเข้าไปดูไฟล์นี้ใน pod ตัวที่สองกันครับ

```bash
$ kubectl exec -it mypod2 -- /bin/bash 
```

ลองอ่านไฟล์ดังกล่าวดูครับ

```bash
$ cat /usr/share/nginx/html/testnew.txt
```

จากขั้นตอนที่ได้กล่าวไปทั้งหมดนะครับ เพียงเท่านี้เราก็จะได้ NFS Provisioner มาให้บริการ Shared Persistent Volume ให้กับ Pods ของเราใน Kubernestes Cluster แล้วครับ 

From <https://blog.leapgio.cloud/kubernetes-shared-volume/>
