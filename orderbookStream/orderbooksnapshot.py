import requests

def getSnapshot():

    url = "https://api3.binance.com/api/v3/depth?symbol=BTCUSDT"

    # A GET request to the API
    response = requests.get(url)

    # Print the response
    return response.json()