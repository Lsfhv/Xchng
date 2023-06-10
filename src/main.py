from src.models.orderbook import Orderbook

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from flask_cors import CORS, cross_origin

from flask import Flask

app = Flask(__name__)

orderbook = Orderbook()
orderbook.fillOrderbook()

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# print(orderbook.getOrderbook())

@app.route('/')
@cross_origin()
def index():
    return 'Server Works!'


# @app.route('/greet')
# def say_hello():
#   return str(orderbook.bids.getBestPrice())

@app.route('/orderbook')
@cross_origin()
def getOrderbook():
    return orderbook.getOrderbook()


app.run()

# orderbook = Orderbook()

# (orderbook.fillOrderbook())

# print(orderbook.bids.getBestPrice(), orderbook.asks.getBestPrice())
# print(orderbook.asks.len)

# export PYTHONPATH="${PYTHONPATH}:${pwd}"
