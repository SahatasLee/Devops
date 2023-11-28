# Config File

/.kube/config

## Install kubectl

https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

1. Download

```bash
curl -LO https://dl.k8s.io/release/v1.28.2/bin/linux/amd64/kubectl
```

2. Validate

```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
```

3. Install

```bash
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

4. Test

```bash
kubectl version --client
kubectl version --client --output=yaml
```

## Uninstall

1. Remove kubectl

```bash
sudo rm -f /usr/local/bin/kubectl
```

2. Remove file

```bash
rm -rf ~/.kube/
```

```bash
sudo rm -f /usr/local/bin/kubectl
rm -rf ~/.kube/
```