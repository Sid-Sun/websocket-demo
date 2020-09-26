import websockets
import logging
from lorem_text import lorem
from utils import get_msg


async def lorem_handler(ws: websockets.WebSocketServerProtocol, logger: logging) -> None:
    query = "How many paragraphs do you want?"
    await ws.send(query)

    while True:
        paragraph_length, e = await get_msg(ws)
        if e is not None:
            if e is not websockets.ConnectionClosed:
                logger.error(e)
            return

        try:
            paragraph_length = int(paragraph_length)
        except ValueError:
            await ws.send("Oops!  That was no valid number.  Try again...")
            continue

        if paragraph_length == 0:
            await ws.close(1000, "Bye")
            break

        p = lorem.paragraphs(paragraph_length)
        await ws.send(p)
        await ws.send(query)
