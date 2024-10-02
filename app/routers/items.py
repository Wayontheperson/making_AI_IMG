# app/api/v1/endpoints/items.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import item as crud_item
from db.session import get_db
from schemas import item as schemas_item

router = APIRouter()


@router.get("/")
async def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    _item = crud_item.get_item(db, skip=skip, limit=limit)
    return schemas_item.Response(
        code="200", status="ok", message="Item read successfully", result=_item
    ).model_dump()


@router.post("/create")
async def create_item(request: schemas_item.RequestItem, db: Session = Depends(get_db)):
    crud_item.create_item(db, item=request.parameter)
    return schemas_item.Response(
        status="Ok", code="200", message="Item created successfully"
    )


import requests
