from pydantic import BaseModel,Field
from datetime import datetime
from typing import List, Optional
# class BaseProduct(BaseModel):
#     name: str=Field(min_length=3,max_length=255,example="Milk")

class BaseMovie(BaseModel):
    name: str = Field(min_length=3, max_length=255, example="The End")
    duration: int = Field(example=120)
    rating: float = Field(example=8.3)
    description: str = Field(min_length=3, max_length=255, example="best horror")
    poster: Optional[str] = Field(None, min_length=3, max_length=255, example="/image/maxresdefault.jpg") 
    date_add: Optional[datetime] = Field(None, example=datetime.now())


class BaseGenre(BaseModel):
    name: str=Field(min_length=3,max_length=255,example="horror")
    description: str=Field(min_length=3,max_length=255,example="scary movie")


# class CategoryBase(BaseModel):
#     # Field используется для описания столбца, None - не обязательно, ... - обязательно
#     # gt - больше чем, example - пример для доки
#     id: int = Field(None, gt=0, example=1)
#     name: str = Field(..., max_length=255, example='Еда')
#     description: str = Field(None, max_length=255, example='То что можно скушать')