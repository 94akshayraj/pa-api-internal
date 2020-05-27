import os.path
import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from app.controller.fpgrowth import FPGrowthController
from app.controller.vec import VecController
from tornado.options import define, options



class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/fp",FPGrowthController),
            (r"/vec",VecController)
        ]
        tornado.web.Application.__init__(self, handlers,debug=True,autoreload=True)

