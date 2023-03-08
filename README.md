# Инструкция по развертыванию

Запуск производился на macOS - M1 pro

Предварительно должен быть установлен `minikube` - `brew install minikube` и `kubectl` - `brew install kubectl` ([тык](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/))

### Деплой postgres
Предварительно нужно установить `helm` - `brew install helm` (на mac os)
Далее добавляем репозиторий `postgres` и разворачиваем базу данных
- `helm repo add my-repo https://charts.bitnami.com/bitnami`
- `helm install demo-database my-repo/postgresql --set global.postgresql.auth.username=demo --set global.postgresql.auth.password=demo --set global.postgresql.auth.database=demo`


### Деплой бэкенда

Запускаем

- `kubectl apply -f backend-deployment.yaml`
- `kubectl apply -f backend-service.yaml`

### Экспозим бекенд
- `minikube service backend`

Откроется страница в браузере. Копируем url

### Деплой фронтенда

Предварительно меняем значение поля `REACT_APP_BACKEND_API` в файле `frontend-deployment.yaml` на скопированный на предыдущем шаге url + api/v1 (Должно получится так - **http://{host:port}/api/v1**)

Запускаем

- `kubectl apply -f frontend-deployment.yaml`
- `kubectl apply -f frontend-service.yaml`

### Экспозим фронтенд
- `minikube service frontend`

P.S. Может понадобится обновить страницу несколько раз

Демо видео - `demo.mov`
