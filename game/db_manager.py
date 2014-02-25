# -*- coding:utf-8 -*-
__author__ = 'Leo'

from utils.db import GameBaseDB

CREATE_TICKETS_TABLE_QUERY = '''
CREATE TABLE IF NOT EXISTS `Tickets64_%s` (
  `id` bigint(20) unsigned NOT NULL auto_increment,
  `stub` char(1) NOT NULL default '',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `stub` (`stub`)
) ENGINE=MyISAM AUTO_INCREMENT=%s
'''


class GameDB(GameBaseDB):
    def __init__(self, database, user, password, host, maxsize=10):
        super(GameDB, self).__init__(database, user, password, host, maxsize)

    def setup(self):
        pass