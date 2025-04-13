from fastapi import FastAPI,HTTPException,Depends
from database import get_db
from sqlalchemy.orm import Session
import models as m
from typing import List
import pyd
app=FastAPI()

@app.get("/movie", response_model=List[pyd.BaseMovie])
def get_all_movie(db:Session=Depends(get_db)):
    movies=db.query(m.Movie).all()
    return movies

@app.get("/product", response_model=List[pyd.ProductSchema])
def get_all_products(db:Session=Depends(get_db)):
    prods=db.query(m.Product).all()
    return prods

@app.get("/products/{product_id}")
def get_product(product_id:int,db: Session=Depends(get_db)):
    prod=db.query(m.Product).filter(
        m.Product.id==product_id
    ).first()

    if not prod:
        raise HTTPException(404,"НЕТ")
    return prod


@app.get("/movie/{movie_id}")
def get_movie(movie_id:int,db: Session=Depends(get_db)):
    mov=db.query(m.Movie).filter(
        m.Movie.id==movie_id
    ).first()

    if not mov:
        raise HTTPException(404,"НЕТ")
    return mov

@app.post("/product")
def create_product(product:pyd.CreateProduct,db: Session= Depends(get_db)):
    product_db=db.query(m.Product).filter(m.Product.name==product.name).first()
    if product_db:
        raise HTTPException(400,"Есть")
    product_db=m.Product(name=product.name)
    

    db.add(product_db)
    db.commit()
    return product_db


@app.post("/movie")
def create_movie(movie:pyd.CreateMovie,db: Session= Depends(get_db)):
    movie_db=db.query(m.Movie).filter(m.Movie.name==movie.name).first()
    if movie_db:
        raise HTTPException(400,"Есть")
    movie_db=m.Movie(name=movie.name,genre=movie.genre)

    db.add(movie_db)
    db.commit()
    return movie_db


@app.delete("/products/{product_id}")
def d_product(product_id:int,db: Session=Depends(get_db)):
    prod=db.query(m.Product).filter(
        m.Product.id==product_id
    ).first()

    if not prod:
        raise HTTPException(404,"НЕТ")
    db.delete(prod)
    db.commit()
    return {"msg":"Товар удален"}

@app.delete("/movies/{movie_id}")
def d_movie(movie_id:int,db: Session=Depends(get_db)):
    prod=db.query(m.Movie).filter(
        m.Movie.id==movie_id
    ).first()

    if not prod:
        raise HTTPException(404,"НЕТ")
    db.delete(prod)
    db.commit()
    return {"msg":"Товар удален"}
#создать модель с 3 полями или больше, сделать посев, и метод
# для вывода всех строк из вашей модели