import logging
import websockets
from utils import get_msg


async def hello_handler(ws: websockets.WebSocketServerProtocol, logger: logging) -> None:
    query = "Hi, What is your name?"
    await ws.send(query)

    while True:
        name, e = await get_msg(ws)
        if e is not None:
            if e is not websockets.ConnectionClosed:
                logger.error(e)
            return

        logger.info(f"<{name}")
        if name == "Bye":
            await ws.close(1000, "Bye")
            break
        greeting = f"Hello {name}!"
        await ws.send(greeting)
        await ws.send(query)
    return
