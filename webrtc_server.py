from aiohttp import web
import aiortc
from aiortc import RTCPeerConnection
import json
import os

class Handler(RTCPeerConnection):
    async def create_offer(self):
        offer = await super().create_offer()
        return json.dumps(offer)

    async def set_remote_description(self, offer):
        offer = json.loads(offer)
        await super().set_remote_description(aiortc.RTCSessionDescription(**offer))
        # 创建并返回answer
        answer = await self.create_answer()
        return json.dumps(answer)

    async def on_track(self, track):
        if track.kind == "audio":
            while True:
                frame = await track.recv()
                # 在这里处理音频帧
                # 例如，保存到文件或进行实时分析

async def index(request):
    return web.FileResponse('index.html')

async def offer(request):
    data = await request.text()
    handler = Handler()
    answer = await handler.set_remote_description(data)
    return web.Response(text=answer)

app = web.Application()
app.router.add_get('/', index)
app.router.add_post('/offer', offer)

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8000)
