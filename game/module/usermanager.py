# -*- coding:utf-8 -*-

__author__ = 'Leo'

from game.module.basemodule import BaseModule


class UserManager(BaseModule):
    def __init__(self, db, server):
        super(UserManager, self).__init__(db, server)

    def generate_new_userid(self):
        """
        REPLACE INTO Tickets64_%s (stub) VALUES ('a')
        @return user_id:
        """
        return self.db.execute("REPLACE INTO Tickets64_%s (stub) VALUES ('a')" % self.server.group_id)