from sqlalchemy.orm import Session
from models.item import Item
from schemas.item import ItemSchema


def get_item(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()


def get_item_by_id(db: Session, book_id: int):
    return db.query(Item)


def create_item(db: Session, item: ItemSchema):
    _item = Item(title=item.title, description=item.description)
    db.add(_item)
    db.commit()
    db.refresh(_item)
    return _item


def remove_book(db: Session, item_id: int):
    _item = get_item_by_id(db=db, item_id=item_id)
    db.delete(_item)
    db.commit()


def update_book(db: Session, item_id: int, title: str, description: str):
    _item = get_item_by_id(db=db, item_id=item_id)
    _item.title = title
    _item.description = description
    db.commit()
    db.refresh(_item)
    return _item
