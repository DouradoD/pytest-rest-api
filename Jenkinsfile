pipeline {
    agent none // No global agent; define agents at the stage level
    stages {
        stage('Example') {
            agent any // Runs on any available agent
            steps {
                echo 'Running on any agent'
            }
        }
    }
}