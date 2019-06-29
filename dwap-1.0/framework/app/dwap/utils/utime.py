#!/usr/bin/env python3
from threading import Thread, Event
import time
import sys


stop_it_global = Event()

def stop(stop_it):
    if stop_it is not None:
        stop_it.set()


def timer(seconds, stop_it, callback, args):
    try:
        i = 0
        while True:
            i += 1
            time.sleep(seconds)
            callback(*args)

            if stop_it is not None:
                if stop_it.is_set():
                    break
    except:
        print('\nProgram stoped...')
        sys.exit(0)


def timeout(seconds, repeat, callback, args, **kwards):
    # We create another Thread and Event
    try:
        stop_it = None
        if repeat == True:
            stop_it = Event()
            action_thread = Thread() #target=timer, args=(seconds, stop_it, callback, args,)
            action_thread.start()
            while True: 
                time.sleep(seconds)
                callback(*args)
        else:
            action_thread = Thread(target=timer, args=(seconds, stop_it_global, callback, args,))
            action_thread.start()
            action_thread.join(timeout=seconds)
            stop_it_global.set()
        return stop_it
    except KeyboardInterrupt:
        message_to_print = kwards.get('im', None)
        if message_to_print is not None:
            print('\n' + message_to_print)
            sys.exit(0)
        else:
            print('\nProgram stoped...aa')
            sys.exit(0)


# Example
# t1 = timeout(seconds=1, repeat=True, callback=print, args=("first", "seccond",))
# t2 = timeout(seconds=3, repeat=False, callback=test, args=("first", "seccond",))
# t3 = timeout(seconds=1, repeat=True, callback=test, args=("first", "seccond",), im='ej: Program stop.')
# stop(t2)  # --> stops thread 2 in this case
