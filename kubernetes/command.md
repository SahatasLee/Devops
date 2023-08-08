# Kubernetes Command

## Bacis command

    kubectl get nodes

output expect:

    NAME    STATUS   ROLES           AGE   VERSION
    node1   Ready    control-plane   21d   v1.26.5
    node2   Ready    control-plane   21d   v1.26.5
    node3   Ready    control-plane   21d   v1.26.5

---

    kubectl get pods 

output expect:

    NAME                       READY   STATUS    RESTARTS        AGE
    nfs-server-provisioner-0   1/1     Running   2 (3h30m ago)   3d23h

---

    kubectl get pods -o wide

output expect:

    NAME                       READY   STATUS    RESTARTS        AGE     IP             NODE    NOMINATED NODE   READINESS GATES
    nfs-server-provisioner-0   1/1     Running   2 (3h35m ago)   3d23h   10.233.71.35   node3   <none>           <none>

---

    kubectl describe pods

output expect:

    Namespace:        default
    Priority:         0
    Service Account:  nfs-server-provisioner
    Node:             node3/10.111.0.115
    Start Time:       Fri, 23 Jun 2023 14:49:36 +0700
    Labels:           app=nfs-server-provisioner
                    chart=nfs-server-provisioner-1.8.0
                    controller-revision-hash=nfs-server-provisioner-d5cbb7f57
                    heritage=Helm
                    release=nfs-server-provisioner
                    statefulset.kubernetes.io/pod-name=nfs-server-provisioner-0
    Annotations:      cni.projectcalico.org/containerID: 2cd598fd7b29e7e1ba2a3e9c0e19bf17988e67f1d2002d9e837ace4634fef8af
                    cni.projectcalico.org/podIP: 10.233.71.35/32
                    cni.projectcalico.org/podIPs: 10.233.71.35/32
    Status:           Running
    IP:               10.233.71.35
    IPs:
    IP:           10.233.71.35
    Controlled By:  StatefulSet/nfs-server-provisioner
    Containers:
    nfs-server-provisioner:
        Container ID:  containerd://0c22545df38ae09515a9133c5ed425fb604ffd5cea3cc1d19935285616c53cc6
        Image:         registry.k8s.io/sig-storage/nfs-provisioner:v4.0.8
        Image ID:      registry.k8s.io/sig-storage/nfs-provisioner@sha256:c825f3d5e28bde099bd7a3daace28772d412c9157ad47fa752a9ad0baafc118d
        Ports:         2049/TCP, 2049/UDP, 32803/TCP, 32803/UDP, 20048/TCP, 20048/UDP, 875/TCP, 875/UDP, 111/TCP, 111/UDP, 662/TCP, 662/UDP
        Host Ports:    0/TCP, 0/UDP, 0/TCP, 0/UDP, 0/TCP, 0/UDP, 0/TCP, 0/UDP, 0/TCP, 0/UDP, 0/TCP, 0/UDP
        Args:
        -provisioner=cluster.local/nfs-server-provisioner
        State:          Running
        Started:      Tue, 27 Jun 2023 11:15:45 +0700
        Last State:     Terminated
        Reason:       Error
        Exit Code:    2
        Started:      Tue, 27 Jun 2023 11:05:40 +0700
        Finished:     Tue, 27 Jun 2023 11:12:39 +0700
        Ready:          True
        Restart Count:  2
        Environment:
        POD_IP:          (v1:status.podIP)
        SERVICE_NAME:   nfs-server-provisioner
        POD_NAMESPACE:  default (v1:metadata.namespace)
        Mounts:
        /export from data (rw)
        /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-565n2 (ro)
    Conditions:
    Type              Status
    Initialized       True
    Ready             True
    ContainersReady   True
    PodScheduled      True
    Volumes:
    data:
        Type:       EmptyDir (a temporary directory that shares a pod's lifetime)
        Medium:
        SizeLimit:  <unset>
    kube-api-access-565n2:
        Type:                    Projected (a volume that contains injected data from multiple sources)
        TokenExpirationSeconds:  3607
        ConfigMapName:           kube-root-ca.crt
        ConfigMapOptional:       <nil>
        DownwardAPI:             true
    QoS Class:                   BestEffort
    Node-Selectors:              <none>
    Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                                node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
    Events:                      <none>

---

    kubectl get svc <tidb-service-name> -o yaml > tidb-service.yaml
