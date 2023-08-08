# MetallLB

## Preparing kubernetes

    kubectl edit configmap -n kube-system kube-proxy
    #Then set​
    strictARP: true​

### install metallb

    kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.13.9/config/manifests/metallb-native.yaml

### check status

    kubectl -n metallb-system get po​

#### output expect

    NAME                          READY   STATUS    RESTARTS        AGE
    controller-5fd797fbf7-n5tmq   1/1     Running   3 (3h7m ago)    19d
    speaker-2wg48                 1/1     Running   3 (3h7m ago)    19d
    speaker-6gcgv                 1/1     Running   5 (3h14m ago)   19d
    speaker-rlq4s                 1/1     Running   4 (3h12m ago)   19d

### set ip

    kubectl apply -f ipaddresspool.yaml

    kubectl -n metallb-system get ipaddresspools.metallb.io
    
    NAME         AUTO ASSIGN   AVOID BUGGY IPS   ADDRESSES
    first-pool   true          false             ["10.111.0.119-10.111.0.130"]


> ref. <https://metallb.universe.tf/installation/>
