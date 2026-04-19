pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "roronoazoro1350/frontend"
        TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/dharanesh-vn/devops-lab.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:$TAG .'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('My Sonar Server') {
                    sh 'sonar-scanner'
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $DOCKER_IMAGE:$TAG'
            }
        }

        stage('Update GitOps Repo') {
            steps {
                sh '''
                sed -i "s|image:.*|image: $DOCKER_IMAGE:$TAG|g" k8s/frontend-deployment.yaml
                git config user.name "jenkins"
                git config user.email "jenkins@example.com"
                git add .
                git commit -m "Updated image to $TAG"
                git push origin main
                '''
            }
        }
    }
}

