# -*- coding:utf-8 -*-
#!/usr/bin/env python

__author__ = 'Leo'

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

from game.game_server import GameApplication


define("port", default=8000, type=int, metavar="SERVER PORT", help="Run on the given port")
define("config", default="conf/server.conf", type=str, metavar="CONFIG FILE", help="Server configuration file")
define("data", default="./data/default", type=str, metavar="DATA FILE", help="Server data file")
define("user_group", type=str, metavar="USER GROUP", help="User Group")

# database config
define("database", default="", type=str, metavar="DATABASE", help="Server database")
define("db_host", default="127.0.0.1", type=str, metavar="HOST", help="Server database host")
define("db_user", default="root", type=str, metavar="USER", help="Server database user")
define("db_password", default="123456", type=str, metavar="PASSWORD", help="Server database password")
define("db_connect_num", default=5, type=int, metavar="NUM", help="Connect DB Number")


def main():

    app = GameApplication()
    app.prepare_application()

    print "Running ..."

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()

