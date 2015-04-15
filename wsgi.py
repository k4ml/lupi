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

@d("/")
def index(request):
    lua = LuaRuntime(unpack_returned_tuples=True)
    body = lua.eval('''[[
        <h1>hello world</h1>
    ]]''')
    return d.HttpResponse(body)

application = d

if __name__ == "__main__":
    d.main()
