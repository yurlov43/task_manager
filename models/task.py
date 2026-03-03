from pydantic import BaseModel, Field
from typing import Optional


class Task(BaseModel):
    """Модель задачи"""

    id: Optional[int] = Field(None, description="Уникальный идентификатор")
    description: str = Field(..., min_length=1, description="Описание задачи")
    completed: bool = Field(False, description="Статус выполнения")