# OpenEBS

https://github.com/openebs/zfs-localpv/blob/develop/README.md

## Prerequisites

Before installing ZFS driver please make sure your Kubernetes Cluster must meet the following prerequisites:

- all the nodes must have zfs utils installed
- ZPOOL has been setup for provisioning the volume
- You have access to install RBAC components into kube-system namespace. The OpenEBS ZFS driver components are installed in kube-system namespace to allow them to be flagged as system critical components.

## Insalling

1. Add disk
2. Install zfsutils-linux

    ```Bash
    apt-get install zfsutils-linux
    ```
3. Create a new pool at new disk

    ```Bash
    zpool create zfspv-pool /dev/sdb
    ```

    > change /dev/sdb to your new disk

4. Verify status

    ```Bash
    sudo zpool status
    ```

5. Insall zfs-operator

    ```Bash
    kubectl apply -f https://openebs.github.io/charts/zfs-operator.yaml
    ```

    - Output :

    ```bash
    root@node1:~# kubectl apply -f https://openebs.github.io/charts/zfs-operator.yaml
    namespace/openebs created
    customresourcedefinition.apiextensions.k8s.io/zfsvolumes.zfs.openebs.io created
    customresourcedefinition.apiextensions.k8s.io/zfssnapshots.zfs.openebs.io created
    customresourcedefinition.apiextensions.k8s.io/zfsbackups.zfs.openebs.io created
    customresourcedefinition.apiextensions.k8s.io/zfsrestores.zfs.openebs.io created
    customresourcedefinition.apiextensions.k8s.io/zfsnodes.zfs.openebs.io created
    csidriver.storage.k8s.io/zfs.csi.openebs.io created
    customresourcedefinition.apiextensions.k8s.io/volumesnapshotclasses.snapshot.storage.k8s.io created
    customresourcedefinition.apiextensions.k8s.io/volumesnapshotcontents.snapshot.storage.k8s.io created
    customresourcedefinition.apiextensions.k8s.io/volumesnapshots.snapshot.storage.k8s.io created
    serviceaccount/openebs-zfs-controller-sa created
    clusterrole.rbac.authorization.k8s.io/openebs-zfs-provisioner-role created
    clusterrolebinding.rbac.authorization.k8s.io/openebs-zfs-provisioner-binding created
    priorityclass.scheduling.k8s.io/openebs-zfs-csi-controller-critical created
    statefulset.apps/openebs-zfs-controller created
    clusterrole.rbac.authorization.k8s.io/openebs-zfs-snapshotter-role created
    clusterrolebinding.rbac.authorization.k8s.io/openebs-zfs-snapshotter-binding created
    serviceaccount/openebs-zfs-node-sa created
    clusterrole.rbac.authorization.k8s.io/openebs-zfs-driver-registrar-role created
    clusterrolebinding.rbac.authorization.k8s.io/openebs-zfs-driver-registrar-binding created
    configmap/openebs-zfspv-bin created
    priorityclass.scheduling.k8s.io/openebs-zfs-csi-node-critical created
    daemonset.apps/openebs-zfs-node created
    ```

6. Create storage  class

    ```Bash
    kubectl apply -f sc-ext4.yaml
    ```

## Ref. 
- https://github.com/openebs/zfs-localpv
- https://github.com/openebs/zfs-localpv/blob/HEAD/docs/faq.md#6-how-to-add-custom-topology-key