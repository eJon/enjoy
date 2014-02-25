# -*- coding:utf-8 -*-

__author__ = 'Leo'

import tornado.options
import tornado.web

from tornado.options import options

from game.handler.basehandler import BaseHandler

from utils.db import GameBaseDB
from game.server_manager import ServerManager


CREATE_TICKETS_TABLE_QUERY = '''
CREATE TABLE IF NOT EXISTS `Tickets64_%s` (
  `id` bigint(20) unsigned NOT NULL auto_increment,
  `stub` char(1) NOT NULL default '',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `stub` (`stub`)
) ENGINE=MyISAM AUTO_INCREMENT=%s
'''


class MainHandler(BaseHandler):
    def get(self, *args, **kwargs):
        print "GET MainHandler"
        #REPLACE INTO Tickets64 (stub) VALUES ('a');
        print "execute =", self.db.execute(CREATE_TICKETS_TABLE_QUERY % ('002', '999999'))
        entries = self.db.query("SELECT LAST_INSERT_ID() as ID;")
        print "entries =", entries
        self.write(str(entries))
        #self.finish()

    def post(self, *args, **kwargs):
        #print "POST MainHandler"
        raise tornado.web.HTTPError(404)


class GameApplication(tornado.web.Application):
    db = None
    server = ServerManager()

    def __init__(self):
        self._parse_config()

        handlers = [
            (r"/*", MainHandler),
        ]

        settings = dict(
            debug=True,
        )

        tornado.web.Application.__init__(self, handlers, **settings)

    def _parse_config(self):
        tornado.options.parse_command_line()
        #print options.config, options.port, options.log_file_prefix, options.data
        tornado.options.parse_config_file(options.config)
        #print options.config, options.port, options.log_file_prefix, options.data

    def _load_data(self):
        #TODO:: load data
        pass

    def _init_db_pool(self):
        self.db = GameBaseDB(database=options.database,
                             host=options.db_host,
                             user=options.db_user,
                             password=options.db_password,
                             maxsize=options.db_connect_num)

        self.server.group_id = options.user_group
        pass

    def prepare_application(self):
        #
        self._load_data()

        #
        self._init_db_pool()

