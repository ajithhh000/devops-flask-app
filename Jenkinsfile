pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t flask-app:${BUILD_NUMBER} .'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Running tests... (mock)"'
                // Add real tests later (pytest, etc.)
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                    docker stop flask-app-prod 2>/dev/null || true
                    docker rm flask-app-prod 2>/dev/null || true
                    docker run -d --name flask-app-prod -p 5000:5000 flask-app:${BUILD_NUMBER}
                '''
            }
        }
    }
}
