# -*- coding:utf-8 -*-

__author__ = 'Leo'

import tornado
from tornado.web import RequestHandler


class BaseHandler(tornado.web.RequestHandler):
    """ Common functionality for all handlers """
    @property
    def db(self):
        return self.application.db

    @property
    def server(self):
        """
        @return server manager Object:
        """
        return self.application.server

