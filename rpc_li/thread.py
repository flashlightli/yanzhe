# -*- coding: utf-8 -*-
import threading
import queue


class ControlWorker(object):

    def __init__(self):
        self.event = threading.Event()
        self.result = None

    def wait(self, wait_time=None):
        self.event.wait(timeout=wait_time)

    def awake(self, result):
        self.event.set()
        self.result = result

    def get_result(self):
        if not self.event.isSet():
            self.wait()
        else:
            return self.result


class ThreadPool(object):

    def __init__(self):
        self.pool = []
        self.queue = queue.Queue()

    def add_event(self):
        t = threading.Thread(target=self)   #target是要执行的方法
        t.daemon = True
        t.start()
        self.pool.append(t)

    def set_worker(self):
        try:
            while True:
                promise, func = self.queue.get()
                try:
                    result = func()
                except Exception:
                    pass
                promise.add_event(result)
        except:
            pass

