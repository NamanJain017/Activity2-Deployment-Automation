
pipeline {
    agent any

    options {
        timestamps()
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Tools') {
            steps {
                bat '''
                    echo Checking Python
                    where python
                    python --version

                    echo Checking Docker
                    where docker
                    docker --version

                    echo Checking Kubernetes
                    where kubectl
                    kubectl version --client
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements-dev.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t shopease:ci-%BUILD_NUMBER% .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat '''
                    kubectl config current-context

                    kubectl set image deployment/shopease shopease=shopease:ci-%BUILD_NUMBER%

                    if errorlevel 1 exit /b 1

                    kubectl set env deployment/shopease APP_VERSION=ci-%BUILD_NUMBER%

                    if errorlevel 1 exit /b 1

                    kubectl rollout status deployment/shopease --timeout=120s
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                bat '''
                    kubectl get deployment shopease
                    kubectl get pods -l app=shopease
                    kubectl get service shopease
                '''
            }
        }
    }

    post {
        success {
            echo 'ShopEase CI/CD pipeline completed successfully.'
        }

        failure {
            echo 'Pipeline failed. Check the failed stage before deployment.'
        }
    }
}
