from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
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


@app.post("/claim")
def claim(data:ClaimInput):
    return ClaimOutput(
        claim_id= data.claim_id,
        status= "recieved",
        extracted_text= data.description, 
        claim_category= "accident"
        )

