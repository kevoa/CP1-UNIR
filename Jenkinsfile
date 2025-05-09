pipeline{
    agent any 
    stages {
        stage('1. Crear y ejecutar un pipeline simple, una sola etapa con un “echo”') {
            steps {
                echo 'Empecemos con la práctica 1!'
            }
        }
        stage('2. Añadir un comando git para traer todo el código fuente del repositorio') {
            steps {
                echo 'Pulling repositorio...'
                git url: 'https://github.com/kevoa/CP1-UNIR', branch: 'master'
            }
        }
        stage('3. Verificar que el código se ha descargado mediante comando dir (o ls –la)') {
            steps {
                echo 'Verificando la descarga del repositorio...'
                sh 'ls -la'
                echo 'Verificación realizada'
            }
        }
        stage('4. Verificar cuál es el espacio de trabajo (echo %WORKSPACE% o echo $WORKSPACE)') {
            steps {
                echo 'Verificando cual es mi espacio de trabajo...'
                sh 'echo "$WORKSPACE"'
            }
        }
        stage('5. Añadir etapa “Build” (que no hace nada realmente)') {
            steps {
                echo 'Etapa Build...'
                echo 'Esta etapa es para fines didácticos.'
            }
        }
    }

    post {
        always {
            echo 'Fin del Pipeline CI de jenkins para el caso practico 1 - Jenkins 1.'
        }
    }
}