from sqlalchemy.orm import Session

from ...data.models.country import CountryModel
from ...domain.schemas.country import CountrySchema
from ...domain.errors.api_error import ApiError

class CountryService:

    def __init__(self, db: Session) -> None:
        self.db = db
        self.country = db.query(CountryModel)

    def get_countries(self) -> list[CountryModel]:
        return self.country.all()

    def create_country(self, country: CountrySchema) -> CountryModel:
        new_country = CountryModel(**country.model_dump())

        if self.country.filter_by(code_iso_3=new_country.code_iso_3).first():
            raise ApiError.not_found("code_iso_3 already exists")

        self.db.add(new_country)
        self.db.commit()
        return new_country

    def get_country_by_id(self, id: int) -> CountryModel:
        return self.country.filter(CountryModel.id == id).first()

    def create_csv(self):
        pass
