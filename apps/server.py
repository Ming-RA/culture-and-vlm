from fastapi import FastAPI, HTTPException, File, UploadFile
from pydantic import BaseModel
from pipelines import VLM_Pipeline

app = FastAPI()


class ImageRequest(BaseModel):
    filename: str
    content_type: str
    prompt: str


@app.post("/upload-image/")
async def upload_image(request: ImageRequest):
    vlm_pipeline = VLM_Pipeline()
    vlm_pipeline.analyze_image(filename=request.filename, prompt=request.prompt)
