# Storage Class

A StorageClass provides a way for administrators to describe the "classes" of storage they offer. Different classes might map to quality-of-service levels, or to backup policies, or to arbitrary policies determined by the cluster administrators. Kubernetes itself is unopinionated about what classes represent. This concept is sometimes called "profiles" in other storage systems.

Storage class คือวิธีที่ใช้ในการจัดการกับ storage คล้ายกับ role ของ user. class แต่ละ class จะมีเงื่อนไขที่ไม่เหมือนกัน วิธีนี้ถูกใช้เพื่อให้ง่ายต่อการจัดการและกำหนด policy ของ storage

Storage class จะประกอบด้วย `provisioner`, `parameters` และ `reclaimPolicy` ซึ่งจะถูกใช้เมื่อ PersistentVolume ที่เป็นของคลาสนั้นๆ จำเป็นต้องได้รับการจัดสรรแบบไดนามิก

## AWS
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: standard
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp2
reclaimPolicy: Retain
allowVolumeExpansion: true
mountOptions:
  - debug
volumeBindingMode: Immediate
```

## NFS
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: example-nfs
provisioner: example.com/external-nfs
parameters:
  server: nfs-server.example.com
  path: /share
  readOnly: "false"
```