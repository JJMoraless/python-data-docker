from sqlalchemy.orm import Session
from ...domain.schemas.sale import SaleSchema
from ...domain.errors.api_error import ApiError

from ...data.models.sale import SaleModel
from ...data.models.item import Item as ItemModel
from ...data.models.detail import Detail as DetailModel


class SaleService:

    def __init__(self, db: Session) -> None:
        self.db = db
        self.sale = db.query(SaleModel)
        self.item = db.query(ItemModel)
        self.detail = db.query(DetailModel)

    def create_sale(self, sale: SaleSchema, user_id: int) -> SaleModel:
        sale_schema = sale.model_dump()
        sale_schema["user_id"] = user_id

        sale_created = SaleModel(**sale_schema)
        self.db.add(sale_created)
        self.db.commit()

        return sale_created.to_dict()

    def find_sale_by_user(self, sale_id: int, user_id: int) -> SaleModel:
        sale_found = self.sale.filter(
            SaleModel.id == sale_id, SaleModel.user_id == user_id
        ).first()

        if not sale_found:
            raise ApiError.not_found("Sale not found")

        return sale_found

    def add_item_to_sale(self, sale_id: int, item_id: int, user_id: int) -> SaleModel:
        sale = self.find_sale_by_user(sale_id, user_id)

        item = self.db.query(ItemModel).filter(ItemModel.id == item_id).first()
        if not item:
            raise ApiError.not_found("Item not found")

        self.detail.


        self.db.commit()
        return sale.to_dict()
