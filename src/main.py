from src.models.orderbook import Orderbook
from src.models.order import Order 

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from flask_cors import CORS, cross_origin

from flask import Flask, request

app = Flask(__name__)

orderbook = Orderbook()
orderbook.fillOrderbook()

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def index():
    return f'Welcome!'

# Get all the orders in the orderbook
@app.route('/orderbook')
@cross_origin()
def getOrderbook():
    return orderbook.getOrderbook()

# Place an order in the order book
@app.route('/placeorder', methods = ['PUT'])
def placeOrder():
    postData = request.get_json()
    order = Order((postData['price']), (postData['size']), postData['side'], postData['userId'])
    orderbook.match(order)
    return "Success"


app.run()

# export PYTHONPATH="${PYTHONPATH}:${pwd}"
