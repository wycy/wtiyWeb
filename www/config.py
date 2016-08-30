#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Configuration
'''

__author__ = 'Michael Liao'
import orm
from DBModel import User, Blog, Comment
import asyncio
import sys

import config_default

class Dict(dict):
    '''
    Simple dict but support access as x.y style.
    '''
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

def merge(defaults, override):
    r = {}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r

def toDict(d):
    D = Dict()
    for k, v in d.items():
        D[k] = toDict(v) if isinstance(v, dict) else v
    return D

configs = config_default.configs

try:
    import config_override
    configs = merge(configs, config_override.configs)
except ImportError:
    pass


# 测试，使用config读取配置信息

async  def test(loop,configs):
    await orm.create_pool(loop=loop,user=configs['user'], password=configs['password'], db=configs['db'])
    users = await User.findAll()
    return users


configs  = toDict(configs)
loop=asyncio.get_event_loop()
users = loop.run_until_complete(test(loop,configs['db']))
print(users)
loop.close()
if loop.is_closed():
    sys.exit(0)