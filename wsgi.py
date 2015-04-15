#!/usr/bin/python
import os

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

import lupa
from lupa import LuaRuntime

from importd import d

class Request(object):
    def __init__(self, path, method):
        self.path = path
        self.method = method

    def get_path(self):
        return self.path

@d("/")
def index(request):
    lua = LuaRuntime(unpack_returned_tuples=True)
    lua_script = open('test.lua').read()
    lua_func = lua.eval('function(request) %s end' % lua_script)
    i_request = Request(request.path, request.method)
    body = lua_func(i_request)
    return d.HttpResponse(body)

application = d

if __name__ == "__main__":
    d.main()
