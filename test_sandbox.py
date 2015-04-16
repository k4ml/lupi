import os
import lupa

from lupa import LuaRuntime
from splash.lua import python2lua

class Request(object):
    def __init__(self):
        self.path = '/'
        self.method = 'GET'
        self.query = {}
        self.form = {}

request = Request()

CWD = os.path.abspath(os.path.dirname(__file__))
lua = LuaRuntime(unpack_returned_tuples=True)
sandbox = lua.eval("require('sandbox')")
sandbox["allowed_require_names"] = python2lua(
    lua,
    {name: True for name in [request]}
)
lua_script = open(os.path.join(CWD, 'test.lua')).read()
result = sandbox.run('function main(request) ' + lua_script + ' end')
print result
import pdb;pdb.set_trace()
