pipeline {
    agent any
    
    parameters {
        choice(
            name: 'ENV',
            choices: ['dev', 'prod'],
            description: 'Окружение для деплоя'
        )
    }

    stages {
        stage('Prepare') {
            steps {
                echo "Deploying to ${params.ENV}"
                cleanWs()
            }
        }
        
        stage('Deploy') {
            steps {
                sshPublisher(
                    publishers: [
                        sshPublisherDesc(
                            configName: 'server1',
                            transfers: [
                                sshTransfer(
                                    sourceFiles: '**/*',
                                    remoteDirectory: "/var/www/${params.ENV}",
                                    execCommand: "sudo systemctl restart ${params.ENV}-app"
                                )
                            ]
                        )
                    ]
                )
            }
        }
    }
}
