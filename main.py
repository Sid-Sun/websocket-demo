import asyncio
import websockets
import logging
from hello_handler import hello_handler as hello
from lorem_handler import lorem_handler as lorem
from config import settings

logger = logging.getLogger("my logger")
logging.basicConfig()
logger.setLevel(logging.DEBUG)


async def router(ws: websockets.WebSocketServerProtocol, path: str) -> None:
    if path == "/lorem":
        await lorem(ws, logger)
    if path == "/" or path == "/hello":
        await hello(ws, logger)


start_server = websockets.serve(router, settings.host, settings.port)
logger.info(f"Listening on ws://{settings.host}:{settings.port}")

loop = asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
