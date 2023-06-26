import json

from dotenv import dotenv_values
from fastapi import FastAPI, Header

app = FastAPI()


def dotenv_to_dict():
    return dotenv_values("./config/.env")


@app.get("/secretsmanager/get")
def get_secret(
    secretId: str,
    secrets_token: str = Header(None, alias="X-Aws-Parameters-Secrets-Token"),
):
    secrets = dotenv_to_dict()
    return {"SecretString": json.dumps(secrets)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=2773)
