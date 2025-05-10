pipeline {
    agent {
        label 'agent1'
    }
    stages {
        stage('1. Descargar repositorio y crear reports.') {
            steps {
                echo 'Descargando repostorio...'
                // checkout scm
                git url: 'https://github.com/kevoa/CP1-UNIR', branch: 'master'
                sh 'ls -la'
                echo 'Creando directorio de reportes...'
                sh 'mkdir -p reports'
            }
        }
        stage('2. Pruebas unitarias (Secuencial).') {
            steps {
                echo 'Realizando pruebas unitarias...'
                sh 'python3 -m pytest test/unit --junitxml=reports/TEST-unit-sequential.xml'
                echo 'Pruebas unitarias (secuenciales) realizadas con éxito'
            }
        }
        stage('3. Pruebas de servicio (Secuencial con aislamiento).') {
            steps {
                script {
                    echo 'Iniciando pruebas de servicio secuencial...'
                    try {
                        echo 'Limpiando entorno en caso de ser necesario...'
                        sh 'docker compose -f docker-compose.yml down --volumes --remove-orphans || true'

                        echo 'Construyendo entorno para pruebas python-app y wiremock...'
                        sh 'docker compose -f docker-compose.yml up -d --build python-app wiremock_service'

                        echo 'Esperando a que los servicios se inicien...'
                        sh 'sleep 20'

                        echo 'Creando directorio para reportes en el workspace...'
                        sh 'mkdir -p reports'

                        echo 'Ejecutando pruebas de servicio (Secuencial)...'
                        sh 'python3 -m pytest test/rest --junitxml=reports/TEST-rest-sequential.xml'
                        echo 'Pruebas de servicio secuencial ejecutadas con éxito.'
                    } catch (e) {
                        echo 'Error en pruebas de servicio secuencial'
                        currentBuild.result = 'FAILURE'
                    } finally {
                        echo 'Deteniendo y eliminando contenedores de prueba (service secuencial) para un workspace limpio...'
                        sh 'docker compose -f docker-compose.yml down --volumes --remove-orphans|| true'
                    }
                }
            }
        }
        stage('4. Pruebas en paralelo (Con aislamiento)') {
            parallel {
                stage('4.1 Pruebas unitarias (Paralelo)') {
                    steps {
                        echo 'Creando directorio para reportes en el workspace...'
                        sh 'mkdir -p reports'

                        echo 'Realizando pruebas unitarias en paralelo...'
                        sh 'python3 -m pytest test --junitxml=reports/TEST-unit-parallel.xml'
                        
                        echo 'Pruebas unitarias realizadas con exito...'
                    }
                }
                stage('4.2 Pruebas de servicio (Paralelo con aislamiento)') {
                    steps {
                        script {
                        echo 'Iniciando pruebas de servicio en paralelo'
                            try {
                                echo 'Limpiando entorno en caso de ser necesario...'
                                sh 'docker compose -f docker-compose.yml down --volumes --remove-orphans || true'


                                echo 'Construyendo entorno para pruebas python-app y wiremock...'
                                sh 'docker compose -f docker-compose.yml up -d --build python-app wiremock_service'

                                echo 'Esperando a que los servicios se inicien'
                                sh 'sleep 20'

                                echo 'Creando directorio para reportes en el workspace...'
                                sh 'mkdir -p reports'

                                echo 'Ejecutando pruebas de servicio (Parallel)...'
                                sh 'python3 -m pytest test/rest --junitxml=reports/TEST-rest-parallel.xml'
                                echo 'Pruebas de servicio en paralelo ejecutadas con éxito.'
                            } catch (e) {
                                currentBuild.result = 'FAILURE'
                            } finally {
                                echo 'Deteniendo y eliminando contenedores de prueba (service parallel) para un workspace limpio...'
                                sh 'docker compose -f docker-compose.yml down --volumes --remove-orphans|| true'
                            }
                        }
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
            echo 'El pipeline falló.'
        }
    }
}
