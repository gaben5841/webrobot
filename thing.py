import io
from picamera import PiCamera
import logging
import websockets
import base64
import numpy
from threading import Condition
import time
import contextlib
import anyio
from anyio import to_thread, from_thread

uri = "ws://192.168.7.85:3030"


@contextlib.asynccontextmanager
async def capture_continuous():

    tx, rx = anyio.create_memory_object_stream()

    def _capture():
        with PiCamera() as camera:
            camera.resolution = (640, 480)
            camera.framerate = 15
            stream = io.BytesIO()
            for frame in camera.capture_continuous(
                stream, format="jpeg", use_video_port=True
            ):
                from_thread.run(tx.send, (frame, stream.getvalue()))
                stream.seek(0)

    async def _acapture():
        async with tx:
            await to_thread.run_sync(_capture)

    async with anyio.create_task_group() as tg, rx:
        tg.start_soon(_acapture)
        yield rx


async def socketSend(ws):
    async with capture_continuous() as agen:
        with anyio.move_on_after(20):
            async for frame, msg in agen:
                print("sending message")
                await ws.send(msg)
                print("waiting for response")
                print(await ws.recv())


async def amain():
    async with await websockets.connect(uri) as ws:
        await socketSend(ws)
    return 0


def main():
    return anyio.run(amain)


if __name__ == "__main__":
    sys.exit(main())
