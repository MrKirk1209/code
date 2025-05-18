from database import Base
from sqlalchemy import Column,Integer,String,Table,ForeignKey,Float
from sqlalchemy.orm import relationship,Mapped

# product_category = Table('product_category', Base.metadata,
#                          Column('product_id', ForeignKey('products.id'), primary_key=True),
#                          Column('category_id', ForeignKey('categories.id'), primary_key=True)
#                          )

# class Category(Base):
#     __tablename__ = "categories"

#     id = Column(Integer, primary_key=True)
#     name = Column(String(255), unique=True)
#     description = Column(String(255), nullable=True)

# class Product(Base):
#     __tablename__="products"
#     id= Column(Integer,primary_key=True,autoincrement=True)
#     name=Column(String(255),unique=True)
    
# # backref автоматически делает связь в другой таблице
#     categories = relationship("Category", secondary="product_category", backref="products")


movie_genre = Table('movie_genre', Base.metadata,
                         Column('movie_id', ForeignKey('movies.id'), primary_key=True),
                         Column('genre_id', ForeignKey('genres.id'), primary_key=True)
                         )



class Genre(Base):
    __tablename__="genres"
    id= Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(255),unique=True)
    description=Column(String(255))

class Movie(Base):
    __tablename__="movies"
    id= Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(255),unique=True)
    duration=Column(Integer)
    rating=Column(Float)
    description=Column(String(255))
    poster=Column(String(255))
    date_add=Column(String(255))
    genres = relationship("Genre", secondary="movie_genre", backref="movies")

class User(Base):
    __tablename__="users"
    id= Column(Integer,primary_key=True,autoincrement=True)
    email = Column(String(255), nullable=True)
    user_name=Column(String(255))
    user_password=Column(String(255))