# CI/CD

- [ ] Test push an image to private repo docker hub.

This is `.gitlab-ci.yaml` file.

```yaml
stages: 
  - build
  - deploy

build:
  stage: build
  image:
    name: gcr.io/kaniko-project/executor:v1.14.0-debug
    entrypoint: [""]
  script:
    - echo "{\"auths\":{\"$CI_REGISTRY\":{\"username\":\"$CI_REGISTRY_USER\",\"password\":\"$CI_REGISTRY_PASSWORD\"}}}" > /kaniko/.docker/config.json
    - /kaniko/executor
      --context "${CI_PROJECT_DIR}"
      --dockerfile "${CI_PROJECT_DIR}/Dockerfile"
      --destination "${CI_REGISTRY_IMAGE}:${CI_COMMIT_TAG}"

deploy:
  stage: deploy
  image: ubuntu:latest
  before_script:
    # Install the SSH client
    - apt-get update && apt-get install -y openssh-client
    - chmod 400 $SSH_KEY
  script:
    - ssh -o StrictHostKeyChecking=no -i $SSH_KEY root@10.111.0.113 "
        kubectl run cicd --image=${CI_REGISTRY_IMAGE}:${CI_COMMIT_TAG} 
        "
```

>IMAGE_NAME=nutlee22/cicd-demo
>IMAGE_TAG=latest

Using context

```yaml
deploy:
  image:
    name: bitnami/kubectl:latest
    entrypoint: ['']
  script:
    - kubectl config get-contexts
    - kubectl config use-context path/to/agent/project:agent-name
    - kubectl get pods
```

## Container Registry

```bash
docker login registry.khaolakonline.com
docker logout registry.khaolakonline.com

openssl s_client -showcerts -connect gitlab.example.com:443 -servername gitlab.example.com < /dev/null 2>/dev/null | openssl x509 -outform PEM > /etc/gitlab-runner/certs/gitlab.example.com.crt

cp gitlab-registry.crt /usr/share/ca-certificates/gitlab-registry.crt
cp gitlab-registry.crt /usr/local/share/ca-certificates/gitlab-registry.crt
cp gitlab-registry.crt /etc/docker/certs.d/registry.khaolakonline.com/ca.crt
openssl s_client -connect registry.khaolakonline.com:443

docker tag <image-name>:<tag> registry.khaolakonline.com/<namespace>/<project>:<tag>

# For testing
docker tag nginx:latest registry.khaolakonline.com/root/cicd-demo:latest

docker build -t registry.khaolakonline.com/root/cicd-demo:latest .

docker push registry.khaolakonline.com/root/cicd-demo:latest

docker tag nginx:latest nutlee22/cicd-demo:latest

docker push nutlee22/cicd-demo:latest
```

## To deploy an application from an image stored in the GitLab Container Registry to a Kubernetes cluster

This is `deployment.yaml` file

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cicd-demo
spec:
  replicas: 3
  selector:
    matchLabels:
      app: cicd-demo
  template:
    metadata:
      labels:
        app: cicd-demo
    spec:
      containers:
      - name: cicd-demo
        image: registry.khaolakonline.com/root/cicd-demo:latest
        ports:
        - containerPort: 80
      imagePullSecrets:
      - name: regcred
```

This is `service.yaml` file

```bash
apiVersion: v1
kind: Service
metadata:
  name: cicd-demo
spec:
  selector:
    app: cicd-demo
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: LoadBalancer
```

This is secret.
> docker-registry is secret type not name.`regcred` is secret name.

```bash
kubectl create secret docker-registry regcred \
    --docker-server=registry.khaolakonline.com \
    --docker-username=root \
    --docker-password=GfgTSQVPFCD7nKOrkg5ygTzymgdCeePUt3KRwZpWjDQEUYAcGAwMHdWMDHyAxT1U \
    --docker-email=admin@example.com
```

```bash
```

## 

```bash
vi /etc/docker/daemon.json
```

In `daemon.json`

```bash
{
  "insecure-registries" : ["registry.khaolakonline.com"]
}
```

## Kaniko

```bash
docker run \
    -v /root/kaniko:/workspace \
    -v /root/.docker/config.json:/kaniko/.docker/config.json \
    gcr.io/kaniko-project/executor:latest \
    --dockerfile=/workspace/Dockerfile \
    --destination=nutlee22/cicd-demo:latest
```

![alt text](image.png)

```yml
        volumeMounts:
        - mountPath: /etc/docker/registry/
          name: registry-server-config
          readOnly: true
        - mountPath: /etc/ssl/certs/
          name: etc-ssl-certs
          readOnly: true
        - mountPath: /etc/pki/ca-trust/extracted/pem
          name: etc-pki-ca-trust-extracted-pem
          readOnly: true
```

## Create custom cert

```
openssl s_client -showcerts -connect gitlab.example.com:443 -servername gitlab.example.com < /dev/null 2>/dev/null | openssl x509 -outform PEM > /etc/gitlab-runner/certs/gitlab.example.com.crt


openssl genpkey -algorithm RSA -out khaolakonline.key -aes256

openssl req -new -key khaolakonline.key -out khaolakonline.csr

openssl x509 -req -in wildcard.khaolakonline.com.csr -signkey wildcard.khaolakonline.com.key -out wildcard.khaolakonline.com.crt -days 365 -extfile wildcard.cnf -extensions req_ext

kubectl create secret tls gitlab-tls-secret -n gitlab     --key khaolakonline.key.unencrypted     --cert khaolakonline.crt
```