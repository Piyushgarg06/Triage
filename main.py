from fastapi import FastAPI
import os 
from dotenv import load_dotenv
from routers.claims import router

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")
print(api_key)

os.makedirs("uploads", exist_ok=True)

app = FastAPI()
app.include_router(router)




