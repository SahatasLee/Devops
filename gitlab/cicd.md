# CI/CD

```yaml
stages: 
  - deploy

variables:
  TARGET_DIR: "/home/sahatas/kafka-cicd"

deploy:
  stage: deploy
  before_script: 
    - chmod 400 $SSH_KEY
  script:
    - ssh -o StrictHostKeyChecking=no -i $SSH_KEY root@10.1.1.1 "
        git clone http://$GITLAB_USERNAME:$GITLAB_TOKEN@10.111.0.116:8080/root/kafka-cicd.git $TARGET_DIR &&
        cd $TARGET_DIR &&
        kubectl -n kafka apply -f KAFKATOPIC-01.yaml &&
        rm -rf $TARGET_DIR
        "

# git clone https://<username>:<personal_token>@gitlab.com/gitlab-org/gitlab.git
# git clone http://root:glpat-PypyuapSns3dy52FXQyY@10.111.0.116:8080/root/kafka-cicd.git /home/sahatas/kafka-cicd
# git clone https://[TOKEN]@github.com/[REPO-OWNER]/[REPO-NAME]
# git remote add origin https://[TOKEN]@github.com/[REPO-OWNER]/[REPO-NAME]
# git remote add origin http://glpat-qCZTtcghUNRzWsAPZxoX@10.111.0.116:8080/root/kafka-cicd.git
# git remote add origin http://root:glpat-PypyuapSns3dy52FXQyY@10.111.0.116:8080/root/kafka-cicd.git
# git clone http://glpat-qCZTtcghUNRzWsAPZxoX@10.111.0.116:8080/root/kafka-cicd.git
# glpat-PypyuapSns3dy52FXQyY
```