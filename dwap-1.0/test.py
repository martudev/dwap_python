#!/usr/bin/env python3
import signal, os

def h1():
    print("test")

signal.signal(signal.SIGALRM, h1)
signal.alarm(1)
signal.setitimer(h1, 1000)