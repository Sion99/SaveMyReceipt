from app.models import *
import os
from dotenv import load_dotenv
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
import requests
import jwt

# ENV VALUES
load_dotenv()
GOOGLE_AUTH_URL = os.getenv("GOOGLE_AUTH_URL")
GOOGLE_TOKEN_URL = os.getenv("GOOGLE_TOKEN_URL")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
JWT_SECRET = os.getenv("JWT_SECRET")


def login():
    auth_url = f"{GOOGLE_AUTH_URL}?client_id={GOOGLE_CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope="

async def get_access_token(auth_request: AuthRequest):
    auth_code = auth_request.code
    token_url = GOOGLE_TOKEN_URL

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    token_payload = {
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "code": auth_code,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI
    }

    response = requests.request(
        "POST",
        token_url,
        headers=headers,
        data=token_payload
    )

    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="토큰 발급에 실패했습니다.")
    response_json = response.json()
    access_token = response_json.get('access_token')

    return access_token


def generate_jwt_token(user_info: dict):
    payload = {
        "username": user_info["username"],
        "email": user_info["email"]
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return token
