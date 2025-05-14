from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import routes
import logging



logging.basicConfig(level=logging.INFO)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/health")
def health():
    return {"res": "OK"}

app.include_router(router=routes.router)

