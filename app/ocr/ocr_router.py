from fastapi import APIRouter
from dotenv import load_dotenv

ocr_router = APIRouter(prefix='/ocr')

load_dotenv()


@ocr_router.get('/', tags=['OCR GET'])
async def print_hello():
    return {'msg': 'Hello'}
