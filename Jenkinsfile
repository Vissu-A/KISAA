pipeline {
    
    agent{
        label 'python'
    }
        
    stages {

        stage('Code Checkout'){
            steps{
                git branch: 'prod', changelog: true, credentialsId: 'git_ssh', poll: false, url: 'git@github.com:VisualizeAI/KISAA.git'
            }

        }
        
        
        stage('Hello') {
            steps {
                echo 'Hello World!'
            }
        }
        
    }
    
}
