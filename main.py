import asyncio
import websockets
import logging
from hello_handler import hello_handler as hello
from lorem_handler import lorem_handler as lorem
from config.config import settings

logging.basicConfig(level=logging.INFO)


async def router(ws: websockets.WebSocketServerProtocol, path: str) -> None:
    if path == "/lorem":
        await lorem(ws, logging)
    if path == "/" or path == "/hello":
        await hello(ws, logging)


start_server = websockets.serve(router, settings.host, settings.port)
logging.info(f"Listening on ws://{settings.host}:{settings.port}")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
