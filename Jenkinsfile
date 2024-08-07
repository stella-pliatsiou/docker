pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-python-app:latest'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/stella-pliatsiou/docker.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Κατασκευή του Docker image
                    bat 'docker build -t my-python-app:latest .'
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    // Εκτέλεση των δοκιμών εντός του Docker container
                    bat 'docker run --rm my-python-app:latest pytest'
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    // Εντολές ανάπτυξης μπορούν να προστεθούν εδώ
                    bat 'docker run -d --name my-python-app -p 8000:8000 my-python-app:latest'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
