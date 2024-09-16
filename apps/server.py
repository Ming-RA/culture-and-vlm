from fastapi import FastAPI, HTTPException, File, UploadFile
from pydantic import BaseModel

app = FastAPI()


class ImageModel(BaseModel):
    filename: str
    content_type: str


@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    return ImageModel(filename=file.filename, content_type=file.content_type)
