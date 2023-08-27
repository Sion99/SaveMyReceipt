from fastapi import APIRouter
from app.models import *
import auth_service
from dotenv import load_dotenv
import requests
import os

auth_router = APIRouter(prefix='/auth')

load_dotenv()


@auth_router.get('/')
async def login():
    auth_service.login()


@auth_router.post('/', status_code=201)
async def get_access_token(auth_request: AuthRequest):
    access_token = auth_service.get_access_token(auth_request)
