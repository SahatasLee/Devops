# Gitlab

https://docs.gitlab.com/ee/install/docker.html

## Install Gitlab by docker 

```bash
sudo docker run --detach \
  --hostname 10.111.0.116 \
  --publish 443:443 --publish 80:80 --publish 2222:22 \
  --name gitlab \
  --restart always \
  --volume $GITLAB_HOME/gitlab/config:/etc/gitlab \
  --volume $GITLAB_HOME/gitlab/logs:/var/log/gitlab \
  --volume $GITLAB_HOME/gitlab/data:/var/opt/gitlab \
  gitlab/gitlab-ce:latest
```

## Install Gitlab by docker compose

`docker-compose.yml`
```docker
version: '3.6'
services:
  web:
    image: 'gitlab/gitlab-ee:latest'
    restart: always
    hostname: '10.111.0.116'
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'http://10.111.0.116'
        # Add any other gitlab.rb configuration here, each on its own line
    ports:
      - '80:80'
      - '443:443'
      - '22:22'
    volumes:
      - '$GITLAB_HOME/config:/etc/gitlab'
      - '$GITLAB_HOME/logs:/var/log/gitlab'
      - '$GITLAB_HOME/data:/var/opt/gitlab'
    shm_size: '256m'
```

Get root password:

```bash
sudo docker exec -it gitlab grep 'Password:' /etc/gitlab/initial_root_password
```

## URL

```url
http://10.111.0.116:80
```

## Gitlab runner

```bash
docker run -d --name gitlab-runner --restart always \
  -v /srv/gitlab-runner/config:/etc/gitlab-runner \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --dns=10.111.0.112 \
  gitlab/gitlab-runner:latest
```

register Gitlab runner:

```bash
docker exec -it gitlab-runner gitlab-runner register
```

url: `http://10.111.0.117:8080`

token: project > setting > cicd > runners > project runners

descriptions: runner

executor: docker

images: ruby:2.7