# 使用aiortc和aiohttp的简单服务器，处理WebRTC通信
from aiohttp import web
import aiortc
import json

class Handler(aiortc.RTCPeerConnection):
    async def create_offer(self):
        offer = await super().create_offer()
        return json.dumps(offer)

    async def set_remote_description(self, offer):
        offer = json.loads(offer)
        await super().set_remote_description(aiortc.RTCSessionDescription(**offer))
        # 创建并返回answer
        answer = await self.create_answer()
        return json.dumps(answer)

async def index(request):
    return web.Response(text="WebRTC Server is running")

async def offer(request):
    data = await request.text()
    answer = await Handler().set_remote_description(data)
    return web.Response(text=answer)

app = web.Application()
app.router.add_get('/', index)
app.router.add_post('/offer', offer)

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8000)