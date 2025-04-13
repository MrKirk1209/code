from pydantic import BaseModel,Field

class BaseProduct(BaseModel):
    name: str=Field(min_length=3,max_length=255,example="Milk")

class BaseMovie(BaseModel):
    name: str=Field(min_length=3,max_length=255,example="The End")
    genre:  str=Field(min_length=3,max_length=255,example="horror")

class CategoryBase(BaseModel):
    # Field используется для описания столбца, None - не обязательно, ... - обязательно
    # gt - больше чем, example - пример для доки
    id: int = Field(None, gt=0, example=1)
    name: str = Field(..., max_length=255, example='Еда')
    description: str = Field(None, max_length=255, example='То что можно скушать')