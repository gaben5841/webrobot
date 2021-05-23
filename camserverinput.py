from io import BytesIO
from picamera import PiCamera
import threading
import logging
import websockets
import base64
import asyncio
#import cv2 as cv
import numpy
from threading import Condition
import time

uri = "ws://192.168.7.85:3030"
my_stream = BytesIO()
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 15
msg = ""

async def recieveMsg(ws):
    print('waiting for response')
    msg = await ws.recv()
    await msg
    print(msg)

async def socketSend(ws, message):
    for foo in camera.capture_continuous(my_stream, format = 'jpeg', use_video_port=True):
        await ws.send(message.getvalue())
        print('sending message')
        asyncio.create_task(recieveMsg(ws))
        my_stream.seek(0)
        if time.time() - start > 20:
            break
        my_stream.seek(0)
        my_stream.truncate()

start = time.time()

loop = asyncio.get_event_loop()

async def main() :
    ws = await websockets.connect(uri)
    
    sender = asyncio.create_task(socketSend(ws, my_stream))
    await sender
        
loop.run_until_complete(main())
