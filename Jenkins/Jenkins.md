# Jenkins101

Tools chain gitlab, nexus

Ref. https://www.jittagornp.me/blog/jenkins-pipeline/ 

# Jenkinsfile

Script

```
pipeline {
    agent any
    tools {nodejs "node"}
    stages {
        stage('Git') {
            steps {
                echo 'git clone'
                git branch: 'master', credentialsId: '101', url: 'https://git.matador.ais.co.th/devops/demo-nut.git'
            }
        }
        stage('npm -i') {
            steps {
                echo 'npm install'
                sh 'npm install --verbose'
            }
        }
        stage('npm build') {
            steps {
                echo 'npm build'
                sh 'npm run build'
            }
        }
        stage('zip') {
            steps {
                script{
                    zip dir: './build', exclude: '', glob: '', zipFile: 'built'
                }
            }
        }
        stage('publish'){
            steps {
                nexusPublisher nexusInstanceId: 'devops-releases', 
                nexusRepositoryId: 'devops-releases', 
                packages: [[$class: 'MavenPackage', mavenAssetList: [[classifier: '', extension: '', filePath: './built']], 
                mavenCoordinate: [artifactId: 'frontend', groupId: 'devops.frontend', packaging: 'zip', version: '1.0.0-20220613']]]
            }
        }
        stage('clean'){
            steps {
                cleanWs()
            }
        }
    }
}
```

Jenkins multibranch pipeline

Webhook : https://docs.gitlab.com/ee/user/project/integrations/webhooks.html#events
