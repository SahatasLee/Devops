# Git clone

```bash
C:\Users\sahatas.l>git clone https://gitlab.sahatas.com/devops/kafka-cicd.git
Cloning into 'kafka-cicd'...
fatal: unable to access 'https://gitlab.sahatas.com/devops/kafka-cicd.git/': SSL certificate problem: unable to get local issuer certificate
```

```bash
NAME                                              READY   STATUS      RESTARTS        AGE     IP             NODE    NOMINATED NODE   READINESS GATES
gitlab-gitlab-runner-fc887b94b-j8xzr              1/1     Running     0               16m     10.233.96.47   node2   <none>           <none>
```

```bash


root@ansible-server:~# kubectl -n gitlab exec -it gitlab-runner-1-6ccbc855c8-wtn2x -- cat /etc/resolv.conf
search gitlab.svc.cluster.local svc.cluster.local cluster.local default.svc.cluster.local
nameserver 169.254.25.10
options ndots:5

kubectl -n gitlab exec -it gitlab-runner-1-6ccbc855c8-wtn2x -- nslookup gitlab.sahatas.com
Server:         169.254.25.10
Address:        169.254.25.10:53

** server can't find gitlab.sahatas.com: NXDOMAIN

** server can't find gitlab.sahatas.com: NXDOMAIN

command terminated with exit code 1


kubectl -n gitlab exec -it gitlab-runner-68cb4b6bfd-bktsx -- cat /etc/gitlab-runner/config.toml

kubectl -n gitlab exec -it <gitlab-runner-pod-name> -- cat /etc/hosts

kubectl -n gitlab exec -it <gitlab-runner-pod-name> -- curl -v https://gitlab.sahatas.com

kubectl -n gitlab exec -it gitlab-runner-68cb4b6bfd-bktsx -- ping -c 4 gitlab.sahatas.com


```

```bash
[session_server]
  session_timeout = 1800

[[runners]]
  name = "gitlab-runner-69885fdd88-nrbkg"
  url = "http://gitlab-webservice-default.gitlab.svc.cluster.local:8080"
  id = 14
  token = "ipSU6fhSCQMjz1CcxFox"
  token_obtained_at = 2023-11-06T09:01:44Z
  token_expires_at = 0001-01-01T00:00:00Z
  executor = "kubernetes"
  [runners.cache]
    MaxUploadedArchiveSize = 0
  [runners.kubernetes]
    host = ""
    bearer_token_overwrite_allowed = false
    image = "alpine"
    namespace = "gitlab"
    namespace_overwrite_allowed = ""
    node_selector_overwrite_allowed = ""
    pod_labels_overwrite_allowed = ""
    service_account_overwrite_allowed = ""
    pod_annotations_overwrite_allowed = ""
    [runners.kubernetes.pod_security_context]
    [runners.kubernetes.init_permissions_container_security_context]
    [runners.kubernetes.build_container_security_context]
    [runners.kubernetes.helper_container_security_context]
    [runners.kubernetes.service_container_security_context]
    [runners.kubernetes.volumes]
    [runners.kubernetes.dns_config]

```

## Gitlab Runner

```bash
There might be a problem with your config based on jsonschema annotations in common/config.go (experimental feature):
jsonschema: '/runners/0/kubernetes/pull_policy' does not validate with https://gitlab.com/gitlab-org/gitlab-runner/common/config#/$ref/properties/runners/items/$ref/properties/kubernetes/$ref/properties/pull_policy/$ref/type: expected array, but got null

Configuration loaded                                builds=0 max_builds=10
listen_address not defined, metrics & debug endpoints disabled  builds=0 max_builds=10
[session_server].listen_address not defined, session endpoints disabled  builds=0 max_builds=10
Initializing executor providers                     builds=0 max_builds=10

```

## Certificate
```bash
spec:
  dnsNames:
  - gitlab.khaolakonline.com
  issuerRef:
    group: cert-manager.io
    kind: Issuer
    name: gitlab-issuer
  secretName: gitlab-gitlab-tls
  usages:
  - digital signature
  - key encipherment
status:
  conditions:
  - lastTransitionTime: "2023-11-17T03:53:51Z"
    message: 'Existing issued Secret is not up to date for spec: [spec.dnsNames]'
```


{"component": "gitlab","subcomponent":"api_json","time":"2023-11-23T08:49:02.604Z","severity":"INFO","duration_s":0.01748,"db_duration_s":0.00288,"view_duration_s":0.0146,"status":200,"method":"POST","path":"/api/v4/runners/verify","params":[{"key":"token","value":"[FILTERED]"},{"key":"system_id","value":"r_6gOqHfrdi8Rr"}],"host":"gitlab-webservice-default.gitlab.svc.cluster.local","remote_ip":"10.233.90.145","ua":"gitlab-runner 16.6.0 (16-6-stable; go1.20.10; linux/amd64)","route":"/api/:version/runners/verify","redis_calls":10,"redis_duration_s":0.003608,"redis_read_bytes":406,"redis_write_bytes":990,"redis_cache_calls":4,"redis_cache_duration_s":0.001545,"redis_cache_read_bytes":406,"redis_cache_write_bytes":558,"redis_shared_state_calls":6,"redis_shared_state_duration_s":0.002063,"redis_shared_state_write_bytes":432,"db_count":2,"db_write_count":0,"db_cached_count":0,"db_replica_count":0,"db_primary_count":2,"db_main_count":0,"db_ci_count":2,"db_main_replica_count":0,"db_ci_replica_count":0,"db_replica_cached_count":0,"db_primary_cached_count":0,"db_main_cached_count":0,"db_ci_cached_count":0,"db_main_replica_cached_count":0,"db_ci_replica_cached_count":0,"db_replica_wal_count":0,"db_primary_wal_count":0,"db_main_wal_count":0,"db_ci_wal_count":0,"db_main_replica_wal_count":0,"db_ci_replica_wal_count":0,"db_replica_wal_cached_count":0,"db_primary_wal_cached_count":0,"db_main_wal_cached_count":0,"db_ci_wal_cached_count":0,"db_main_replica_wal_cached_count":0,"db_ci_replica_wal_cached_count":0,"db_replica_duration_s":0.0,"db_primary_duration_s":0.003,"db_main_duration_s":0.0,"db_ci_duration_s":0.003,"db_main_replica_duration_s":0.0,"db_ci_replica_duration_s":0.0,"cpu_s":0.022379,"mem_objects":7670,"mem_bytes":820832,"mem_mallocs":2098,"mem_total_bytes":1127632,"pid":44,"worker_id":"puma_0","rate_limiting_gates":[],"correlation_id":"44a1d783-d4d8-4f51-9b52-a597f7f526e1","meta.caller_id":"POST /api/:version/runners/verify","meta.remote_ip":"10.233.90.145","meta.feature_category":"runner","meta.client_id":"runner/1","content_length":"61","request_urgency":"low","target_duration_s":5}
