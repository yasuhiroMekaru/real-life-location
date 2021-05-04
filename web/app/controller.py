import logging

from app.database import session
from app.model import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def insert_category(data):
	category = Category()
	category.category = data
	session.add(category)
	session.commit()

def insert_products(datas):
	products = Products()
	products.title = datas['title']
	products.director = datas['director']
	products.overview = datas['overview']
	products.image_path = datas['image_path']
	products.category_id = datas['category_id']
	session.add(products)
	session.commit()

def insert_real_life_location(datas):
	rll = Real_life_location()
	rll.name = datas['name']
	rll.scene = datas['scene']
	rll.overview = datas['overview']
	rll.image_path = datas['image_path']
	rll.latitude = datas['latitude']
	rll.longitude = datas['longitude']
	rll.products_id = datas['products_id']
	session.add(rll)
	session.commit()


def get_category():
	"""
	Args:
		None
	Return:
		List
	"""
	categories = session.query(Category).all()
	datas = []
	for category in categories:
		datas.append(category.category)
	logger.info({
			'action': 'controller.py',
			'datas': datas,
			'datas type': type(datas),
			'datas[0]': datas[0],
			'datas[0] type': type(datas[0])
		})
	return datas


def get_products(category_id):
	"""
	Args:
		category_id (int): カテゴリid
	Return:
		List
	"""
	products = session.query(Products.products_id, Products.title).filter(Products.category_id == category_id).all()
	datas = []
	for product in products:
		datas.append(product)
		logger.info({
			'action': 'controller.py',
			'datas': datas,
			'datas type': type(datas),
			'datas[0]': datas[0][0],
			'datas[0] type': type(datas[0][0])
		})
	return datas


def get_all_datas(products_id):
	"""
	Args:
		products_id (int): 作品id
	Return:
		List
	"""
	all_datas = session.query(Products, Real_life_location).\
	join(Real_life_location, Products.products_id==Real_life_location.products_id).\
	filter(Products.products_id==products_id).all()
	datas = []
	for all_data in all_datas:
		datas.append(all_data)
	main_datas = []
	for data in datas:
		main_data = {}
		main_data['p_title'] = data.Products.title,
		main_data['p_director'] = data.Products.director,
		main_data['p_overview'] = data.Products.overview,
		main_data['p_image_path'] = data.Products.image_path,
		main_data['r_name'] = data.Real_life_location.name,
		main_data['r_scene'] = data.Real_life_location.scene,
		main_data['r_overview'] = data.Real_life_location.overview,
		main_data['r_image_path'] = data.Real_life_location.image_path,
		main_data['r_latitude'] = data.Real_life_location.latitude,
		main_data['r_longitude'] = data.Real_life_location.longitude
		main_datas.append(main_data)

	logger.info({
			'action': 'controller.py',
			'main_datas': main_datas,
			'main_datas[0]': main_datas[0],
			'main_datas[0] type': type(main_datas[0])
		})
	return main_datas




if __name__ == '__main__':
	datas = {
		'name': '赤城山',
		'scene': '高橋兄弟のホーム',
		'overview': 'RX-7の聖地。',
		'image_path': '/',
		'latitude': '36',
		'longitude': '138',
		'products_id': 3
	}
	# insert_real_life_location(datas)

	r = get_all_datas(products_id=3)



