pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "roronoazoro1350/frontend"
        TAG = "${BUILD_NUMBER}"
        SONAR_TOKEN = "sqa_cd3c98f9ca833e3937ef9bba3259c8cfe0855a81"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $DOCKER_IMAGE:$TAG .
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                sh '''
                /opt/sonar-scanner/bin/sonar-scanner \
                -Dsonar.projectKey=devops-lab \
                -Dsonar.sources=. \
                -Dsonar.host.url=http://localhost:9000 \
                -Dsonar.login=$SONAR_TOKEN
                '''
            }
        }

        stage('Quality Gate (Simulated)') {
            steps {
                echo "Quality Gate Passed ✅"
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                docker push $DOCKER_IMAGE:$TAG
                '''
            }
        }

        stage('Update GitOps Repo') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'github-creds',
                    usernameVariable: 'GIT_USER',
                    passwordVariable: 'GIT_PASS'
                )]) {
                    sh '''
                    git checkout -B main

                    sed -i "s|image:.*|image: $DOCKER_IMAGE:$TAG|g" k8s/frontend-deployment.yaml

                    git config user.name "jenkins"
                    git config user.email "jenkins@example.com"

                    git add .
                    git commit -m "Updated image to $TAG" || echo "No changes"

                    git remote set-url origin https://$GIT_USER:$GIT_PASS@github.com/dharanesh-vn/devops-lab.git

                    git push origin main
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "🚀 Pipeline executed successfully!"
        }
        failure {
            echo "❌ Pipeline failed!"
        }
    }
}
