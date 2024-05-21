from sqlalchemy.orm import Session

from src.data.models.country import Country as CountryModel
from src.domain.schemas.country import Country as CountrySchema


class CountryService:

    def __init__(self, db: Session) -> None:
        self.db = db
        self.country = db.query(CountryModel)

    def get_countries(self) -> list[CountryModel]:
        return self.country.all()

    def create_country(self, country: CountrySchema) -> CountryModel:
        new_country = CountryModel(**country.model_dump())
        self.db.add(new_country)
        self.db.commit()
        return new_country

    def get_country_by_id(self, id: int) -> CountryModel:
        return self.country.filter(CountryModel.id == id).first()

    def create_csv(self):
        pass
