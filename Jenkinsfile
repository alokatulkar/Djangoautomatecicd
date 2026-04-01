pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "alok2804/django-app"
        SONARQUBE_ENV = "SonarQube"   // Name configured in Jenkins
    }

    tools {
        sonarScanner 'SonarScanner'   // Name from Global Tool Config
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/alokatulkar/Djangoautomatecicd.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("${SONARQUBE_ENV}") {
                    sh '''
                    sonar-scanner \
                    -Dsonar.projectKey=django-app \
                    -Dsonar.projectName=django-app \
                    -Dsonar.sources=. \
                    -Dsonar.language=py \
                    -Dsonar.python.version=3
                    '''
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

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Migrations') {
            steps {
                sh '''
                . venv/bin/activate
                python manage.py migrate
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                python manage.py test
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:latest .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    sh '''
                    echo "$PASS" | docker login -u "$USER" --password-stdin
                    docker push ${DOCKER_IMAGE}:latest
                    docker logout
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }
}
