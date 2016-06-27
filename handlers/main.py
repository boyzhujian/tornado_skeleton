
import tornado.web

class indexHandler(tornado.web.RequestHandler):
    def  get(self):
       self.write("Welcome to GDC,cisco general data collector system")


    def  post(self):
        pass

