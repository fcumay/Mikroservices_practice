import service_auth
from fastapi import FastAPI, APIRouter

import models

from schema import Token, UserIn, UserOut
from database import engine
from typing import List
from sqlalchemy.orm import Session

import service
from database import get_db
from schema import TaskOut, ToDoOut, ToDoIn, TaskIn
from fastapi import Depends

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


@router.post("/register", response_model=Token)
async def register_user(
        data: UserIn,
        db: Session = Depends(get_db)
):
    token = service_auth.create_user(data, db)
    return token


@router.post("/token", response_model=Token)
async def login_for_access_token(
        data: UserIn,
        db: Session = Depends(get_db)):
    token = service_auth.authenticate_user(db, data.username, data.password)
    return token


@router.get("/users/me/", response_model=UserOut)
async def read_users_me(
        token: str,
        db: Session = Depends(get_db)
):
    current_user = service_auth.get_current_user(token, db)
    return current_user


app.include_router(router)
