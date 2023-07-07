pipeline {
  agent any
  
  stages {
    stage('Build') {
      steps {
          docker build -t opium .
      }
    }

    stage('Deploy') {
      steps {
          echo 'deploying the application'
      }
    }
    
  }
}
