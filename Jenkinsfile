pipeline {
    agent {
        label 'agent1' 
    }
    stages {
        stage('1. Descargar repositorio.') {
            steps {
                echo 'Descargando repositorio '
                sh 'ls -la' 
                sh 'mkdir -p reports' 
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
                sh 'python3 -m pytest test/rest --junitxml=reports/TEST-rest-sequential.xml'
                echo 'Pruebas de servicio realizadas con exito'
            }
        }
        stage('4. Ejecución en paralelo.') {
            parallel {
                stage('4.1 Pruebas unitarias') {
                    steps {
                        sh 'mkdir -p reports' 
                        sh 'python3 -m pytest test/unit --junitxml=reports/TEST-unit-parallel.xml'

                    }
                }
                stage('4.2 Pruebas de servicio') {
                    steps {
                        sh 'mkdir -p reports' 
                        sh 'python3 -m pytest test/rest --junitxml=reports/TEST-rest-parallel.xml'
                    }
                }
            }
        }
    }
    post {
        always {
            echo 'Fin del Pipeline'
            archiveArtifacts artifacts: 'reports/*.xml', allowEmptyArchive: true
        }
        failure {
            echo 'El pipeline falló'
        }

    }
}
