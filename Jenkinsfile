pipeline {
    agent {
        label('python')
    }
    environment {
        PYPI_CREDENTIALS = credentials('pypi-credentials')
        DO_COVERAGE = "${BUILD_NUMBER.toInteger() % 2 == 0 ? 'true' : 'false'}"
    }
    //triggers {
    //    cron('*/2 * * * *')
    //}
    options { 
        disableConcurrentBuilds()
        ansiColor('xterm')
        timeout(time: 5, unit: 'MINUTES')
        timestamps()
    }
    stages {
        stage('Build') {
            steps {
                dir('python-example-app') {
                    sh 'pip install -r requirements.txt'
                    echo "${DO_COVERAGE}"
                }
            }
        }
        stage('Unit Test') {
            steps {
                dir('python-example-app') {
                    sh 'python -m coverage run -m pytest -s -v'
                }
            }
        }
        stage('Coverage') {
            when {
                allOf {
                    expression {
                        environment name: 'DO_COVERAGE', value: == 'true'
                    }
                    branch 'master'
                }
            }
            steps {
                dir('python-example-app') {
                    sh 'python -m coverage report -m --fail-under=90'
                }
            }
        }
        stage('Package') {
            steps {
                dir('python-example-app') {
                    sh 'python -m build'
                }
            }
        }
        stage('Publish') {
            /*
            input {
              message "Do you want to continue: "
              ok "Yes, continue the pipeline"
            }*/
            when {
                branch 'master'
            }
            steps {
                dir('python-example-app') {
                    sh 'python -m twine upload dist/* --skip-existing -u $PYPI_CREDENTIALS_USR -p $PYPI_CREDENTIALS_PSW'
                    //sh 'python -m twine upload dist/* --skip-existing --config-file ~/.pypirc'
                }
            }
        }
    }
    post {
        failure {
            echo "Your pipeline has failed, contact with your administrator"
        }
        success {
            echo "The deployment was done successfully"
        }
        always {
            echo "I hope you like Jenkins"
        }
    }
}
