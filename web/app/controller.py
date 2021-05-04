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
	try:
		categories = session.query(Category).all()
		datas = []
		for category in categories:
			data = {}
			data['category_id'] = category.category_id
			data['category'] = category.category
			datas.append(data)
		logger.info({
				'action': 'controller.py',
				'datas': datas,
				'datas type': type(datas),
				'datas[0]': datas[0],
				'datas[0] type': type(datas[0])
			})
	finally:
		session.close()
	return datas


def get_products(category_id):
	"""
	Args:
		category_id (int): カテゴリid
	Return:
		List
	"""
	try:
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
	finally:
		session.close()
	return datas


def get_all_data(products_id):
	"""
	Args:
		products_id (int): 作品id
	Return:
		dict
	"""
	try:
		products_datas = session.query(Products).filter(Products.products_id==products_id).all()
		main_data = {}
		for products_data in products_datas:
			main_data['p_id'] = products_data.products_id
			main_data['p_title'] = products_data.title
			main_data['p_director'] = products_data.director
			main_data['p_overview'] = products_data.overview
			main_data['p_image_path'] = products_data.image_path
		# logger.info({
		# 		'action': 'controller.py',
		# 		'main_data': main_data
		# 	})
		rrl_datas = session.query(Real_life_location).filter(Real_life_location.products_id==products_id).all()
		real_life_location_datas = []
		for rrl_data in rrl_datas:
			data = {}
			data['r_name'] = rrl_data.name
			data['r_scene'] = rrl_data.scene
			data['r_overview'] = rrl_data.overview
			data['r_image_path'] = rrl_data.image_path
			data['r_latitude'] = rrl_data.latitude
			data['r_longitude'] = rrl_data.longitude
			data['r_id'] = rrl_data.real_life_location_id
			real_life_location_datas.append(data)
		# logger.info({
		# 		'action': 'controller.py',
		# 		'real_life_location_datas': real_life_location_datas
		# 	})
		main_data['real_life_location_data'] = real_life_location_datas
	finally:
		session.close()

	return main_data


def get_latlng_data(real_life_location_id):
	"""
	Args:
		real_life_location_id (int): 聖地id
	Return:
		List
	"""
	try:
		datas = session.query(Real_life_location).\
		filter(Real_life_location.real_life_location_id==real_life_location_id).all()
		real_life_location_data = {}
		real_life_location_data['name'] = datas[0].name
		real_life_location_data['scene'] = datas[0].scene
		real_life_location_data['overview'] = datas[0].overview
		real_life_location_data['image_path'] = datas[0].image_path
		real_life_location_data['latitude'] = float(datas[0].latitude)
		real_life_location_data['longitude'] = float(datas[0].longitude)
		logger.info({
				'action': 'controller.py',
				'real_life_location_data': real_life_location_data,
				'real_life_location_data type': type(real_life_location_data)
			})
		real_life_location_datas = []
		real_life_location_datas.append(real_life_location_data)
	finally:
		session.close()
	return real_life_location_datas


def get_all_latlng_datas(products_id):
	"""
	Args:
		products_id (int): 作品id
	Return:
		List
	"""
	try:
		rrl_datas = session.query(Real_life_location).filter(products_id==products_id).all()
		real_life_location_datas = []
		for rrl_data in rrl_datas:
			data = {}
			data['name'] = rrl_data.name
			data['scene'] = rrl_data.scene
			data['overview'] = rrl_data.overview
			data['image_path'] = rrl_data.image_path
			data['latitude'] = float(rrl_data.latitude)
			data['longitude'] = float(rrl_data.longitude)
			real_life_location_datas.append(data)
		logger.info({
				'action': 'controller.py',
				'real_life_location_datas': real_life_location_datas,
				'real_life_location_datas type': type(real_life_location_datas)
			})
	finally:
		session.close()
	return real_life_location_datas



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

	# r = get_all_latlng_datas(1)
	# get_latlng_data(1)



