# Installing Kubernetes Cluster By Kubespray

---

## Prerequisition

- One or more machines running a deb/rpm-compatible Linux OS; for example: Ubuntu or CentOS.
- 2 GiB or more of RAM per machine--any less leaves little room for your apps.
- At least 2 CPUs on the machine that you use as a control-plane node.
- Full network connectivity among all machines in the cluster. You can use either a public or a private network.
- 4 machine
  - one for ansible
  - three for nodes

## Installation

1. ทำให้แต่ละ node รู้จักกันก่อน

    ```bash
    vi /etc/hosts
    ```

    The **hosts** file:

    ```bash
    127.0.0.1 localhost localhost.localdomain
    127.0.1.1 node01 # change name node01 to your node name

    10.111.0.111 nfs-server # change ip to your ip
    10.111.0.112 ansible-server # change ip to your ansible node ip
    10.111.0.113 node01  # change ip to your node ip
    10.111.0.114 node02  # change ip to your node ip
    10.111.0.115 node03 # change ip to your node ip
    ```

    Test

    ```bash
    ping node1
    ```

2. ทำให้เครื่อง ansible สามารถ ssh ไปทุก node ได้โดยไม่ติด password

    1. สร้าง ssh key 

      ```bash
      ssh-keygen -t rsa
      ```

    2. เอา public key ไปวางไว้ที่แต่ละ node `/root/.ssh/authorized_keys`

      ```bash
      /root/.ssh/id_rsa.pub
      ```

    3. test

      ```bash
      ssh node1
      ```

3. Install python & ansible

    ```bash
    apt install python3-pip -y 
    pip3 install --upgrade pip 
    ```

4. Clone kubespray

    ```bash
    git clone https://github.com/kubernetes-sigs/kubespray.git 
    ```

    ```
    cd kubespray 
    pip install -r requirements.txt --default-timeout=1000 
    cp -rfp inventory/sample inventory/kubecluster 
    ```

    ```
    declare -a IPS=(10.255.0.51 10.255.0.52 10.255.0.53) 
    CONFIG_FILE=inventory/xxx-cluster/hosts.yaml python3 contrib/inventory_builder/inventory.py ${IPS[@]} 
    ```

5. Config `inventory/xxx-cluster/hosts.yaml`

    ```yaml
    all:
      hosts:
        node1:
          ansible_host: 10.111.0.113
          ip: 10.111.0.113
          access_ip: 10.111.0.113
        node2:
          ansible_host: 10.111.0.114
          ip: 10.111.0.114
          access_ip: 10.111.0.114
        node3:
          ansible_host: 10.111.0.115
          ip: 10.111.0.115
          access_ip: 10.111.0.115
      children:
        kube_control_plane:
          hosts:
            node1:
            node2:
            node3:
        kube_node:
          hosts:
            node1:
            node2:
            node3:
        etcd:
          hosts:
            node1:
            node2:
            node3:
        k8s_cluster:
          children:
            kube_control_plane:
            kube_node:
        calico_rr:
          hosts: {}
    ```

6. Deploy cluster

    ```bash
    cd kubespray
    ansible-playbook -i inventory/xxx-cluster/hosts.yaml --become --become-user=root cluster.yml
    ```

7. Remove cluster

    ```bash
    cd kubespray 
    ansible-playbook -i inventory/kubecluster/hosts.yaml --become --become-user=root reset.yml
    ```