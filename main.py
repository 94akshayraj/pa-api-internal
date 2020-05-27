import tornado.ioloop
import tornado.web
from app.router import Application
from tornado import httpserver

if __name__ == "__main__":
    app=httpserver.HTTPServer(Application())
    app.listen(8111)
    print('running on port 8111')
    print('************====****************')
    tornado.ioloop.IOLoop.current().start()
