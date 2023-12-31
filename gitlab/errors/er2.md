# Unable to access

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

Can 
1. Git clone 
2. Git push
3. Gitlab version ce 16.5.0
4. image: registry.gitlab.com/gitlab-org/gitlab-runner:alpine-v16.6.0


