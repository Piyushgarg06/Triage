from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
import os 
from fastapi import File, UploadFile

os.makedirs("uploads", exist_ok=True)

app = FastAPI()

@app.get("/health")
def health():
    return {"status":"ok"}

class ClaimInput(BaseModel):
    claim_id: str
    description: str
    claim_type: str
    audio_file_path: Optional[str]

class ClaimOutput(BaseModel):
    claim_id: str
    status: str
    extracted_text: str
    claim_category: str

@app.post("/claim/upload")
def file(file:UploadFile = File(...)):
    file_path = os.path.join("uploads", file.filename)
    with open(file_path, 'wb') as f:
        f.write(file.file.read())
        

    return {"fileName": file.filename}

@app.post("/claim")
def claim(data:ClaimInput):
    return ClaimOutput(
        claim_id= data.claim_id,
        status= "received",
        extracted_text= data.description, 
        claim_category= "accident"
        )

