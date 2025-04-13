from database import Base
from sqlalchemy import Column,Integer,String,Table,ForeignKey
from sqlalchemy.orm import relationship

product_category = Table('product_category', Base.metadata,
                         Column('product_id', ForeignKey('products.id'), primary_key=True),
                         Column('category_id', ForeignKey('categories.id'), primary_key=True)
                         )

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    description = Column(String(255), nullable=True)

class Product(Base):
    __tablename__="products"
    id= Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(255),unique=True)
    
# backref автоматически делает связь в другой таблице
    categories = relationship("Category", secondary="product_category", backref="products")

class Movie(Base):
    __tablename__="movies"
    id= Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(255),unique=True)
    genre=Column(String(255))



