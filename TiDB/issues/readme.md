# Issues

1. PV deploy on same node and pod try to deploy on same node too but it have pod anti-affinity.

    Error:
    ```Bash
    Events:
    Type     Reason            Age   From               Message
    ----     ------            ----  ----               -------
    Warning  FailedScheduling  106s  default-scheduler  0/3 nodes are available: pod has unbound immediate PersistentVolumeClaims. preemption: 0/3 nodes are available: 3 No preemption victims found for incoming pod..
    ```

    This is sc.
    ```Bash
    Name:            zpool-ext4
    IsDefaultClass:  No
    Annotations:     kubectl.kubernetes.io/last-applied-configuration={"allowVolumeExpansion":true,"apiVersion":"storage.k8s.io/v1","kind":"StorageClass","metadata":{"annotations":{},"name":"zpool-ext4"},"parameters":{"compression":"off","dedup":"off","fstype":"ext4","poolname":"z-pool","volblocksize":"4k"},"provisioner":"zfs.csi.openebs.io"}

    Provisioner:           zfs.csi.openebs.io
    Parameters:            compression=off,dedup=off,fstype=ext4,poolname=z-pool,volblocksize=4k
    AllowVolumeExpansion:  True
    MountOptions:          <none>
    ReclaimPolicy:         Delete
    VolumeBindingMode:     Immediate
    Events:                <none>
    ```
    Problem is `VolumeBindingMode`. 
    - The Immediate mode indicates that volume binding and dynamic provisioning occurs once the PersistentVolumeClaim is created. For storage backends that are topology-constrained and not globally accessible from all Nodes in the cluster, PersistentVolumes will be bound or provisioned without knowledge of the Pod's scheduling requirements. This may result in unschedulable Pods.
    - A cluster administrator can address this issue by specifying the WaitForFirstConsumer mode which will delay the binding and provisioning of a PersistentVolume until a Pod using the PersistentVolumeClaim is created. PersistentVolumes will be selected or provisioned conforming to the topology that is specified by the Pod's scheduling constraints. These include, but are not limited to, resource requirements, node selectors, pod affinity and anti-affinity, and taints and tolerations.

    Fix:

    Just change from Immediate to WaitForFirstConsumer.

    1. Change sc.
    2. Apply new sc.

    Example
    ```yaml
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
    name: zpool-ext4
    allowVolumeExpansion: true
    parameters:
    volblocksize: "4k"
    compression: "off"
    dedup: "off"
    fstype: "ext4"
    poolname: "z-pool"
    provisioner: zfs.csi.openebs.io
    volumeBindingMode: WaitForFirstConsumer
    ```


2. Pods with PersistentVolumeClaims (PVCs) are not getting scheduled, even though there are available PersistentVolumes (PVs). The error message indicates:

    ```bash
    Warning  FailedScheduling  0/3 nodes are available: pod has unbound immediate PersistentVolumeClaims. preemption: 0/3 nodes are available: 3 No preemption victims found for incoming pod..
    ```

    This issue is arising because of the `VolumeBindingMode` setting in the StorageClass. Currently, the `VolumeBindingMode` is set to `Immediate`, which means that the PV binding and dynamic provisioning occur as soon as the PVC is created. However, for storage backends that are topology-constrained and not globally accessible from all nodes, this can lead to problems. The PV might be bound or provisioned without considering the Pod's scheduling requirements, potentially resulting in unschedulable Pods.

    **Solution**:
    To resolve this, we should change the `VolumeBindingMode` from `Immediate` to `WaitForFirstConsumer`. In this mode, the PV binding and provisioning are delayed until a Pod that uses the PVC is created. This ensures that the PVs are selected or provisioned in accordance with the Pod's scheduling constraints, such as resource requirements, node selectors, pod affinity/anti-affinity, taints, and tolerations.

    **Steps**:

    1. Modify the StorageClass to use the `WaitForFirstConsumer` binding mode.
    2. Apply the updated StorageClass to the cluster.

    Here's an example of the updated StorageClass:

    ```yaml
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
    name: zpool-ext4
    allowVolumeExpansion: true
    parameters:
    volblocksize: "4k"
    compression: "off"
    dedup: "off"
    fstype: "ext4"
    poolname: "z-pool"
    provisioner: zfs.csi.openebs.io
    volumeBindingMode: WaitForFirstConsumer
    ```

    By implementing this change, the PVs will be provisioned in a way that is consistent with the Pod's scheduling constraints, resolving the scheduling issues.