from app import app
from models.order_details import orders
from flask import render_template
from flask.templating import render_template

@app.route('/')
def index():
    return render_template('index.html', title='Perfect Pizzas', order_details=orders)

@app.route('/orders/<index>')
def order1():
    return render_template('order1.html', title='order1', order1 = orders[0])
