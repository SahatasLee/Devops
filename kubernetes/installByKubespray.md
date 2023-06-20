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

1. config host file

        vi /etc/hosts

    The **hosts** file:

        127.0.0.1 localhost localhost.localdomain
        127.0.1.1 node01 # change name node01 to your node name

        10.111.0.111 nfs-server # change ip to your ip
        10.111.0.112 ansible-server # change ip to your ansible node ip
        10.111.0.113 node01  # change ip to your node ip
        10.111.0.114 node02  # change ip to your node ip
        10.111.0.115 node03 # change ip to your node ip

2. ansible node ssh

        ssh-keygen -t rsa
