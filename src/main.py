from src.models.orderbook import Orderbook

from http.server import BaseHTTPRequestHandler, HTTPServer
import time

from flask import Flask
app = Flask(__name__)

orderbook = Orderbook()
orderbook.fillOrderbook()

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/greet')
def say_hello():
  return str(orderbook.bids.getBestPrice())

# orderbook = Orderbook()

# (orderbook.fillOrderbook())

# print(orderbook.bids.getBestPrice(), orderbook.asks.getBestPrice())
# print(orderbook.asks.len)

# export PYTHONPATH="${PYTHONPATH}:/home/lsfhv/seagrate4tbhdd/Xchng"
