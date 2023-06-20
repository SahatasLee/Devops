# Installation TiDB on Kubernetes

## Prerequisition

Step 1. Assume to have kube cluster already
helm should be preinstalled
Step 2. Deploy TiDB Operator
You need to install TiDB Operator CRDs first, and then install TiDB Operator.

Install TiDB Operator CRDs
TiDB Operator includes a number of Custom Resource Definitions (CRDs) that implement different components of the TiDB cluster.
Run the following command to install the CRDs into your cluster:

    kubectl create -f https://raw.githubusercontent.com/pingcap/tidb-operator/master/manifests/crd.yaml

OR

    kubectl create -f https://raw.githubusercontent.com/pingcap/tidb-operator/v1.3.9/manifests/crd.yaml

Expected output

Note
For Kubernetes earlier than 1.16, only v1beta1 CRD is supported. Therefore, you need to change crd.yaml in the preceding command to crd_v1beta1.yaml.

## Install TiDB Operator

This section describes how to install TiDB Operator using Helm 3.

1. Add the PingCAP repository:

        helm repo add pingcap https://charts.pingcap.org/

    • Expected output
    • Create a namespace for TiDB Operator:

        kubectl create namespace tidb-operator

    • Expected output
    • Install TiDB Operator

        helm install --namespace tidb-operator tidb-operator pingcap/tidb-operator --version v1.3.9

2. To confirm that the TiDB Operator components are running, run the following command:

        kubectl get pods --namespace tidb-operator -l app.kubernetes.io/instance=tidb-operator

    **Expected output:**

    As soon as all Pods are in the "Running" state, proceed to the next step.

3. Deploy a TiDB cluster and its monitoring services

    This section describes how to deploy a TiDB cluster and its monitoring services.

    **Deploy a TiDB cluster**

        kubectl create namespace tidb-cluster

        kubectl -n tidb-cluster apply -f tidb-cluster.yaml

> Note : see tidb-cluster.yaml file (edit storageclassname and size of TIKV & PD)

---

The **Tidb-cluster.yaml** file:

    apiVersion: pingcap.com/v1alpha1
    kind: TidbCluster
    metadata:
    name: basic
    namespace: tidb-cluster
    spec:
    version: v6.1.0
    timezone: Asia/Bangkok
    pvReclaimPolicy: Retain
    enableDynamicConfiguration: true
    configUpdateStrategy: RollingUpdate
    discovery: {}
    helper:
        image: alpine:3.16.0
    pd:
        baseImage: pingcap/pd
        maxFailoverCount: 0
        replicas: 3
        # if storageClassName is not set, the default Storage Class of the Kubernetes cluster will be used
        enableDashboardInternalProxy: true
        #limits:
        #cpu: "8"
        #memory: "16Gi"
        requests:
        cpu: "4"
        memory: "8Gi"
        storage: "5Gi"
        storageClassName: ceph-block #please change to match sc name
        service:
        type: LoadBalancer
        affinity:
            podAntiAffinity:
                requiredDuringSchedulingIgnoredDuringExecution:
                - labelSelector:
                    matchExpressions:
                        - key: app.kubernetes.io/component
                        operator: In
                        values:
                            - pd
                    topologyKey: "kubernetes.io/hostname"
        config: {}
    tikv:
        baseImage: pingcap/tikv
        maxFailoverCount: 0
        # If only 1 TiKV is deployed, the TiKV region leader 
        # cannot be transferred during upgrade, so we have
        # to configure a short timeout
        evictLeaderTimeout: 1m
        replicas: 3
        # if storageClassName is not set, the default Storage Class of the Kubernetes cluster will be used
        #limits:
        #cpu: "16"
        #memory: "64Gi"
        requests:
        cpu: "8"
        memory: "32Gi"
        storage: "8Gi"
        storageClassName: ceph-block #please change to match sc name
        config:
        storage:
            # In basic examples, we set this to avoid using too much storage.
            reserve-space: "0MB"
        rocksdb:
            # In basic examples, we set this to avoid the following error in some Kubernetes clusters:
            # "the maximum number of open file descriptors is too small, got 1024, expect greater or equal to 82920"
            max-open-files: 256
        raftdb:
            max-open-files: 256
        affinity:
            podAntiAffinity:
                requiredDuringSchedulingIgnoredDuringExecution:
                - labelSelector:
                    matchExpressions:
                        - key: app.kubernetes.io/component
                        operator: In
                        values:
                            - tikv
                    topologyKey: "kubernetes.io/hostname"
    tidb:
        baseImage: pingcap/tidb
        maxFailoverCount: 0
        replicas: 3
        limits:
        #cpu: "16"
        #memory: "48Gi"
        requests:
        cpu: "8"
        memory: "24Gi" 
        service:
        type: LoadBalancer
        affinity:
            podAntiAffinity:
                requiredDuringSchedulingIgnoredDuringExecution:
                - labelSelector:
                    matchExpressions:
                        - key: app.kubernetes.io/component
                        operator: In
                        values:
                            - tidb
                    topologyKey: "kubernetes.io/hostname"
        config: {}
    tiflash:
        affinity:
        podAntiAffinity:
            requiredDuringSchedulingIgnoredDuringExecution:
            - labelSelector:
                matchExpressions:
                - key: app.kubernetes.io/component
                operator: In
                values:
                - tiflash
            topologyKey: kubernetes.io/hostname
        baseImage: pingcap/tiflash
        maxFailoverCount: 0
        replicas: 3
        limits:
        #cpu: "48"
        #memory: "128Gi"
        requests:
        cpu: "8"
        memory: "24Gi"
        storageClaims:
        - resources:
            requests:
            storage: 5Gi
        storageClassName: ceph-block #please change to match sc name
        config: {}

