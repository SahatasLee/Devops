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
      ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
      ```

    2. เอา public key ไปวางไว้ที่แต่ละ node `/root/.ssh/authorized_keys`

      ```bash
      # Method 1:
      # Manually Copy the Key
      /root/.ssh/id_rsa.pub
      # Method 2: Using ssh-copy-id (Recommended)
      # Add the SSH Key to the SSH Agent
      # Start the SSH agent:
      eval "$(ssh-agent -s)"
      # Add your key:
      ssh-add ~/.ssh/id_rsa
      # Copy the Public Key to the Remote Server
      ssh-copy-id user@remote-server-ip
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

    ```sh
    # git clone https://github.com/kubernetes-sigs/kubespray.git 
    git clone https://github.com/kubernetes-sigs/kubespray.git --branch release-2.17 --single-branch
    ```

    ```
    cd kubespray 
    pip install -r requirements.txt --default-timeout=1000 
    cp -rfp inventory/sample inventory/kubecluster 
    ```

    ```
    declare -a IPS=(10.111.0.13 10.111.0.14 10.111.0.15) 
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
    # ansible-playbook -i inventory/cat-cluster/hosts.yaml -e docker_version=20.10 --become --become-user=root cluster.yml 
    ansible-playbook -i inventory/xxx-cluster/hosts.yaml --become --become-user=root cluster.yml
    ```

## Config 

```sh
cd kubespray
vi roles/container-engine/docker/vars/ubuntu.yml
```

ubuntu.yml

```yml
---
# https://download.docker.com/linux/ubuntu/
docker_versioned_pkg:
  'latest': docker-ce
  '18.09': docker-ce=5:18.09.9~3-0~ubuntu-{{ ansible_distribution_release|lower }}
  '19.03': docker-ce=5:19.03.15~3-0~ubuntu-{{ ansible_distribution_release|lower }}
  '20.10': docker-ce=5:20.10.7~3-0~ubuntu-{{ ansible_distribution_release|lower }}
  'stable': docker-ce=5:20.10.7~3-0~ubuntu-{{ ansible_distribution_release|lower }}
  'edge': docker-ce=5:20.10.7~3-0~ubuntu-{{ ansible_distribution_release|lower }}

docker_cli_versioned_pkg:
  'latest': docker-ce-cli
  '18.09': docker-ce-cli=5:18.09.9~3-0~ubuntu-{{ ansible_distribution_release|lower }}
  '19.03': docker-ce-cli=5:19.03.15~3-0~ubuntu-{{ ansible_distribution_release|lower }}
  '20.10': docker-ce-cli=5:20.10.7~3-0~ubuntu-{{ ansible_distribution_release|lower }}

docker_package_info:
  pkgs:
    - "{{ containerd_versioned_pkg[containerd_version | string] }}"
    - "{{ docker_cli_versioned_pkg[docker_cli_version | string] }}"
    - "{{ docker_versioned_pkg[docker_version | string] }}"

docker_repo_key_info:
  url: '{{ docker_ubuntu_repo_gpgkey }}'
  repo_keys:
    - '{{ docker_ubuntu_repo_repokey }}'

docker_repo_info:
  repos:
    - >
      deb [arch={{ host_architecture }}] {{ docker_ubuntu_repo_base_url }}
      {{ ansible_distribution_release|lower }}
      stable
```

## Delete cluster

    ```bash
    cd kubespray 
    ansible-playbook -i inventory/cat-cluster/hosts.yaml --become --become-user=root reset.yml
    ```

## Remove Worker Node


## Config insecure

```sh
kubectl config set-cluster cluster.local --insecure-skip-tls-verify=true
```