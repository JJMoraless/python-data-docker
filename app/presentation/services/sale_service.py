from sqlalchemy.orm import Session
from typing import List, Dict, Any
from sqlalchemy.exc import IntegrityError

from .item_service import ItemService
from ...domain.schemas.sale import SaleSchema, ItemDetailSchema
from ...domain.errors.api_error import ApiError
from ...data.models.sale import SaleModel
from ...data.models.item import Item as ItemModel
from ...data.models.detail import Detail as DetailModel


item_service = ItemService(Session())


class SaleService:

    def __init__(self, db: Session) -> None:
        self.db = db
        self.sale = db.query(SaleModel)
        self.item = db.query(ItemModel)
        self.detail = db.query(DetailModel)

    def create_sale(self, sale_dto: SaleSchema, user_id: int) -> SaleModel:
        sale_created = SaleModel()
        sale_created.currency = sale_dto.items_quantity
        sale_created.sub_total_amount = sale_dto.sub_total_amount
        sale_created.currency = sale_dto.currency
        sale_created.items_quantity = sale_dto.items_quantity
        sale_created.total = sale_dto.total
        sale_created.user_id = user_id

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

    def add_items_to_sale(
        self, sale_id: int, items_dto: List[ItemDetailSchema], user_id: int
    ) -> SaleModel:
        sale = self.find_sale_by_user(sale_id, user_id)

        items_found = self.item.filter(
            ItemModel.id.in_([item.item_id for item in items_dto])
        ).all()

        if len(items_found) != len(items_dto):
            raise ApiError.not_found("Item not found")

        try:
            for item_dto in items_dto:
                item = next(item for item in items_found if item.id == item_dto.item_id)
                price = item.price
                total = price * item_dto.quantity

                detail = DetailModel(
                    item_id=item_dto.item_id,
                    quantity=item_dto.quantity,
                    price=price,
                    total=total,
                    discount_amount=0,
                    sale_id=sale.id,
                )
                self.db.add(detail)

            self.db.commit()

        except IntegrityError:
            self.db.rollback()

            raise ApiError.bad_request(
                "A detail with the same sale_id and item_id already exists"
            )

        except Exception as e:
            self.db.rollback()
            raise e

        return sale.to_dict()

    def get_sale_with_details(self, sale_id: int, user_id: int) -> Dict[str, Any]:
        sale = self.find_sale_by_user(sale_id, user_id)

        if not sale:
            raise ApiError.not_found("Sale not found")

        details_sale = self.detail.filter(DetailModel.sale_id == sale_id).all()
        sale_map = sale.to_dict()
        sale_map["details"] = [detail.to_dict() for detail in details_sale]

        return sale_map

    def cancel_sale(self, sale_id: int, user_id: int) -> SaleModel:
        sale = self.find_sale_by_user(sale_id, user_id)

        if sale.is_completed:
            raise ApiError.bad_request("Sale is already completed")

        sale.is_cancelled = True
        self.db.commit()

        return sale.to_dict()

    def complete_sale(self, sale_id: int, user_id: int) -> SaleModel:
        sale_found = self.find_sale_by_user(sale_id, user_id)

        if not sale_found:
            raise ApiError.not_found("Sale not found")

        if sale_found.is_completed:
            raise ApiError.bad_request("Sale is already completed")

        sale_found.is_completed = True
        self.db.commit()

        return sale_found.to_dict()

    def get_sales(
        self, user_id: int, page: int, page_size: int
    ) -> List[Dict[str, Any]]:
        offset = (page - 1) * page_size

        sales = (
            self.sale.filter(SaleModel.user_id == user_id)
                .offset(offset)
                .limit(page_size)
                .all()
        )

        return [sale.to_dict() for sale in sales]
