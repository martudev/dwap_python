#!/usr/bin/env python3	
from threading import Thread, Event
from multiprocessing import Process
import time
 
 
# Event object used to send signals from one thread to another
stop_event = Event()
 
def get(varsss):
    return "test " + varsss
 
def do_actions(a):
    """
    Function that should timeout after 5 seconds. It simply prints a number and waits 1 second.
    :return:
    """
    i = 0
    while True:
        i += 1
        print(a + " / ")
        time.sleep(1)
 
        # Here we make the check if the other thread sent a signal to stop execution.
        if stop_event.is_set():
            break
 
def timeout(seconds, callback):
    # We create another Thread
    q = get("holi")
    action_thread = Process(target=do_actions, args=(q,))
 
    # Here we start the thread and we wait 5 seconds before the code continues to execute.
    action_thread.start()
    action_thread.join(timeout=seconds)
 
    # We send a signal that the other thread should stop.
    action_thread.terminate()
 
    callback("hola")
 
if __name__ == '__main__':
    timeout(seconds=5, callback=print)