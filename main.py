from fastapi import FastAPI,HTTPException,Depends,UploadFile
from database import get_db
from sqlalchemy.orm import Session
import models as m
from typing import List
import pyd
import shutil
from pathlib import Path
from auth import basic_auth

app=FastAPI()
import uuid
# @app.get("/movie", response_model=List[pyd.BaseMovie])
# def get_all_movie(db:Session=Depends(get_db)):
#     movies=db.query(m.Movie).all()
#     return movies

# @app.get("/product", response_model=List[pyd.ProductSchema])
# def get_all_products(db:Session=Depends(get_db)):
#     prods=db.query(m.Product).all()
#     return prods

# @app.get("/products/{product_id}")
# def get_product(product_id:int,db: Session=Depends(get_db)):
#     prod=db.query(m.Product).filter(
#         m.Product.id==product_id
#     ).first()

#     if not prod:
#         raise HTTPException(404,"НЕТ")
#     return prod


# @app.get("/movie/{movie_id}")
# def get_movie(movie_id:int,db: Session=Depends(get_db)):
#     mov=db.query(m.Movie).filter(
#         m.Movie.id==movie_id
#     ).first()

#     if not mov:
#         raise HTTPException(404,"НЕТ")
#     return mov

# @app.post("/product")
# def create_product(product:pyd.CreateProduct,db: Session= Depends(get_db)):
#     product_db=db.query(m.Product).filter(m.Product.name==product.name).first()
#     if product_db:
#         raise HTTPException(400,"Есть")
#     product_db=m.Product(name=product.name)
    

#     db.add(product_db)
#     db.commit()
#     return product_db


# @app.post("/movie")
# def create_movie(movie:pyd.CreateMovie,db: Session= Depends(get_db)):
#     movie_db=db.query(m.Movie).filter(m.Movie.name==movie.name).first()
#     if movie_db:
#         raise HTTPException(400,"Есть")
#     movie_db=m.Movie(name=movie.name,genre=movie.genre)

#     db.add(movie_db)
#     db.commit()
#     return movie_db


# @app.delete("/products/{product_id}")
# def d_product(product_id:int,db: Session=Depends(get_db)):
#     prod=db.query(m.Product).filter(
#         m.Product.id==product_id
#     ).first()

#     if not prod:
#         raise HTTPException(404,"НЕТ")
#     db.delete(prod)
#     db.commit()
#     return {"msg":"Товар удален"}

# @app.delete("/movies/{movie_id}")
# def d_movie(movie_id:int,db: Session=Depends(get_db)):
#     prod=db.query(m.Movie).filter(
#         m.Movie.id==movie_id
#     ).first()

#     if not prod:
#         raise HTTPException(404,"НЕТ")
#     db.delete(prod)
#     db.commit()
#     return {"msg":"Товар удален"}
# #создать модель с 3 полями или больше, сделать посев, и метод
# # для вывода всех строк из вашей модели

@app.get("/movies", response_model=List[pyd.MovieSchema])
def get_all_movie(db:Session=Depends(get_db)):
    movies=db.query(m.Movie).all()
    return movies
@app.get("/genres", response_model=List[pyd.BaseGenre])
def get_all_genre(db:Session=Depends(get_db)):
    genre=db.query(m.Genre).all()
    return genre
@app.get("/movies/{movie_id}", response_model=pyd.MovieSchema)
def get_one_movie(movie_id:int,db: Session=Depends(get_db)):
    mov=db.query(m.Movie).filter(
        m.Movie.id==movie_id
    ).first()

    if not mov:
        raise HTTPException(404,"Такого фильма нет")
    return mov


