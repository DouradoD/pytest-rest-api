pipeline {
    agent { dockerfile true }
    environment {
        DOCKER_IMAGE = "pytest-restapi"
    }
    stages {
        stage('Build Project Image') {
            steps {
                script {
                    // Build the project Docker image
                    docker.build("${env.DOCKER_IMAGE}")
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Run the project Docker container and execute tests
                    docker.image("${env.DOCKER_IMAGE}").inside {
                        // Run pytest inside the container
                        sh 'pytest -s -v --log-level=info --tb=auto --html=reports/report.html --self-contained-html'
                    }
                }
            }
        }
        stage('Archive Test Results') {
            steps {
                // Archive the test report
                archiveArtifacts artifacts: 'reports/report.html', allowEmptyArchive: true
            }
        }
    }
    post {
        always {
            // Clean up Docker images
            script {
                sh "docker rmi ${env.DOCKER_IMAGE} || true"
            }
        }
    }
}