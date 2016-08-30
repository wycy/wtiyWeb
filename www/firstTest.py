import orm
from DBModel import User, Blog, Comment
import asyncio
import sys


async  def test(loop):
    await orm.create_pool(loop=loop,user='root', password='wtiy', db='wtiy')

    u = User(name='Test', email='test2w24342312aaasas@example.com', passwd='1234567890', image='about:blank')

    await u.save()

loop=asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
    sys.exit(0)