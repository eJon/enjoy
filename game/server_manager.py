# -*- coding:utf-8 -*-

__author__ = 'Leo'


class ServerManager(object):

    def __init__(self):
        self._group_id = None
        pass

    @property
    def group_id(self):
        """
        @return group_id string id
        """
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value

    pass