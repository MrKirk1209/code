from typing import List
from pyd.base_models import BaseGenre
from pydantic import BaseModel,Field,EmailStr
import datetime
# class CreateProduct(BaseModel):
#     name: str=Field(min_length=3,max_length=255,example="Milk")
class CreateMovie(BaseModel):
    name: str=Field(min_length=3,max_length=255,example="The End")
    duration: int=Field(example=120)
    rating:  float=Field(example=8.3)
    description:  str=Field(min_length=3,max_length=255,example="best horror")
    genres: List[BaseGenre]
class CreateGenre(BaseModel):
    name: str=Field(min_length=3,max_length=255,example="horror")
    description: str=Field(min_length=3,max_length=255,example="scary movie")

# class CategoryCreate(BaseModel):
#     name: str = Field(..., max_length=255, example='Еда')
#     description: str = Field(None, max_length=255, example='То что можно скушать')
class CreateUser(BaseModel):
    user_name: str = Field(example="Denis123", min_length=3, max_length=60)
    user_password: str = Field(example="qwerty123", min_length=8, max_length=60)
    email: EmailStr | None = Field(None)
