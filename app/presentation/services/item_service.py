from sqlalchemy.orm import Session
from ...domain.schemas.item import ItemSchema
from ...data.models.item import Item as ItemModel


class ItemService:

    def __init__(self, db: Session) -> None:
        self.db = db
        self.item = db.query(ItemModel)

    def create_item(self, item: ItemSchema):
        item_schema = item.model_dump()

        item_created = ItemModel(**item_schema)
        self.db.add(item_created)
        self.db.commit()

        return item_created.to_dict()

    def get_items(self) -> list:
        model_items = self.item.all()
        return [item.to_dict() for item in model_items]
