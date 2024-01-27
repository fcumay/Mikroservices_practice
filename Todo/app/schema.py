from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from .models import Priority


class TaskIn(BaseModel):
    name: str
    priority: Priority
    timestamp_finish: Optional[datetime] = None
    list_id: int


class TaskOut(BaseModel):
    id: int
    timestamp_start: datetime
    name: str
    is_active: bool
    priority: Priority
    timestamp_finish: Optional[datetime] = None
    list_id: int


class ToDoIn(BaseModel):
    name: str


class ToDoOut(BaseModel):
    id: int
    name: str
    tasks: Optional[List[TaskOut]] = None


class UserIn(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int | None = None
    username: str


class Token(BaseModel):
    access_token: str
    token_type: str
