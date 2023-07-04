# Installation TiDB on Kubernetes

## Prerequisition

Step 1. Assume to have kube cluster already
helm should be preinstalled

Step 2. Deploy TiDB Operator
You need to install TiDB Operator CRDs first, and then install TiDB Operator.

### Install TiDB Operator CRDs

TiDB Operator includes a number of Custom Resource Definitions (CRDs) that implement different components of the TiDB cluster.

Run the following command to install the CRDs into your cluster:

    kubectl create -f https://raw.githubusercontent.com/pingcap/tidb-operator/master/manifests/crd.yaml

OR

    kubectl create -f https://raw.githubusercontent.com/pingcap/tidb-operator/v1.3.9/manifests/crd.yaml

Expected output:

    customresourcedefinition.apiextensions.k8s.io/tidbclusters.pingcap.com created
    customresourcedefinition.apiextensions.k8s.io/backups.pingcap.com created
    customresourcedefinition.apiextensions.k8s.io/restores.pingcap.com created
    customresourcedefinition.apiextensions.k8s.io/backupschedules.pingcap.com created
    customresourcedefinition.apiextensions.k8s.io/tidbmonitors.pingcap.com created
    customresourcedefinition.apiextensions.k8s.io/tidbinitializers.pingcap.com created
    customresourcedefinition.apiextensions.k8s.io/tidbclusterautoscalers.pingcap.com created

or v1.3.9

    customresourcedefinition.apiextensions.k8s.io/backupschedules.pingcap.com created
    customresourcedefinition.apiextensions.k8s.io/backups.pingcap.com created
    customresourcedefinition.apiextensions.k8s.io/dmclusters.pingcap.com created
    customresourcedefinition.apiextensions.k8s.io/restores.pingcap.com created
    customresourcedefinition.apiextensions.k8s.io/tidbclusterautoscalers.pingcap.com created
    customresourcedefinition.apiextensions.k8s.io/tidbclusters.pingcap.com created
    customresourcedefinition.apiextensions.k8s.io/tidbinitializers.pingcap.com created
    customresourcedefinition.apiextensions.k8s.io/tidbmonitors.pingcap.com created
    customresourcedefinition.apiextensions.k8s.io/tidbngmonitorings.pingcap.com created

> Note
> For Kubernetes earlier than 1.16, only v1beta1 CRD is supported.
> Therefore, you need to change crd.yaml in the preceding command to crd_v1beta1.yaml.

### Install TiDB Operator

This section describes how to install TiDB Operator using Helm 3.

1. Add the PingCAP repository:

        helm repo add pingcap https://charts.pingcap.org/

    • Expected output

        "pingcap" has been added to your repositories

    • Create a namespace for TiDB Operator:

        kubectl create namespace tidb-operator

    • Expected output

        namespace/tidb-operator created

    create file **tidb-operator-values.yaml**

        scheduler:
        create: true
        # With rbac.create=false, the user is responsible for creating this account
        # With rbac.create=true, this service account will be created
        # Also see rbac.create and clusterScoped
        serviceAccount: tidb-scheduler
        logLevel: 2
        replicas: 1
        schedulerName: tidb-scheduler
        resources:
            limits:
            cpu: 250m
            memory: 150Mi
            requests:
            cpu: 80m
            memory: 50Mi
        kubeSchedulerImageName: registry.k8s.io/kube-scheduler

    • Install TiDB Operator

        helm install --namespace tidb-operator tidb-operator pingcap/tidb-operator --version v1.3.9 -f tidb-operator-values.yaml

    • Expected output

        NAME: tidb-operator
        LAST DEPLOYED: Wed Jun 21 12:12:19 2023
        NAMESPACE: tidb-operator
        STATUS: deployed
        REVISION: 1
        TEST SUITE: None
        NOTES:
        Make sure tidb-operator components are running:

            kubectl get pods --namespace tidb-operator -l app.kubernetes.io/instance=tidb-operator

2. To confirm that the TiDB Operator components are running, run the following command:

        kubectl get pods --namespace tidb-operator -l app.kubernetes.io/instance=tidb-operator

    • Expected output

        NAME                                       READY   STATUS    RESTARTS   AGE
        tidb-controller-manager-7fb56cccb7-rm8dz   1/1     Running   0          10s
        tidb-scheduler-6b5cc4bd-kr2q4              2/2     Running   0          10s

    As soon as all Pods are in the "Running" state, proceed to the next step.

---

### Install TiDB cluster

Deploy a TiDB cluster and its monitoring services

This section describes how to deploy a TiDB cluster and its monitoring services.

> Note! TiFlash not need

#### Deploy a TiDB cluster

    kubectl create namespace tidb-cluster

• Expected output

    namespace/tidb-cluster created

• Install TiDB-cluster

    kubectl -n tidb-cluster apply -f tidb-cluster.yaml

• Expected output

    tidbcluster.pingcap.com/basic created

• Watch Pod

    watch kubectl -n tidb-cluster get po

• Get Logs

    kubectl logs -n tidb-cluster basic-tiflash-0 -c tiflash

> Note : see tidb-cluster.yaml file (edit storageclassname and size of TIKV & PD)
>
> IF error, change storage class to local-path

The **tidb-cluster.yaml** file:

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
        replicas: 2
        enableDashboardInternalProxy: true
        requests:
          cpu: "1"
          memory: "2Gi"
          storage: "5Gi"
        storageClassName: local-path #please change to match sc name
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
        evictLeaderTimeout: 1m
        replicas: 2
        requests:
          cpu: "1"
          memory: "2Gi"
          storage: "8Gi"
        storageClassName: local-path #please change to match sc name
        config:
          storage:
            reserve-space: "0MB"
        rocksdb:
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
        replicas: 2
        requests:
          cpu: "1"
          memory: "2Gi"
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
        replicas: 2
        requests:
          cpu: "1"
          memory: "2Gi"
        storageClaims:
          - resources:
              requests:
                storage: 5Gi
        storageClassName: local-path #please change to match sc name
        config: {}

---

### Deploy TiDB monitoring services

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

### TiDB Dashboard

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

## Connecting TiDB using Dbeaver

1. Download dbeaver
2. Connecting 10.xxx.x.xxx:4000

## Connecting Dashboard

        10.xxx.xxx.xxx:2379/dashboard
