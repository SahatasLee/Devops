# Add Worker Node

1. config new node 

ให้ ansible สามารถ ssh เป็น root เข้า node4 (new node) ได้

```bash
ssh node4
```

2. config /inventory/kubernetes/hosts.yaml

add `all.hosts.new-node`
add `all.children.kube_node.hosts.new-node`

```bash
all:
  hosts:
    node1:
      ansible_host: node1
      ip: 10.111.0.113
      access_ip: 10.111.0.113
    node2:
      ansible_host: node2
      ip: 10.111.0.114
      access_ip: 10.111.0.114
    node3:
      ansible_host: node3
      ip: 10.111.0.115
      access_ip: 10.111.0.115
    node4: ## New Node
      ansible_host: node4
      ip: 10.111.0.116
      access_ip: 10.111.0.116
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
        node4: ## Add New Worker Node
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

3. run ansible

```bash
 ansible-playbook -i inventory/kubecluster/hosts.yaml cluster.yml -b -l new-node
```

Example

```bash
 ansible-playbook -i inventory/kubecluster/hosts.yaml cluster.yml -b -l node4
```
