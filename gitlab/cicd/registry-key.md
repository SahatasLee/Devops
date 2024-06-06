# Registry Key

```bash
kubectl create secret docker-registry gitlab-registry-key \
--docker-server=registry.khaolakonline.com \
--docker-username=root \
--docker-password=cm9vdDpnbHBhdC02VTJBenhuYW0zcFA5N2JEZGhkTQ==

# Create a new secret named my-secret from ~/.docker/config.json
kubectl create secret docker-registry gitlab-registry-key --from-file=.dockerconfigjson=/root/.docker/config.json
```