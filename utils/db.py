# -*- coding:utf-8 -*-
__author__ = 'Leo'

from Queue import Queue
import contextlib

import utils.database


class ConnectionPool(object):
    """A simple connection pool which uses a queue to limit how many
    connections to a single resource are made.  Override the `connection`
    method to make new connections to your resource."""
    def __init__(self, maxsize=10):
        self.maxsize = maxsize
        self.pool = Queue()
        self.size = 0

    def get(self):
        pool = self.pool
        if self.size >= self.maxsize or pool.qsize():
            return pool.get()
        self.size += 1
        try:
            con = self.new_connection()
        except:
            self.size -= 1
            raise
        return con

    def put(self, con):
        self.pool.put(con)

    @contextlib.contextmanager
    def connection(self):
        con = self.get()
        try:
            yield con
        finally:
            self.put(con)

    def new_connection(self, *a, **kw):
        raise NotImplementedError


class MysqlPool(ConnectionPool):
    def __init__(self, database, user, password, host, maxsize):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        super(MysqlPool, self).__init__(maxsize)

    def new_connection(self):
        con = utils.database.Connection(host=self.host,
                                        database=self.database,
                                        user=self.user,
                                        password=self.password)
        return con


class GameBaseDB(object):
    def __init__(self, database, user, password, host, maxsize=10):
        self.pool = MysqlPool(database=database,
                              user=user,
                              password=password,
                              host=host,
                              maxsize=maxsize)
        pass

    def query(self, sql, args=None):
        """Return the results for a query."""
        with self.pool.connection() as c:
            if args:
                return c.query(sql, args)
            return c.query(sql)

    def execute(self, sql, args=None):
        """Executes the given query, returning the lastrowid from the query."""
        with self.pool.connection() as c:
            if args:
                return c.execute(sql, args)
            return c.execute(sql)