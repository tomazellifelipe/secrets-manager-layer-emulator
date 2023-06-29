"""
This simple app can be used to emulate AWS Secrets Manager Layer for AWS Lambdas.

"""
import json

from dotenv import dotenv_values
from fastapi import FastAPI, Header
from typing import Any
app = FastAPI()


def dotenv_to_dict() -> dict[str, Any]:
    """Responsible for loading a .env file into a dictionary"""
    return dotenv_values("./config/.env")


@app.get("/secretsmanager/get")
def get_secret(
    secretId: str,
    secrets_token: str = Header(None, alias="X-Aws-Parameters-Secrets-Token"),
) -> dict[str, Any]:
    """
    Get route for access to local Secrets Manager.

    Parameters
    ----------
    secretId : str
    secrets_token : str
        Header:
            Alias : X-Aws-Parameters-Secrets-Token.
    
    Returns
    -------
    secretString: dict[str, Any]
        Return a json with a jsonstring body.

    Examples
    --------
    >>> secrets=$(curl localhost:2773/secretsmanager/get?secretId=my-secret -H '{"X-Aws-Parameters-Secrets-Token": ""}') 
    >>> secrets
    '{"SecretString": "{\"user\":\"admin\",\"password\":\"EXAMPLE\"}"}'
    """

    secrets = dotenv_to_dict()
    return {"SecretString": json.dumps(secrets)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=2773)
