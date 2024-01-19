from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
import enum


class Priority(enum.Enum):
    ONE = 1
    TWO = 2
    THREE = 3


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    timestamp_start = Column(DateTime, default=datetime.now)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    priority = Column(Enum(Priority))
    timestamp_finish = Column(DateTime, nullable=True)
    list_id = Column(Integer, ForeignKey('task_lists.id'), default=None)
    todo_list = relationship('ToDoList', back_populates='tasks')



class ToDoList(Base):
    __tablename__ = 'task_lists'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    tasks = relationship('Task', back_populates='todo_list', cascade='all, delete-orphan')

