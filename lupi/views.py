import os

import lupa
from lupa import LuaRuntime
from splash.lua import run_in_sandbox
from splash.lua_runtime import SplashLuaRuntime

CWD = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CWD, '..'))

class Request(object):
    def __init__(self, request):
        self.path = request.path
        self.method = request.method
        self.query = request.GET
        self.form = request.POST

    def get_path(self):
        return self.path

def index(request):
    i_request = Request(request)
    lua = LuaRuntime(unpack_returned_tuples=True)
    sandbox = lua.eval("""package.path = "../?.lua;" .. package.path; require('sandbox')""")
    lua_script = open(os.path.join(CWD, 'test.lua')).read()
    result = sandbox.run('function main(request) ' + lua_script + ' end')
    if result is True:
        body = sandbox.env["main"](i_request)
        return d.HttpResponse(body)

    return d.HttpResponse('Failed')

def new_script(request):
    if request.method == 'POST':
        return "new.html"
