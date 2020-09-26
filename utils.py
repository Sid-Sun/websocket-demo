import websockets


async def get_msg(ws: websockets.WebSocketServerProtocol) -> (websockets.Data, websockets.WebSocketException):
    try:
        msg = await ws.recv()
        return msg, None
    except websockets.ConnectionClosed:
        return "", websockets.ConnectionClosed
    except websockets.WebSocketException:
        return "", websockets.WebSocketException
