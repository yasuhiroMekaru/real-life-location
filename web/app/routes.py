import json
import logging
import sys

from flask import render_template, request

from app import app
from app import controller

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/select_category', methods=['GET'])
def select_category():
	categories = controller.get_category()
	logger.info({
			'action': 'routes.py',
		})
	return render_template('select_category.html', categories=categories)


@app.route('/select_products/<category_id>', methods=['GET'])
def select_products(category_id):
	category_id = int(category_id)
	products_list = controller.get_products(category_id=category_id)
	return render_template('products.html', products_list=products_list)


@app.route('/main_menu/<products_id>', methods=['GET'])
def main_menu(products_id):
	products_id = int(products_id)
	datas = controller.get_all_data(products_id=products_id)
	return render_template('main_menu.html', datas=datas)


@app.route('/show_map/<real_life_location_id>', methods=['GET'])
def show_map(real_life_location_id):
	real_life_location_id = int(real_life_location_id)
	latlng = controller.get_latlng_data(real_life_location_id=real_life_location_id)
	return render_template('map.html', datas=latlng)

@app.route('/show_all_map/<products_id>', methods=['GET'])
def show_all_map(products_id):
	products_id = int(products_id)
	real_life_location_datas = controller.get_all_latlng_datas(products_id=products_id)
	return render_template('map.html', datas=real_life_location_datas)



