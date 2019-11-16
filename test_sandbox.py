import os
import lupa

from lupa import LuaRuntime
from splash.lua import python2lua

def attr_getter(obj, attr_name):
    allowed_attr = ['method', 'path', 'query', 'form']
    if attr_name in allowed_attr:
        return getattr(obj, attr_name)
    raise AttributeError('not allowed to read %s' % attr_name)

def attr_setter(obj, attr_name):
    raise AttributeError('not allowed to write')

class Request(object):
    def __init__(self):
        self.path = '/'
        self.method = 'GET'
        self.query = {}
        self.form = {}

request = Request()

CWD = os.path.abspath(os.path.dirname(__file__))
lua = LuaRuntime(unpack_returned_tuples=True, attribute_handlers=(attr_getter, attr_setter))
sandbox = lua.eval("require('sandbox')")
#sandbox["allowed_require_names"] = python2lua(
#    lua,
#    {name: True for name in [request]}
#)
lua_script = open(os.path.join(CWD, 'test.lua')).read()
result = sandbox.run('function main(request) ' + lua_script + ' end')
print(result)
print(sandbox.env["main"](request))
