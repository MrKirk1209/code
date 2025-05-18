from sqlalchemy.orm import Session
from database import engine
import models as m
import datetime
m.Base.metadata.drop_all(bind=engine)

m.Base.metadata.create_all(bind=engine)

with Session(bind=engine) as session:
    # cat1 = m.Category(name='Еда', description='Вкусная, для людей')
    # session.add(cat1)
    # p1=m.Product(name="milk",categories=[cat1])
    # session.add(p1)

    g1=m.Genre(name="horror",description="scary movie")
    session.add(g1)

    m1=m.Movie(name="The E",duration=120,rating=8.3,description="best horror",poster="/image/maxresdefault.jpg",date_add=str(datetime.datetime.now()),genres=[g1])
    session.add(m1)

    u1=m.User(email="false@gmail.com",user_name="Mr.Noski",user_password="1234")
    session.add(u1)

    session.commit()