from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
import schemas
import crud
from database import SessionLocal

router = APIRouter(
    prefix="/todos"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", status_code=status.HTTP_201_CREATED)
def create_todo_endpoint(todo: schemas.ToDoRequest, db: Session = Depends(get_db)):
    created = crud.create_todo(db, todo)
    return created

@router.get("", response_model=List[schemas.ToDoResponse])
def get_todos(completed: bool = None, db: Session = Depends(get_db)):
    return crud.read_todos(db, completed)

@router.get("/{id}")
def get_todo_by_id(id: int, db: Session = Depends(get_db)):
    todo = crud.read_todo(db, id)
    if todo is None:
        raise HTTPException(status_code=404, detail="to do not found")
    return todo

@router.put("/{id}")
def update_todo_endpoint(id: int, todo: schemas.ToDoRequest, db: Session = Depends(get_db)):
    updated = crud.update_todo(db, id, todo)
    if updated is None:
        raise HTTPException(status_code=404, detail="to do not found")
    return updated

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_todo_endpoint(id: int, db: Session = Depends(get_db)):
    result = crud.delete_todo(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail="to do not found")
    return {"success": True}
