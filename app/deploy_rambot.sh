
kubectl create namespace rambot

kubectl create -f database/mysql-secret.yaml -n rambot
kubectl create -f database/mysql-storage.yaml -n rambot

kubectl create -f rambot-deployment.yaml --namespace rambot
kubectl create -f rambot-service.yaml --namespace rambot
