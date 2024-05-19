# HELM

## List

1. list repo
```bash
helm repo list
```

2. list chart

```bash
helm list
```

3. list all chart

```bash
helm search repo 
```

4. list all version

```bash
helm search repo <reponame>/<chartname> --versions

# list all available versions of a gitlab chart
helm search repo gitlab/gitlab-runner --versions
```
