from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field


T = TypeVar("T")


class ItemSchema(BaseModel):
    id: Optional[int] = Field(default=None, description="ID of the item(read-only)")
    title: Optional[str] = None
    description: Optional[str] = None

    class Config:
        from_attributes = True


class Request(BaseModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestItem(BaseModel):
    parameter: ItemSchema = Field(...)


class Response(BaseModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T] = None
