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
                sh 'python3 -m pytest test/unit'
                echo 'Pruebas unitarias realizadas con exito.'
            }
        }
        stage('3. Etapa service...') {
            steps {
                echo 'Etapa service...'
                sh 'python3 -m pytest test/rest'
                echo 'Pruebas de servicio realizadas con exito'
            }
        }
        stage('4. Ejecución en paralelo.') {
            parallel {
                stage('4.1 Pruebas unitarias') {
                    steps {
                        sh 'python3 -m pytest test/unit'
                    }
                    post {
                        always {
                            junit "**/TEST-*.xml"
                        }
                    }
                }
                stage('4.2 Pruebas de servicio') {
                    steps {
                        sh 'python3 -m pytest test/rest'
                    }
                    post {
                        always {
                            junit "**/TEST-*.xml"
                        }
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