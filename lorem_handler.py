from websockets import WebSocketServerProtocol, ConnectionClosed
import logging
from lorem_text import lorem # type: ignore
from utils import get_msg


async def lorem_handler(ws: WebSocketServerProtocol, logger: logging.Logger) -> None:
    query = "How many paragraphs do you want?"
    await ws.send(query)

    while True:
        data, e = await get_msg(ws)
        if e is not None:
            if e is not ConnectionClosed:
                logger.error(e)
            return

        paragraph_count = int(data) if isinstance(data, str) and data.isnumeric() else None

        if paragraph_count is None or paragraph_count < 0:
            await ws.send("Oops!  That was not a valid number.  Try again.")
            continue

        if paragraph_count == 0:
            await ws.close(1000, "Bye")
            break

        await ws.send(lorem.paragraphs(paragraph_count))
        await ws.send(query)
