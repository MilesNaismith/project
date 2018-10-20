from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///products.db')
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    metro_price = Column(String(10))
    auchan_price = Column(String(10))
    perekrestok_price = Column(String(10))
    
    def __init__(self, name = None, metro_price = None, auchan_price = None, perekrestok_price = None):
        self.name = name
        self.metro_price = metro_price
        self.auchan_price = auchan_price
        self.perekrestok_price = perekrestok_price
    
    def __repr__(self):
        return '<Product {}>'.format(self.name)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)