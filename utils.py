from typing import Tuple, Union, Type

from websockets import Data, WebSocketServerProtocol, WebSocketException, ConnectionClosed


async def get_msg(ws: WebSocketServerProtocol) -> Tuple[Data, Union[None, Type[WebSocketException]]]:
    try:
        msg = await ws.recv()
        return msg, None
    except ConnectionClosed:
        return "", ConnectionClosed
    except WebSocketException:
        return "", WebSocketException
