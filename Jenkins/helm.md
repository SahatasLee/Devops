# Helm

```bash
helm repo add jenkinsci https://charts.jenkins.io
helm repo update

kubectl apply -f jenkins-volume.yaml -n jenkins

kubectl apply -f jenkins-sa.yaml -n jenkins

kubectl apply -f jenkins-sa.yaml -f jenkins-volume.yaml -n jenkins

kubectl delete -f jenkins-sa.yaml -f jenkins-volume.yaml -n jenkins

helm install jenkins -n jenkins -f values.yaml jenkinsci/jenkins

helm delete jenkins -n jenkins

kubectl logs -f jenkins-0 -c init -n jenkins 

kubectl logs jenkins-0 -n jenkins -c config-reload

# show containers
kubectl get pods jenkins-0 -o jsonpath='{.spec.containers[*].name}'

kubectl logs -f jenkins-0 -c jenkins -n jenkins

kubectl -n jenkins exec -it jenkins-0 -- /bin/bash

# get password
jsonpath="{.data.jenkins-admin-password}"
secret=$(kubectl get secret -n jenkins jenkins -o jsonpath=$jsonpath)
echo $(echo $secret | base64 --decode)

# get password
kubectl get secret -n jenkins jenkins -o jsonpath="{.data.jenkins-admin-password}" | base64 --decode

2c46K6DB6rYtvFx5ogivXb

# get url
jsonpath="{.spec.ports[0].nodePort}"
NODE_PORT=$(kubectl get -n jenkins -o jsonpath=$jsonpath services jenkins)
jsonpath="{.items[0].status.addresses[0].address}"
NODE_IP=$(kubectl get nodes -n jenkins -o jsonpath=$jsonpath)
echo http://$NODE_IP:$NODE_PORT/login

http://10.111.0.113:30175/login
```

add to `value.yaml`

```bash
  initContainerEnv:
  - name: CACHE_DIR
    value: "/tmp/cache"
```

```bash
NAME: jenkins
LAST DEPLOYED: Tue Jan 30 16:00:01 2024
NAMESPACE: jenkins
STATUS: deployed
REVISION: 1
NOTES:
1. Get your 'admin' user password by running:
  kubectl exec --namespace jenkins -it svc/jenkins -c jenkins -- /bin/cat /run/secrets/additional/chart-admin-password && echo
2. Get the Jenkins URL to visit by running these commands in the same shell:
  NOTE: It may take a few minutes for the LoadBalancer IP to be available.
        You can watch the status of by running 'kubectl get svc --namespace jenkins -w jenkins'
  export SERVICE_IP=$(kubectl get svc --namespace jenkins jenkins --template "{{ range (index .status.loadBalancer.ingress 0) }}{{ . }}{{ end }}")
  echo http://$SERVICE_IP:8080

3. Login with the password from step 1 and the username: admin
4. Configure security realm and authorization strategy
5. Use Jenkins Configuration as Code by specifying configScripts in your values.yaml file, see documentation: http://$SERVICE_IP:8080/configuration-as-code and examples: https://github.com/jenkinsci/configuration-as-code-plugin/tree/master/demos

For more information on running Jenkins on Kubernetes, visit:
https://cloud.google.com/solutions/jenkins-on-container-engine

For more information about Jenkins Configuration as Code, visit:
https://jenkins.io/projects/jcasc/


NOTE: Consider using a custom image with pre-installed plugins
```

## 

```bash
  Warning  FailedScheduling  100s  default-scheduler  0/4 nodes are available: 4 node(s) didn't find available persistent volumes to bind.
  Warning  FailedScheduling  26s   default-scheduler  0/4 nodes are available: 4 node(s) didn't find available persistent volumes to bind.

  Normal  WaitForFirstConsumer  2m32s                persistentvolume-controller  waiting for first consumer to be created before binding
  Normal  WaitForPodScheduled   4s (x10 over 2m19s)  persistentvolume-controller  waiting for pod jenkins-0 to be scheduled
```

## Permission denied on disable Setup Wizard step

```bash
root@ansible-server:~# kubectl logs -f jenkins-0 -c init -n jenkins
disable Setup Wizard
/var/jenkins_config/apply_config.sh: 4: cannot create /var/jenkins_home/jenkins.install.UpgradeWizard.state: Permission denied
root@ansible-server:~#
```

https://github.com/jenkinsci/helm-charts/issues/210

## Error while deploying on OpenShift: AccessDeniedException: /.cache

```bash
disable Setup Wizard
download plugins
File containing list of plugins to be downloaded: /var/jenkins_home/plugins.txt
Reading in plugins from /var/jenkins_home/plugins.txt

No directory to download plugins entered. Will use default of /usr/share/jenkins/ref/plugins
Using update center https://updates.jenkins.io/update-center.json from JENKINS_UC environment variable
Using experimental update center https://updates.jenkins.io/experimental/update-center.json from JENKINS_UC_EXPERIMENTAL environment variable
Using incrementals mirror https://repo.jenkins-ci.org/incrementals from JENKINS_INCREMENTALS_REPO_MIRROR environment variable
No CLI option or environment variable set for plugin info, using default of https://updates.jenkins.io/plugin-versions.json
Will use war file: /usr/share/jenkins/jenkins.war

Retrieving update center information
java.io.UncheckedIOException: java.nio.file.FileSystemException: /root/.cache: Read-only file system
        at io.jenkins.tools.pluginmanager.impl.CacheManager.createCache(CacheManager.java:48)
        at io.jenkins.tools.pluginmanager.impl.PluginManager.getUCJson(PluginManager.java:849)
        at io.jenkins.tools.pluginmanager.impl.PluginManager.start(PluginManager.java:225)
        at io.jenkins.tools.pluginmanager.impl.PluginManager.start(PluginManager.java:189)
        at io.jenkins.tools.pluginmanager.cli.Main.main(Main.java:52)
Caused by: java.nio.file.FileSystemException: /root/.cache: Read-only file system
        at java.base/sun.nio.fs.UnixException.translateToIOException(UnixException.java:100)
        at java.base/sun.nio.fs.UnixException.rethrowAsIOException(UnixException.java:106)
        at java.base/sun.nio.fs.UnixException.rethrowAsIOException(UnixException.java:111)
        at java.base/sun.nio.fs.UnixFileSystemProvider.createDirectory(UnixFileSystemProvider.java:397)
        at java.base/java.nio.file.Files.createDirectory(Files.java:700)
        at io.jenkins.tools.pluginmanager.impl.CacheManager.createCache(CacheManager.java:43)
        ... 4 more
java.nio.file.FileSystemException: /root/.cache: Read-only file system
```

https://github.com/jenkinsci/helm-charts/issues/506

add to `value.yaml`

```bash
  initContainerEnv:
  - name: CACHE_DIR
    value: "/tmp/cache"
```