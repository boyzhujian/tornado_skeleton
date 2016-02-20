import logging
import os

import tornado
import tornado.template
from tornado.options import define, options



# Make filepaths relative to settings.


path = lambda root,*a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

define("port", default=7889, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=True, help="debug mode")
tornado.options.parse_command_line()

MEDIA_ROOT = path(ROOT, 'media')
TEMPLATE_ROOT = path(ROOT, 'templates')

settings = {}
settings['static_path'] = MEDIA_ROOT
settings['cookie_secret'] = "your-cookie-secret"
settings['xsrf_cookies'] = False

settings['template_loader'] = tornado.template.Loader(TEMPLATE_ROOT)

settings['login_url'] = "/login"


if options.config:
    tornado.options.parse_config_file(options.config)
