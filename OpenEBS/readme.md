# OpenEBS

## Prerequisites

## Insalling

```Bash
zpool create zfspv-pool /dev/sdb
```

Ref. (https://github.com/openebs/zfs-localpv)

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