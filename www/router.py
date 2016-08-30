__author__ = 'Michael Liao'

' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from weburl import get, post

from DBModel import User, Comment, Blog, next_id

@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'index.html',
        'users': users
    }