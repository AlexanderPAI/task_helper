from dataclasses import dataclass
from datetime import datetime


@dataclass
class Project:
    name: str
    description: str
    customer: str


@dataclass
class Customer:
    name: str


@dataclass
class User:
    name: str
    telegram_id: int


@dataclass
class Task:
    title: str
    description: str
    executor: User
    project: Project
    created_at: datetime | None = None
    updated_at: datetime | None = None
