#!/usr/bin/env python
# encoding: utf-8

from threading import Timer, Event, Thread
import threading
import time


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


def TimerReset(*args, **kwargs):
    """ Global function for Timer """
    return _TimerReset(*args, **kwargs)


class _TimerReset(Thread):
    """Call a function after a specified number of seconds:

    t = TimerReset(30.0, f, args=[], kwargs={})
    t.start()
    t.cancel() # stop the timer's action if it's still waiting
    """

    def __init__(self, owner, interval, function, args=[], kwargs={}):
        Thread.__init__(self)
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.owner = owner
        self.finished = Event()
        self.resetted = True

    def cancel(self):
        """Stop the timer if it hasn't finished yet"""
        self.finished.set()

    def run(self):
        while self.resetted:
            self.resetted = False
            self.finished.wait(self.interval)

        if not self.finished.isSet():
            self.function(*self.args, **self.kwargs)
        self.finished.set()

    def reset(self, interval=None):
        """ Reset the timer """

        if interval:
            self.interval = interval

        self.resetted = True
        self.finished.set()
        self.finished.clear()


def test_timer_reset():
    def hello():
        print("Time: {0} - hello, world".format(time.asctime()))

    # No reset
    print("Time: {0} - start...".format(time.asctime()))
    tim = TimerReset("test", 5, hello)
    tim.start()
    print("Time: %s - sleeping for 10..." % time.asctime())
    time.sleep(10)
    print("Time: %s - end..." % time.asctime())

    print("\n\n")

    # With Reset
    print("Time: %s - start..." % time.asctime())
    tim = TimerReset("test", 5, hello)
    tim.start()
    print("Time: %s - sleeping for 4..." % time.asctime())
    time.sleep(4)
    tim.reset()
    print("Time: %s - sleeping for 10..." % time.asctime())
    time.sleep(10)
    print("Time: %s - end..." % time.asctime())

    print("\n\n")

    # With reset interval
    print("Time: %s - start..." % time.asctime())
    tim = TimerReset("test", 5, hello)
    tim.start()
    print("Time: %s - sleeping for 4..." % time.asctime())
    time.sleep(4)
    tim.reset(9)
    print("Time: %s - sleeping for 10..." % time.asctime())
    time.sleep(10)
    print("Time: %s - end..." % time.asctime())


if __name__ == '__main__':
    from time import sleep

    def hello(name):
        print("Hello %s!" % name)
    print("starting...")
    # rt = RepeatedTimer(1, hello, "World")
    rt = TimerThread(1, hello, "World")
    rt.start()
    print("main thread")
    sleep(3)
    rt.stop()
