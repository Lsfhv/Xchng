import asyncio
import websockets
import json

async def handler(websocket, lst):
    st = ['b', 'a']
    while True:
        message = await websocket.recv()
        # print(json.loads(message['U']))
        message = json.loads(message)
        message = {k: v for k,v in message.items() if k in st}
        # print(message)
        lst.append(message)


async def getStream(lst):
    url = "wss://stream.binance.com:9443/ws/btcusdt@depth"
    async with websockets.connect(url) as ws:
        await handler(ws, lst)
        await asyncio.Future()  # run forever

def wssRun(lst):
    asyncio.run(getStream(lst))