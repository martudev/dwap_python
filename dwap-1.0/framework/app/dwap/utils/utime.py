#!/usr/bin/env python3
from threading import Thread, Event
import time


stop_it_global = Event()

def stop(stop_it):
    if stop_it is not None:
        stop_it.set()


def timer(seconds, stop_it, callback, args):
    i = 0
    while True:
        i += 1
        time.sleep(seconds)
        callback(*args)

        if stop_it is not None:
            if stop_it.is_set():
                break


def timeout(seconds, repeat, callback, args):
    # We create another Thread and Event
    stop_it = None
    if repeat == True:
        stop_it = Event()
        action_thread = Thread(target=timer, args=(seconds, stop_it, callback, args,))
        action_thread.start()
    else:
        action_thread = Thread(target=timer, args=(seconds, stop_it_global, callback, args,))
        action_thread.start()
        action_thread.join(timeout=seconds)
        stop_it_global.set()
    return stop_it


# Example
# t1 = timeout(seconds=1, repeat=True, callback=print, args=("first", "seccond",))
# t2 = timeout(seconds=3, repeat=False, callback=test, args=("first", "seccond",))
# stop(t2)  # --> stops thread 2 in this case
