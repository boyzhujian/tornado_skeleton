from handlers.main import *
from handlers.user import *
from handlers.movie import *
from handlers.myjson import *
from handlers.doc import *
from handlers.system import *
from handlers.collectbaiduyun import *

url_patterns = [
    (r"/", indexHandler),
    (r"/login", loginHandler),
    (r"/logout", logoutHandler),
    (r"/signup", signupHandler),
  


]





# ([0-9]+)   (.*)
