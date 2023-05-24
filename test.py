import asyncio
import websockets
import requests


async def handler(websocket):
    while True:
        message = await websocket.recv()
        print(message)


async def main():
    url = "wss://stream.binance.com:9443/ws/btcusdt@depth"
    async with websockets.connect(url) as ws:
        await handler(ws)
        await asyncio.Future()  # run forever


# if __name__ == "__main__":
#     asyncio.run(main())
url = "https://api3.binance.com/api/v3/depth?symbol=BTCUSDT"

# A GET request to the API
response = requests.get(url)

# Print the response
response_json = response.json()
print(response_json)
print("Received")





