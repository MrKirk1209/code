from sqlalchemy.orm import Session
from database import engine
import models as m

m.Base.metadata.drop_all(bind=engine)

m.Base.metadata.create_all(bind=engine)

with Session(bind=engine) as session:
    cat1 = m.Category(name='Еда', description='Вкусная, для людей')
    session.add(cat1)
    p1=m.Product(name="milk",categories=[cat1])
    session.add(p1)

    m1=m.Movie(name="The E",genre="horror")
    session.add(m1)

    session.commit()