# secrets-manager-layer-emulator

Emulates aws secrets manager layer for local run using .env as secrets variables for aws lambda testing

```sh
docker image build -t secrets-manager-layer-emulator:latest
docker container run -d -p 2773:2773 -v ./.env:/app/config/.env --name secrets-layer secrets-manager-layer-emulator:latest
```
