from tornado.options import define, options
from views import *
from urls import urls
from sqlalchemy import Column, ForeignKey, Integer, String
import tornado.web
import os
import uuid
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


define('port', default=8000, type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = urls
        settings = dict(
            title=u'Adult Game',
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            xsrf_cookies=True,
            cookie_secret=uuid.uuid4().int,
            debug=True
        )
        super(Application, self).__init__(handlers, **settings)