from pydantic import BaseModel,Field

class CreateProduct(BaseModel):
    name: str=Field(min_length=3,max_length=255,example="Milk")
class CreateMovie(BaseModel):
    name: str=Field(min_length=3,max_length=255,example="The End")
    genre:  str=Field(min_length=3,max_length=255,example="horror")
class CategoryCreate(BaseModel):
    name: str = Field(..., max_length=255, example='Еда')
    description: str = Field(None, max_length=255, example='То что можно скушать')
