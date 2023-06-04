import requests
from constants import BID, ASK
from src.models.order import Order

from constants import binanceOrderbookSnapshot

def getSnapshot():
    response = requests.get(binanceOrderbookSnapshot).json()
    return [format(BID, response['bids']), format(ASK, response['asks'])]

def format(side, data):
    if side != BID and side != ASK:
        raise TypeError("Side not ASK or BID")
    return list(map(lambda x: Order(x[0], x[1], side), data))
