from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
import os 
from fastapi import File, UploadFile
from fastapi import BackgroundTasks
import asyncio

os.makedirs("uploads", exist_ok=True)

app = FastAPI()

image_extensions = [
    '.jpg', '.jpeg', '.jpe', '.jif', '.jfif', '.pjpeg', '.pjp', 
    '.png', '.apng',                                             
    '.bmp',                                                       
    '.tiff', '.tif',                                              
    '.webp',                                                      
    '.svg',
    '.ico', '.cur',
    '.avif',
    '.heif', '.heic',                                             
    '.raw', '.cr2', '.nef', '.orf', '.sr2'                        
]

doc_extensions = [
    '.pdf',
    '.doc', '.docx',                                              
    '.txt',
    '.rtf',                                                       
    '.odt',                                                       
    '.md',                                                        
    '.ppt', '.pptx',                                              
    '.xls', '.xlsx',
    '.csv'                                                        
]
valid_extensions = image_extensions + doc_extensions

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


def validate_file(file: UploadFile):
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in valid_extensions:
        return {"valid": False, "error": f"Invalid file extension: {ext}"}
    return {"valid": True}


@app.post("/claim/upload")
def upload_file(file: UploadFile = File(...)):
    validation = validate_file(file)
    if not validation["valid"]:
        return validation

    file_path = os.path.join("uploads", file.filename)
    with open(file_path, 'wb') as f:
        f.write(file.file.read())
    return {"fileName": file.filename}

async def process_claim(claim_id: str):
    await asyncio.sleep(3)
    print(f"Processed {claim_id}")


@app.post("/claim")
def claim(data: ClaimInput, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_claim, data.claim_id)    
    return ClaimOutput(
        claim_id= data.claim_id,
        status= "received",
        extracted_text= data.description, 
        claim_category= "accident"
        )
