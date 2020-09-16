import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref
import uuid

engine = sqlalchemy.create_engine('sqlite:///po.db')
Base = declarative_base()

class Order_Produck(Base):
    __tablename__ = 'order_product'
    id = Column(String(35), primary_key=True, unique=True)
    order_is = Column(Integer, ForeignKey('orders.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    quantity = Column(Integer)

    order =relationship("Order",backref=backref(
        "order_products", cascade="all, delete-orphan"))
    product =relationship("Product", backref=backref(
        "order_products", cascade="all, delete-orphan0"))
    
    def __init__(self, order=None, product=None, quantity=None):
        self.id = uuid.uuid4().hex
        self.order = order
        self.product = product
        self.quantity = quantity
    
    def __repr__(self):
        return '<Order_Product {}>'.format(self.order.name+" "+self.product.name)

class Product(Base):