@app.post("/movies")
def create_movie(movie:pyd.CreateMovie,Verifcation = Depends(basic_auth),db: Session= Depends(get_db)):
    movie_db=db.query(m.Movie).filter(m.Movie.name==movie.name).first()
    if movie_db:
        raise HTTPException(400,"Есть")
    movie_db=m.Movie(name=movie.name,duration=movie.duration,rating=movie.rating,description=movie.description)

    if movie.genres is None:
        raise HTTPException(404,"Вы не ввели жанр")
    else:
        for genre in movie.genres:
            gen=db.query(m.Genre).filter(m.Genre.name==genre.name).first()
            if gen is None:
                gen=m.Genre(name=genre.name,description=genre.description)
            db.add(gen)
            db.commit()
            movie_db.genres.append(gen)
                
    db.add(movie_db)
    db.commit()
    db.refresh(movie_db)
    return movie_db

@app.post("/genres")
def create_genre(genre:pyd.CreateGenre,Verifcation = Depends(basic_auth),db: Session= Depends(get_db)):
    genre_db=db.query(m.Genre).filter(m.Genre.name==genre.name).first()
    if genre_db:
        raise HTTPException(400,"Есть")
    genre_db=m.Genre(name=genre.name,description=genre.description)
    
    db.add(genre_db)
    db.commit()
    db.refresh(genre_db)
    return genre_db

@app.put("/movies")
def update_movie(movie:pyd.CreateMovie,Verifcation = Depends(basic_auth),db: Session= Depends(get_db)):
    movie_db=db.query(m.Movie).filter(m.Movie.name==movie.name).first()
    if movie_db is None:
        raise HTTPException(400,"Нет такого фильма")
    movie_db.name=movie.name
    movie_db.duration=movie.duration
    movie_db.rating=movie.rating
    movie_db.description=movie.description

    if movie.genres is None:
        raise HTTPException(404,"Вы не ввели жанр")
    else:
        movie_db.genres.clear()
        for genre in movie.genres:
            gen=db.query(m.Genre).filter(m.Genre.name==genre.name).first()
            if gen is None:
                gen=m.Genre(name=genre.name,description=genre.description)
            db.add(gen)
            db.commit()
            movie_db.genres.append(gen)
                
    db.add(movie_db)
    db.commit()
    db.refresh(movie_db)
    return movie_db
@app.delete("/movies/{movie_id}")
def delete_movie(movie_id:int,Verifcation = Depends(basic_auth),db: Session=Depends(get_db)):
    dmovie=db.query(m.Movie).filter(
        m.Movie.id==movie_id
    ).first()

    if not dmovie:
        raise HTTPException(404,"Нет такого фильма")
    db.delete(dmovie)
    db.commit()
    return {"msg":"Фильм удален"}

@app.put("/movies/{id}/image")
async def create_upload_file(image: UploadFile,id:int,Verifcation = Depends(basic_auth),db: Session=Depends(get_db)):
    movie=db.query(m.Movie).filter(
        m.Movie.id==id
    ).first()
    image.file.read()
    size_mb=image.file.tell()/1024/1024
    image.file.seek(0)
    if size_mb>2:
        raise HTTPException(status_code=400,detail="Размер файла не должен превышать 2MB")
    
    random_uuid = uuid.uuid4()
    extension = Path(image.filename).suffix
    file_path=f"image/{random_uuid}{extension}"
    if not movie:
        raise HTTPException(404)
    if extension not in (".png", ".jpeg", ".jpg"):
        raise HTTPException(400, "Неверный тип данных")
    with open(file_path, "wb") as f:
        shutil.copyfileobj(image.file, f)
    movie.poster = f"{file_path}"
    db.commit()
    db.refresh(movie)
    return movie  

@app.post("/user", response_model=pyd.BaseUser)
def user_reg(create_user: pyd.CreateUser, db: Session = Depends(get_db),Verifcation = Depends(basic_auth)):
        user_db = db.query(m.User).filter(m.User.user_name == create_user.user_name).first()
        if user_db:
            raise HTTPException(400, "Логин занят")
        user_db = m.User()
        user_db.user_name = create_user.user_name
        user_db.user_password = create_user.user_password
        user_db.email = create_user.email
        db.add(user_db)
        db.commit()
        return user_db


@app.get("/test")
def get_test(user_name: m.User = Depends(basic_auth)):
    return {"r": 2}


