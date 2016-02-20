#!/usr/bin/env python

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options
import logging

from settings import settings
from urls import url_patterns

class TornadoBoilerplate(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)


def main():
    app = TornadoBoilerplate()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    logging.info("listening on port:"+str(options.port))
    print "http://127.0.0.1:7889"
    tornado.ioloop.IOLoop.instance().start()




if __name__ == "__main__":
     main()
