from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/test')
def test():
    return render_template('products.html', title='作品情報')
