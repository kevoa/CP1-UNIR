pipeline {
    agent {
        label 'agent1' // Define el agente por defecto para todo el pipeline
    }
    stages {
        stage('1. Descargar repositorio.') {
            steps {
                echo 'Descargando repositorio '
                sh 'ls -la' 
                sh 'mkdir -p reports' // Crea el directorio de reportes si no existe
            }
        }
        stage('2. Etapa Unit prueba unitaria...') {
            steps {
                echo 'Lanzando pruebas unitarias...'
                // Ejecuta pruebas unitarias y genera un reporte JUnit XML
                sh 'python3 -m pytest test/unit --junitxml=reports/TEST-unit-sequential.xml'
                // La publicación de resultados JUnit se puede habilitar descomentando la siguiente línea
                // junit 'reports/TEST-unit-sequential.xml' 
                echo 'Pruebas unitarias realizadas con exito.'
            }
        }
        stage('3. Etapa service...') {
            steps {
                echo 'Etapa service...'
                // Ejecuta pruebas de servicio y genera un reporte JUnit XML
                sh 'python3 -m pytest test/rest --junitxml=reports/TEST-rest-sequential.xml'
                // La publicación de resultados JUnit se puede habilitar descomentando la siguiente línea
                // junit 'reports/TEST-rest-sequential.xml'
                echo 'Pruebas de servicio realizadas con exito'
            }
        }
        stage('4. Ejecución en paralelo.') {
            parallel {
                stage('4.1 Pruebas unitarias') {
                    agent {
                        label 'agent1'
                    }
                    steps {
                        sh 'mkdir -p reports' // Asegura que el directorio exista en el workspace del agente
                        // Ejecuta pruebas unitarias en paralelo y genera un reporte JUnit XML
                        sh 'python3 -m pytest test/unit --junitxml=reports/TEST-unit-parallel.xml'
                        // Publica los resultados de las pruebas JUnit
                        // junit 'reports/TEST-unit-parallel.xml' 
                    }
                }
                stage('4.2 Pruebas de servicio') {
                    agent {
                        label 'agent1'
                    }
                    steps {
                        sh 'mkdir -p reports' // Asegura que el directorio exista en el workspace del agente
                        // Ejecuta pruebas de servicio en paralelo y genera un reporte JUnit XML
                        sh 'python3 -m pytest test/rest --junitxml=reports/TEST-rest-parallel.xml'
                        // Publica los resultados de las pruebas JUnit
                        // junit 'reports/TEST-rest-parallel.xml'
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
            // Se ejecuta solo si el pipeline falla
            echo 'El pipeline falló'
            // Aquí se podrían añadir notificaciones o pasos de limpieza específicos para fallos.
        }

    }
}
