from handlers.main import *
from handlers.user import *


url_patterns = [
    (r"/", indexHandler),
    (r"/login", loginHandler),
    (r"/logout", logoutHandler),
    (r"/signup", signupHandler),
  


]





# ([0-9]+)   (.*)