---

## Deploy TiDB monitoring services

    kubectl -n tidb-cluster apply -f tidb-monitoring.yaml

The **tidb-monitoring.yaml** file:

    apiVersion: pingcap.com/v1alpha1
    kind: TidbMonitor
    metadata:
    name: basic
    namespace: tidb-cluster
    spec:
    replicas: 1
    clusters:
    - name: basic
    prometheus:
        baseImage: prom/prometheus
        version: v2.27.1
    grafana:
        baseImage: grafana/grafana
        version: 7.5.11
    initializer:
        baseImage: pingcap/tidb-monitor-initializer
        version: v6.1.0
    reloader:
        baseImage: pingcap/tidb-monitor-reloader
        version: v1.0.1
    prometheusReloader:
        baseImage: quay.io/prometheus-operator/prometheus-config-reloader
        version: v0.49.0
    imagePullPolicy: IfNotPresent

---

## TiDB Dashboard

    kubectl apply -n tidb-cluster -f tidbngmonitoring.yaml

The **tidbngmonitoring.yaml** file:

    apiVersion: pingcap.com/v1alpha1
    kind: TidbNGMonitoring
    metadata:
    name: basic
    spec:
    clusters:
    - name: basic
        namespace: tidb-cluster
    ngMonitoring:
        requests:
        storage: 1Gi
        version: v6.1.0
        # storageClassName: default
        baseImage: pingcap/ng-monitoring

> (NOT USE above)

        kubectl -n tidb-cluster apply -f https://raw.githubusercontent.com/pingcap/tidb-operator/master/examples/basic/tidb-monitor.yaml

Expected output

    http://lbip:2379/dashboard Login with root

View the Pod status

    watch kubectl get po -n tidb-cluster

Expected output

> Wait until all Pods for all services are started. As soon as you see Pods of each type (-pd, -tikv, and -tidb) are in the "Running" state, you can press Ctrl+C to get back to the command line and go on to connect to your TiDB cluster.

From <https://docs.pingcap.com/tidb-in-kubernetes/dev/get-started#step-2-deploy-tidb-operator>
