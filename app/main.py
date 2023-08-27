from fastapi import FastAPI
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from auth.auth_router import auth_router
from ocr.ocr_router import ocr_router

# ENV
load_dotenv()

app = FastAPI()

app.include_router(auth_router)
app.include_router(ocr_router)

# CORS
origins = [
    "http://localhost:3000",
    "https://localhost:3000",
    "https://sion99.github.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


