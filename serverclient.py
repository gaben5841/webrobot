import websockets
import asyncio
import io
from threading import Condition


async def hello():
    uri = "ws://192.168.7.85:3030"
    async with websockets.connect(uri) as websocket:
        message = input("What would you like to send to the server? ")
        await websocket.send(message)
        #await websocket.send
        response = await websocket.recv()
        print(response)

class streamer(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

asyncio.get_event_loop().run_until_complete(hello())
