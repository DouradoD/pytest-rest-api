pipeline {
    agent any // Runs on any available agent
    environment {
        DOCKER_IMAGE = "pytest-restapi" // Name of the Docker image
    }
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    docker.build("${env.DOCKER_IMAGE}")
                }
            }
        }
        stage('Debug') {
                steps {
                    script {
                        // Check Docker version
                        sh 'docker --version'

                        // List Docker images
                        sh 'docker images'

                        // Check Jenkins workspace
                        sh 'pwd'
                        sh 'ls -la'
                    }
                }
            }
        stage('Run Tests') {
            steps {
                script {
                    // Run the Docker container and execute tests
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