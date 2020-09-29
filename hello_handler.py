import logging
from websockets import WebSocketServerProtocol, ConnectionClosed
from utils import get_msg


async def hello_handler(ws: WebSocketServerProtocol, logger: logging.Logger) -> None:
    query = "Hi, What is your name?"
    await ws.send(query)

    while True:
        data, e = await get_msg(ws)
        if e is not None:
            if e is not ConnectionClosed:
                logger.error(e)
            return

        name = data if isinstance(data, str) else None

        if name is None:
            await ws.send("That was invalid, try again!")
            continue

        logger.info(f"<{name}")
        if name == "Bye":
            await ws.close(1000, "Bye")
            break

        await ws.send(f"Hello {name}!")
        await ws.send(query)
    return
