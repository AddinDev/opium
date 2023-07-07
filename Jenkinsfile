pipeline {
  agent any
  
  stages {
    stage('Build') {
      steps {
        script {
          docker build -t opium .
        }
      }
    }

    stage('Deploy') {
      steps {
          echo 'deploying the application'
      }
    }
    
  }
}
