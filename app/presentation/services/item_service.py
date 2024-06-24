from sqlalchemy.orm import Session
from ...domain.schemas.item import ItemSchema
from ...data.models.item import Item as ItemModel
from ...domain.errors.api_error import ApiError


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
        model_items = self.item.filter(ItemModel.is_active == True).all()
        return [item.to_dict() for item in model_items]

    def find_item_by_id(self, item_id: int) -> ItemModel:
        item_found = self.item.filter(ItemModel.id == item_id).first()
        if not item_found:
            raise ApiError.not_found("Item not found")
        return item_found

    def update_item(self, item_id: int, item: ItemSchema) -> ItemModel:
        item_found = self.find_item_by_id(item_id)

        item_schema = item.model_dump()
        item_found.price = item_schema["price"]
        item_found.description = item_schema["description"]
        item_found.img = item_schema["img"]
        self.db.commit()

        return item_found.to_dict()

    def delete_item(self, item_id: int):
        item_found = self.find_item_by_id(item_id)
        if not item_found:
            raise ApiError.not_found("Item not found")

        item_found.is_active = False
        self.db.commit()
        
        return item_found.to_dict()
