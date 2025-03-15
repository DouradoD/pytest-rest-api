pipeline {
    agent any
    environment {
        PYTHON_VERSION = '3.8.12'
    }
    stages {
        stage('Set up Python Environment') {
            steps {
                script {
                    def isWindows = isUnix() ? false : true
                    if (isWindows) {
                        // Windows-specific setup
                        bat """
                        choco install pyenv-win -y
                        pyenv install ${env.PYTHON_VERSION} --force
                        pyenv local ${env.PYTHON_VERSION}
                        python -m venv venv
                        venv\\Scripts\\pip install -r requirements.txt
                        """
                    } else {
                        // Linux-specific setup
                        sh '''
                        curl https://pyenv.run | bash
                        export PYENV_ROOT="$HOME/.pyenv"
                        export PATH="$PYENV_ROOT/bin:$PATH"
                        eval "$(pyenv init -)"
                        pyenv install ${env.PYTHON_VERSION} --force
                        pyenv local ${env.PYTHON_VERSION}
                        python -m venv venv
                        venv/bin/pip install -r requirements.txt
                        '''
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    def isWindows = isUnix() ? false : true
                    if (isWindows) {
                        bat 'venv\\Scripts\\pytest'
                    } else {
                        sh 'venv/bin/pytest'
                    }
                }
            }
        }
    }
    post {
        always {
            script {
                def isWindows = isUnix() ? false : true
                if (isWindows) {
                    bat 'rmdir /s /q venv'
                } else {
                    sh 'rm -rf venv'
                }
            }
        }
    }
}