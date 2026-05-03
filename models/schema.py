from pydantic import BaseModel
from typing import Optional
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