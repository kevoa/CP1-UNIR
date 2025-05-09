pipeline{
    agent {
        label 'agent1'
    }
    stages {
        stage('1. Descargar repositorio.') {
            steps {
                echo 'Descargando repositorio '
                checkout scm
                sh 'echo "ls -la"'
            }
        }
        stage('2. Etapa Unit prueba unitaria...') {
            steps {
                echo 'Lanzando pruebas unitarias...'
                sh 'python3 -m pytest test/unit --junitxml=reports/TEST-unit-sequential.xml'
                echo 'Pruebas unitarias realizadas con exito.'
            }
        }
        stage('3. Etapa service...') {
            steps {
                echo 'Etapa service...'
                sh 'python3 -m pytest test/rest junitxml=TEST-rest-sequential.xml'
                echo 'Pruebas de servicio realizadas con exito'
            }
        }
        stage('4. Ejecución en paralelo.') {
            parallel {
                stage('4.1 Pruebas unitarias') {
                    steps {
                        sh 'python3 -m pytest test/unit --junitxml=reports/TEST-unit-parallel.xml'
                    }

                }
                stage('4.2 Pruebas de servicio') {
                    steps {
                        sh 'python3 -m pytest test/rest --junitxml=reports/TEST-unit-parallel.xml'
                    }
                }
            }
        }
    }
    post {
        always {
            echo 'Fin del Pipeline'
        }
        failure {
            echo 'El pipeline falló'
        }
    }
}