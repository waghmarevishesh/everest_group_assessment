from fastapi import APIRouter, HTTPException, Request, Depends
import requests
from pydantic import BaseModel

router = APIRouter()

@router.get('/hello')
def hello():
    return {"res": "hello"}
