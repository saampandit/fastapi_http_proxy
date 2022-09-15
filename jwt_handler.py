import jwt
import secrets
from datetime import datetime, timezone


def generate_jwt_token(username):
    """
    This function generates the jwt_token for the 
    particular username
    """

    secret = "a9ddbcaba8c0ac1a0a812dc0c2f08514b23f2db0a68343cb8199ebb38a6d91e4ebfb378e22ad39c2d01 d0b4ec9c34aa91056862ddace3fbbd6852ee60c36acbf"
    today = datetime.today()

    payload = {"user": username,
               "date": today.strftime("%b-%d-%Y"),
               "iat": datetime.now(tz=timezone.utc),
               "jti": secrets.token_urlsafe()
                }
    token = jwt.encode(payload, secret, algorithm="HS512")
    print(f"Token is {token}")
    return token
