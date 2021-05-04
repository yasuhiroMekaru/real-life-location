import json

from flask import render_template, request

from app import app
import controller

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/select_category', methods=['GET', 'POST'])
def select_category():
	categories = controller.get_category()
	return render_template('select_category.html', categories=categories)


@app.route('/select_products', methods=['GET', 'POST'])
def select_products():
	data = request.get_data()
	category_id = int(json.loads(data))
	products_list = controller.get_products(category_id=category_id)
	return render_template('select_products.html', products_list=products_list)


@app.route('/main_menu', methods=['GET', 'POST'])
def main_menu():
	data = request.get_data()
	products_id = int(json.loads(data))
	datas = controller.get_all_data(products_id=products_id)
	return render_template('main_menu.html', datas=datas)


@app.route('/show_map')
def show_map():
	data = request.get_data()
	latlng = json.loads(data)
	return render_template('map.html', datas=latlng)

