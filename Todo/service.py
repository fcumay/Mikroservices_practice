from sqlalchemy.orm import Session
from datetime import datetime

from schema import TaskOut, ToDoOut, TaskIn
from models import Task, ToDoList


async def insert_task(session: Session, task_data: TaskIn):
    new_task = Task(
        timestamp_start=datetime.now(),
        name=task_data.name,
        priority=task_data.priority,
        timestamp_finish=task_data.timestamp_finish,
        list_id=task_data.list_id
    )

    session.add(new_task)
    session.commit()
    session.refresh(new_task)

    return new_task


async def insert_list(session: Session, list_data: ToDoOut):
    new_list = ToDoList(
        name=list_data.name
    )

    session.add(new_list)
    session.commit()
    session.refresh(new_list)

    return new_list


async def get_lists(session: Session):
    gotten_lists = session.query(ToDoList).all()
    return gotten_lists


async def get_list_by_id(session: Session, list_id: int):
    todo_list = session.query(ToDoList).get(list_id)
    return todo_list


async def get_tasks(session: Session):
    gotten_tasks = session.query(Task).all()
    return gotten_tasks


async def get_task_by_id(session: Session, task_id: int):
    task = session.query(Task).get(task_id)
    return task


async def delete_list_by_id(session: Session, list_id: int):
    deleted_list = session.query(ToDoList).get(list_id)
    session.delete(deleted_list)
    session.commit()
    return deleted_list


async def delete_task_by_id(session: Session, task_id: int):
    deleted_task = session.query(Task).get(task_id)
    session.delete(deleted_task)
    session.commit()
    return deleted_task
