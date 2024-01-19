from fastapi import FastAPI, APIRouter, Depends
import models
from database import engine
from typing import Mapping, Any, List
from sqlalchemy.orm import Session

import service
from database import get_db
from dependencies import valid_task_id
from schema import TaskOut, ToDoOut, ToDoIn, TaskIn

app = FastAPI()
router = APIRouter()
models.Base.metadata.create_all(bind=engine)


@router.get("/lists", response_model=List[ToDoOut])
async def get_lists(db: Session = Depends(get_db)):
    gotten_lists = await service.get_lists(db)
    return gotten_lists


@router.get("/lists/{list_id}", response_model=ToDoOut)
async def get_list_by_id(list_id: int, db: Session = Depends(get_db)):
    gotten_list = await service.get_list_by_id(db, list_id)
    return gotten_list


@router.get("/tasks", response_model=List[TaskOut])
async def get_tasks(db: Session = Depends(get_db)):
    gotten_tasks = await service.get_tasks(db)
    return gotten_tasks


@router.get("/tasks/{task_id}", response_model=TaskOut)
async def get_task_by_id(task_id: int, db: Session = Depends(get_db)):
    gotten_task = await service.get_task_by_id(db, task_id)
    return gotten_task


@router.post("/task", response_model=TaskOut)
async def post_task(
        data: TaskIn,
        db: Session = Depends(get_db)
):
    posted_task = await service.insert_task(db, data)
    return posted_task


@router.post("/list", response_model=ToDoOut)
async def post_list(
        data: ToDoIn,
        db: Session = Depends(get_db)
):
    posted_list = await service.insert_list(db, data)
    return posted_list


@router.delete("/list/{list_id}", response_model=ToDoOut)
async def delete_lisr_by_id(list_id: int, db: Session = Depends(get_db)):
    deleted_list = await service.delete_list_by_id(db, list_id)
    return deleted_list


@router.delete("/task/{task_id}", response_model=TaskOut)
async def delete_lisr_by_id(task_id: int, db: Session = Depends(get_db)):
    deleted_task = await service.delete_task_by_id(db, task_id)
    return deleted_task


app.include_router(router)
