import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from app.database import Base
from app.database import ENGINE


class Products(Base):
	"""docstring for Products"""
	__tablename__ = 'products'
	products_id = Column('products_id', Integer, nullable=False, primary_key=True)
	title = Column('title', String(30), nullable=False,)
	director = Column('director', String(20), nullable=False,)
	overview = Column('overview', String(200), nullable=False,)
	image_path = Column('image_path', String(50))
	category_id = Column('category_id', Integer, nullable=False,)


class Category(Base):
	"""docstring for Category"""
	__tablename__ = 'category'
	category_id = Column('category_id', Integer, nullable=False, primary_key=True)
	category = Column('category', String(10), nullable=False)


class Real_life_location(Base):
	"""docstring for Real_life_location"""
	__tablename__ = 'real_life_location'
	real_life_location_id = Column('real_life_location_id', Integer, nullable=False, primary_key=True)
	name = Column('name', String(20), nullable=False,)
	scene = Column('scene', String(50), nullable=False,)
	overview = Column('overview', String(200), nullable=False,)
	image_path = Column('image_path', String(50))
	latitude = Column('latitude', String(15), nullable=False)
	longitude = Column('longitude', String(15), nullable=False)
	products_id = Column('products_id', Integer, nullable=False,)
		


def main(args):
	Base.metadata.create_all(bind=ENGINE)


if __name__ == '__main__':
	main(sys.argv)
