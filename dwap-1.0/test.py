#!/usr/bin/env python3	
from threading import Thread, Event
from multiprocessing import Process
import time
 
 
# Event object used to send signals from one thread to another
stop_event = Event()
action_thread = None
 
def timer():
    while True:
        time.sleep(1)
 
def timeout(seconds, callback):
    # We create another Thread
    action_thread = Process(target=timer)
 
    # Here we start the thread and we wait 5 seconds before the code continues to execute.
    action_thread.start()
    action_thread.join(timeout=seconds)

    # We send a signal that the other thread should stop.
    action_thread.terminate()
 
    callback("hola")
 
if __name__ == '__main__':
    timeout(seconds=0.5, callback=print)