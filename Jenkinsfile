pipeline {
    agent {
        label 'agent1'
    }
    stages {
        stage('1. Descargar repositorio.') {
            steps {
                echo 'Descargando repositorio '
                // El checkout scm aquí es redundante si ya lo tienes al inicio del pipeline declarativo.
                // Si este es el único checkout que quieres, elimina el global.
                // checkout scm 
                sh 'ls -la' // Para ejecutar ls -la, no 'echo "ls -la"'
                sh 'mkdir -p reports' // Buena práctica: crear el directorio de informes
            }
        }
        stage('2. Etapa Unit prueba unitaria...') {
            steps {
                echo 'Lanzando pruebas unitarias...'
                sh 'python3 -m pytest test/unit --junitxml=reports/TEST-unit-sequential.xml' // <--- AÑADIR ESTO
                junit 'reports/TEST-unit-sequential.xml'
                echo 'Pruebas unitarias realizadas con exito.'
            }
        }
        stage('3. Etapa service...') {
            steps {
                echo 'Etapa service...'
                sh 'python3 -m pytest test/rest --junitxml=reports/TEST-rest-sequential.xml' // <--- AÑADIR ESTO
                junit 'reports/TEST-rest-sequential.xml'
                echo 'Pruebas de servicio realizadas con exito'
            }
        }
        stage('4. Ejecución en paralelo.') {
            parallel {
                stage('4.1 Pruebas unitarias') {
                    agent any // Si las etapas paralelas necesitan un workspace distinto o agente
                    steps {
                        sh 'mkdir -p reports' // También aquí si el workspace es diferente
                        sh 'python3 -m pytest test/unit --junitxml=reports/TEST-unit-parallel.xml' // <--- AÑADIR ESTO
                        junit 'reports/TEST-unit-parallel.xml'
                    }
                }
                stage('4.2 Pruebas de servicio') {
                    agent any // Si las etapas paralelas necesitan un workspace distinto o agente
                    steps {
                        sh 'mkdir -p reports' // También aquí si el workspace es diferente
                        sh 'python3 -m pytest test/rest --junitxml=reports/TEST-rest-parallel.xml' // <--- AÑADIR ESTO
                        junit 'reports/TEST-rest-parallel.xml'
                    }
                }
            }
        }
    }
    post {
        always {
            echo 'Fin del Pipeline'
            // Es útil archivar los reportes para verlos manualmente si es necesario
            archiveArtifacts artifacts: 'reports/*.xml', allowEmptyArchive: true
        }
        failure {
            echo 'El pipeline falló'
        }
    }
}