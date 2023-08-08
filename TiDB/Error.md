# Error

## tiflash

• Get Logs

    kubectl logs -n tidb-cluster basic-tiflash-0 -c tiflash

• Output

    root@node1:~/tidb# kubectl logs -n tidb-cluster basic-tiflash-0 -c tiflash
    Logging debug to /data0/logs/server.log
    Logging errors to /data0/logs/error.log
    [2023/06/22 22:39:35.533 +07:00] [INFO] [lib.rs:37] ["Welcome To RaftStore Proxy"]
    [2023/06/22 22:39:35.533 +07:00] [INFO] [lib.rs:39] ["Git Commit Hash:   7578b8163992ce933074135f8687ad447d88ea9b"]
    [2023/06/22 22:39:35.533 +07:00] [INFO] [lib.rs:39] ["Git Commit Branch: HEAD"]
    [2023/06/22 22:39:35.533 +07:00] [INFO] [lib.rs:39] ["UTC Build Time:    2022-06-07 12:01:49"]
    [2023/06/22 22:39:35.533 +07:00] [INFO] [lib.rs:39] ["Rust Version:      rustc 1.60.0-nightly (1e12aef3f 2022-02-13)"]
    [2023/06/22 22:39:35.534 +07:00] [INFO] [lib.rs:39] ["Storage Engine:    tiflash"]
    [2023/06/22 22:39:35.534 +07:00] [INFO] [lib.rs:39] ["Prometheus Prefix: tiflash_proxy_"]
    [2023/06/22 22:39:35.534 +07:00] [INFO] [lib.rs:39] ["Profile:           release"]
    [2023/06/22 22:39:35.534 +07:00] [INFO] [mod.rs:73] ["cgroup quota: memory=9223372036854771712, cpu=None, cores={7, 6, 3, 0, 1, 5, 2, 4}"]
    [2023/06/22 22:39:35.543 +07:00] [INFO] [mod.rs:80] ["memory limit in bytes: 34749581312, cpu cores quota: 8"]
    [2023/06/22 22:39:35.544 +07:00] [WARN] [server.rs:1394] ["check: kernel"] [err="kernel parameters net.core.somaxconn got 4096, expect 32768"]
    [2023/06/22 22:39:35.544 +07:00] [WARN] [server.rs:1394] ["check: kernel"] [err="kernel parameters net.ipv4.tcp_syncookies got 1, expect 0"]
    [2023/06/22 22:39:35.544 +07:00] [WARN] [server.rs:1394] ["check: kernel"] [err="kernel parameters vm.swappiness got 60, expect 0"]
    [2023/06/22 22:39:35.556 +07:00] [INFO] [util.rs:547] ["connecting to PD endpoint"] [endpoints=basic-pd.tidb-cluster.svc:2379]
    [2023/06/22 22:39:35.565 +07:00] [INFO] [<unknown>] ["TCP_USER_TIMEOUT is available. TCP_USER_TIMEOUT will be used thereafter"]
    [2023/06/22 22:39:35.570 +07:00] [INFO] [util.rs:547] ["connecting to PD endpoint"] [endpoints=http://basic-pd-2.basic-pd-peer.tidb-cluster.svc:2379]
    [2023/06/22 22:39:35.612 +07:00] [INFO] [util.rs:547] ["connecting to PD endpoint"] [endpoints=http://basic-pd-1.basic-pd-peer.tidb-cluster.svc:2379]
    [2023/06/22 22:39:35.632 +07:00] [INFO] [util.rs:673] ["connected to PD member"] [endpoints=http://basic-pd-1.basic-pd-peer.tidb-cluster.svc:2379]
    [2023/06/22 22:39:35.632 +07:00] [INFO] [util.rs:539] ["all PD endpoints are consistent"] [endpoints="[\"basic-pd.tidb-cluster.svc:2379\"]"]
    [2023/06/22 22:39:35.656 +07:00] [INFO] [server.rs:434] ["connect to PD cluster"] [cluster_id=7247456890130936905]
    [2023/06/22 22:39:35.656 +07:00] [INFO] [config.rs:2005] ["readpool.storage.use-unified-pool is not set, set to true by default"]
    [2023/06/22 22:39:35.657 +07:00] [INFO] [config.rs:2028] ["readpool.coprocessor.use-unified-pool is not set, set to true by default"]
    [2023/06/22 22:39:36.031 +07:00] [INFO] [server.rs:1402] ["beginning system configuration check"]
    [2023/06/22 22:39:36.031 +07:00] [FATAL] [server.rs:1413] ["the maximum number of open file descriptors is too small, got 65535, expect greater or equal to 82920"]

## tikv

• Get Logs

    kubectl logs -n tidb-cluster basic-tiflash-0 -c tiflash

• Output

    root@node1:~/tidb# kubectl logs -n tidb-cluster basic-tikv-0 -c tikv
    starting tikv-server ...
    /tikv-server --pd=http://basic-pd:2379 --advertise-addr=basic-tikv-0.basic-tikv-peer.tidb-cluster.svc:20160 --addr=0.0.0.0:20160 --status-addr=0.0.0.0:20180 --advertise-status-addr=basic-tikv-0.basic-tikv-peer.tidb-cluster.svc:20180 --data-dir=/var/lib/tikv --capacity=0 --config=/etc/tikv/tikv.toml

    [2023/06/22 22:49:47.422 +07:00] [INFO] [lib.rs:79] ["Welcome to TiKV"]
    [2023/06/22 22:49:47.423 +07:00] [INFO] [lib.rs:84] ["Release Version:   6.1.0"]
    [2023/06/22 22:49:47.423 +07:00] [INFO] [lib.rs:84] ["Edition:           Community"]
    [2023/06/22 22:49:47.423 +07:00] [INFO] [lib.rs:84] ["Git Commit Hash:   080d086832ae5ce2495352dccaf8df5d40f30687"]
    [2023/06/22 22:49:47.423 +07:00] [INFO] [lib.rs:84] ["Git Commit Branch: heads/refs/tags/v6.1.0"]
    [2023/06/22 22:49:47.423 +07:00] [INFO] [lib.rs:84] ["UTC Build Time:    Unknown (env var does not exist when building)"]
    [2023/06/22 22:49:47.423 +07:00] [INFO] [lib.rs:84] ["Rust Version:      rustc 1.60.0-nightly (1e12aef3f 2022-02-13)"]
    [2023/06/22 22:49:47.423 +07:00] [INFO] [lib.rs:84] ["Enable Features:   jemalloc mem-profiling portable sse test-engine-kv-rocksdb test-engine-raft-raft-engine cloud-aws cloud-gcp cloud-azure"]
    [2023/06/22 22:49:47.423 +07:00] [INFO] [lib.rs:84] ["Profile:           dist_release"]
    [2023/06/22 22:49:47.423 +07:00] [INFO] [mod.rs:74] ["cgroup quota: memory=Some(9223372036854771712), cpu=None, cores={4, 5, 6, 1, 7, 0, 3, 2}"]
    [2023/06/22 22:49:47.434 +07:00] [INFO] [mod.rs:81] ["memory limit in bytes: 34749581312, cpu cores quota: 8"]
    [2023/06/22 22:49:47.435 +07:00] [WARN] [server.rs:1533] ["check: kernel"] [err="kernel parameters net.core.somaxconn got 4096, expect 32768"]
    [2023/06/22 22:49:47.435 +07:00] [WARN] [server.rs:1533] ["check: kernel"] [err="kernel parameters net.ipv4.tcp_syncookies got 1, expect 0"]
    [2023/06/22 22:49:47.435 +07:00] [WARN] [server.rs:1533] ["check: kernel"] [err="kernel parameters vm.swappiness got 60, expect 0"]
    [2023/06/22 22:49:47.454 +07:00] [INFO] [util.rs:575] ["connecting to PD endpoint"] [endpoints=http://basic-pd:2379]
    [2023/06/22 22:49:47.468 +07:00] [INFO] [<unknown>] ["TCP_USER_TIMEOUT is available. TCP_USER_TIMEOUT will be used thereafter"]
    [2023/06/22 22:49:47.473 +07:00] [INFO] [util.rs:575] ["connecting to PD endpoint"] [endpoints=http://basic-pd-2.basic-pd-peer.tidb-cluster.svc:2379]
    [2023/06/22 22:49:47.488 +07:00] [INFO] [util.rs:575] ["connecting to PD endpoint"] [endpoints=http://basic-pd-1.basic-pd-peer.tidb-cluster.svc:2379]
    [2023/06/22 22:49:47.497 +07:00] [INFO] [util.rs:701] ["connected to PD member"] [endpoints=http://basic-pd-1.basic-pd-peer.tidb-cluster.svc:2379]
    [2023/06/22 22:49:47.498 +07:00] [INFO] [util.rs:567] ["all PD endpoints are consistent"] [endpoints="[\"http://basic-pd:2379\"]"]
    [2023/06/22 22:49:47.500 +07:00] [INFO] [server.rs:369] ["connect to PD cluster"] [cluster_id=7247456890130936905]
    [2023/06/22 22:49:47.501 +07:00] [INFO] [config.rs:2041] ["readpool.storage.use-unified-pool is not set, set to true by default"]
    [2023/06/22 22:49:47.501 +07:00] [INFO] [config.rs:2064] ["readpool.coprocessor.use-unified-pool is not set, set to true by default"]
    [2023/06/22 22:49:47.507 +07:00] [FATAL] [setup.rs:304] ["invalid configuration: Found raft data set when it should not exist."]

### SVC

    Name:                     basic-pd
    Namespace:                tidb-cluster
    Labels:                   app.kubernetes.io/component=pd
                            app.kubernetes.io/instance=basic
                            app.kubernetes.io/managed-by=tidb-operator
                            app.kubernetes.io/name=tidb-cluster
                            app.kubernetes.io/used-by=end-user
    Annotations:              metallb.universe.tf/ip-allocated-from-pool: first-pool
                            pingcap.com/last-applied-configuration:
                                {"ports":[{"name":"client","protocol":"TCP","port":2379,"targetPort":2379}],"selector":{"app.kubernetes.io/component":"pd","app.kubernetes...
    Selector:                 app.kubernetes.io/component=pd,app.kubernetes.io/instance=basic,app.kubernetes.io/managed-by=tidb-operator,app.kubernetes.io/name=tidb-cluster
    Type:                     LoadBalancer
    IP Family Policy:         SingleStack
    IP Families:              IPv4
    IP:                       10.233.37.178
    IPs:                      10.233.37.178
    LoadBalancer Ingress:     10.111.0.116
    Port:                     client  2379/TCP
    TargetPort:               2379/TCP
    NodePort:                 client  32486/TCP
    Endpoints:                10.233.102.177:2379,10.233.71.45:2379
    Session Affinity:         None
    External Traffic Policy:  Cluster
    Events:
    Type    Reason       Age   From                Message
    ----    ------       ----  ----                -------
    Normal  IPAllocated  104s  metallb-controller  Assigned IP ["10.111.0.116"]
