import logging; logging.basicConfig(level=logging.INFO)
import asyncio
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1 color="ff0000">Awesome</h1>')

async def __init(loop):
    app = web.Application(loop=loop)
    app.router.add_route("GET",'/',index)
    server = await loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('please open 127.0.0.1:9000...')
    return server
loop = asyncio.get_event_loop()
loop.run_until_complete(__init(loop))
loop.run_forever()