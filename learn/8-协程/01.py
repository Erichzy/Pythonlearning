from aiohttp import web
import asyncio

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')
async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>'% request.match_info['name']
    return web.Response(body=text.encode('utf-s'))
async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', '800...')
    print('server started at http://127.0.0.1:800...')

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
