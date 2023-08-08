import uuid, os

from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/post")
async def save_images(file: UploadFile):
    UPLOAD_DIR = './images'
    content = await file.read()
    filename = f"{str(uuid.uuid4())}.jpg"
    with open(os.path.join(UPLOAD_DIR, filename), "wb") as fp:
        fp.write(content)
    return {"filename" : filename}