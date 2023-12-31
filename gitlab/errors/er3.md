Gitlab and Runner is running on k8s.

1. I can `git clone`, `git push`.
2. Gitlab version ce 16.5.0
3. Git-runner version  image: registry.gitlab.com/gitlab-org/gitlab-runner:alpine-v16.6.0
4. UFW is disable.

When I try gitlab-ci, I got this error.
Full error
```bash
Running with gitlab-runner 16.6.0 (3046fee8)
  on gitlab-runner-76687b884d-ljmgh zzAt8-S8, system ID: r_ecd1uLtBtA3a
Preparing the "kubernetes" executor
00:00
Using Kubernetes namespace: gitlab
Using Kubernetes executor with image alpine ...
Using attach strategy to execute scripts...
Preparing environment
00:10
Using FF_USE_POD_ACTIVE_DEADLINE_SECONDS, the Pod activeDeadlineSeconds will be set to the job timeout: 1h0m0s...
Waiting for pod gitlab/runner-zzat8-s8-project-1-concurrent-0-s345dpl6 to be running, status is Pending
Waiting for pod gitlab/runner-zzat8-s8-project-1-concurrent-0-s345dpl6 to be running, status is Pending
	ContainersNotInitialized: "containers with incomplete status: [init-permissions]"
	ContainersNotReady: "containers with unready status: [build helper]"
	ContainersNotReady: "containers with unready status: [build helper]"
Waiting for pod gitlab/runner-zzat8-s8-project-1-concurrent-0-s345dpl6 to be running, status is Pending
	ContainersNotReady: "containers with unready status: [build helper]"
	ContainersNotReady: "containers with unready status: [build helper]"
Running on runner-zzat8-s8-project-1-concurrent-0-s345dpl6 via gitlab-runner-76687b884d-ljmgh...
Getting source from Git repository
00:02
Fetching changes with git depth set to 20...
Initialized empty Git repository in /builds/devops/kafka/.git/
Created fresh repository.
fatal: unable to access 'http://gitlab.khaolakonline.com/devops/kafka.git/': Failed to connect to gitlab.khaolakonline.com port 80 after 1061 ms: Couldn't connect to server
Cleaning up project directory and file based variables
00:00
ERROR: Job failed: command terminated with exit code 1
```

Checking Network

```bash
root@ansible-server:~# kubectl exec -i -t dnsutils -- nslookup gitlab-webservice-default.gitlab
Server:         169.254.25.10
Address:        169.254.25.10#53

Name:   gitlab-webservice-default.gitlab.svc.cluster.local
Address: 10.233.12.24

root@ansible-server:~# kubectl -n gitlab get ing
NAME                        CLASS          HOSTS                        ADDRESS        PORTS   AGE
gitlab-kas                  gitlab-nginx   kas.khaolakonline.com        10.111.0.117   80      23h
gitlab-minio                gitlab-nginx   minio.khaolakonline.com      10.111.0.117   80      23h
gitlab-registry             gitlab-nginx   registry.khaolakonline.com   10.111.0.117   80      23h
gitlab-webservice-default   gitlab-nginx   gitlab.khaolakonline.com     10.111.0.117   80      23h
root@ansible-server:~# kubectl exec -i -t dnsutils -- nslookup gitlab.khaolakonline.com
Server:         169.254.25.10
Address:        169.254.25.10#53

Name:   gitlab.com
Address: 10.111.0.117
```

curl

```
root@ansible-server:~# curl http://gitlab.khaolakonline.com
<html><body>You are being <a href="http://gitlab.khaolakonline.com/users/sign_in">redirected</a>.</body></html>
```