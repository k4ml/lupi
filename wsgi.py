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
from splash.lua import run_in_sandbox
from splash.lua_runtime import SplashLuaRuntime

from importd import d

CWD = os.path.abspath(os.path.dirname(__file__))
d(
    INSTALLED_APPS=[
        'lupi',
    ]
)

class Request(object):
    def __init__(self, request):
        self.path = request.path
        self.method = request.method
        self.query = request.GET
        self.form = request.POST

    def get_path(self):
        return self.path

@d("/")
def index(request):
    i_request = Request(request)
    lua = LuaRuntime(unpack_returned_tuples=True)
    sandbox = lua.eval("require('sandbox')")
    lua_script = open(os.path.join(CWD, 'test.lua')).read()
    result = sandbox.run('function main(request) ' + lua_script + ' end')
    if result is True:
        body = sandbox.env["main"](i_request)
        return d.HttpResponse(body)

    return d.HttpResponse('Failed')

@d("/scripts/new/")
def new_script(request):
    if request.method == 'POST':
        return "new.html"

application = d

if __name__ == "__main__":
    d.main()
