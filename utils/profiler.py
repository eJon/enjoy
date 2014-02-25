__author__ = 'Leo'

import logging
import time

from functools import wraps

def timer(f):
    logger = logging.getLogger("%s.%s" % (f.__module__, f.__name__))
    @wraps(f)
    def wrapper(*a, **kw):
        t0 = time.time()
        r = f(*a, **kw)
        td = time.time() - t0
        logger.info("took %0.2fs" % td)
        return r
    return wrapper

class Stopwatch(object):
    def __init__(self, name='Stopwatch'):
        self.name = name
        self.start = time.time()
        self.ticks = []

    def tick(self, name):
        self.ticks.append((name, time.time()))

    def stop(self):
        self.stop = time.time()

    def summary(self):
        """Return a summary of timing information."""
        self.stop()
        total = self.stop - self.start
        s = "%s duration: %0.2f\n" % (self.name, total)
        prev = ("start", self.start)
        for tick in self.ticks:
            s += ("   %s => %s" % (prev[0], tick[0])).ljust(30) + "... %0.2fs\n" % (tick[1] - prev[1])
            prev = tick
        s += ("   %s => end" % (tick[0])).ljust(30) + "... %0.2fs" % (self.stop - tick[1])
        return s

if __name__ == "__main__":

    @timer
    def test():
        time.sleep(5)

    s = Stopwatch()
    test()
    s.tick("test1")
    test()
    s.tick("test2")
    test()
    print s.summary()