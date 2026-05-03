from fastapi import APIRouter
from services.processor import validate_file
from models.schema import ClaimInput, ClaimOutput
from fastapi import BackgroundTasks
import asyncio
from fastapi import File, UploadFile
import os
router = APIRouter()

@router.post("/claim")
def claim(data: ClaimInput, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_claim, data.claim_id)    
    return ClaimOutput(
        claim_id= data.claim_id,
        status= "received",
        extracted_text= data.description, 
        claim_category= "accident"
        )

@router.post("/claim/upload")
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