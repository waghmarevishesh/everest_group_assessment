from fastapi import APIRouter, HTTPException, Request, Depends
from pydantic import BaseModel
from typing import Optional
from utils import connection
import logging
from utils import simulateAI

router = APIRouter(prefix="/api")

class Project(BaseModel):
    name: str
    description: Optional[str] = None
    technologies: Optional[list] = None
    image_url: Optional[str] = None

@router.get('/projects')
def get_projects():
    try:
        db = connection.connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM projects")
        result = cursor.fetchall()
        return {"projects": result}
    except db.Error as err:
        logging.info(f"Error in query", str(err))
        raise HTTPException(status_code=500, detail=f"Error while fetching projecs {str(err)}")

@router.post('/addproject')
def add_project(request: Request, body: Project, db = Depends(connection.connect_db)):
    try:
        cursor = db.cursor()
        technologies = ", ".join(body.technologies) if body.technologies else ""
        cursor.execute("INSERT INTO PROJECTS(name, description, technologies, image_url) VALUES( %s, %s, %s, %s)", (body.name, body.description, technologies, body.image_url))
        db.commit()
        return {
            "response": "Project added successfuly"
        }
    
    except db.Error as err:
        logging.info(f"Error in query", str(err))
        raise HTTPException(status_code=500, detail=f"Error while adding the project {str(err)}")
    
@router.get('/{id}/getproject')
def get_projects(id: int, db = Depends(connection.connect_db)):
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM projects WHERE id = %s", (id))
        result = cursor.fetchall()
        summary =  simulateAI.generate_project_summary(result[0])
        return {
            "response": summary
        }
    except db.Error as err:
        logging.info(f"Error in query", str(err))
        raise HTTPException(status_code=500, detail=f"Error while getting the project {str(err)}")
