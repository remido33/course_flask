from datetime import date
from pydantic import BaseModel, ConfigDict, computed_field


class AnimalCreate(BaseModel):
    type: str
    name: str
    birth_date: date
    breed: str
    image_url: str

    @computed_field
    @property
    def age(self) -> str:
        today = date.today()
        years = today.year - self.birth_date.year
        months = today.month - self.birth_date.month
        days_diff = today.day - self.birth_date.day

        if days_diff < 0:
            months -= 1

        if months < 0:
            years -= 1
            months += 12

        if years <= 0:
            return f"{months} month{'s' if months != 1 else ''}"
        return f"{years} year{'s' if years != 1 else ''} {months} month{'s' if months != 1 else ''}"


class AnimalResponse(AnimalCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
