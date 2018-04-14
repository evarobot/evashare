#!/usr/bin/env python
# encoding: utf-8

from threading import Timer
import threading


class RepeatedTimer(object):
    """
    Added by Wells
    """
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False

    def _run(self):
        self.is_running = False
        self.run()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


class TimerThread(threading.Thread):
    """Thread that executes a task every N seconds
    Added by Wells
    """

    def __init__(self, interval, function, *args, **kwargs):
        threading.Thread.__init__(self)
        self._finished = threading.Event()
        self._interval = interval
        self._function = function
        self._args = args
        self._kwargs = kwargs
        self.daemon = True

    def setInterval(self, interval):
        """Set the number of seconds we sleep between executing our task"""
        self._interval = interval

    def stop(self):
        """Stop this thread"""
        self._finished.set()

    def run(self):
        """
        If you don't want to block the main thread, you can invoke `start()` instead.
        """
        while True:
            if self._finished.isSet():
                return
            self._function(*self._args, **self._kwargs)
            # sleep for interval or until shutdown
            self._finished.wait(self._interval)


if __name__ == '__main__':
    from time import sleep

    def hello(name):
        print "Hello %s!" % name
    print "starting..."
    #rt = RepeatedTimer(1, hello, "World")
    rt = TimerThread(1, hello, "World")
    rt.start()
    print "main thread"
    sleep(3)
    rt.stop()
