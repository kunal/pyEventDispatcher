#!/usr/bin/env python

from pyEventDispatcher.EventDispatcher import EventDispatcher

class dispatcher():
    def __init__(self):
        pass

    def getEventDispatcher(self):
        self.dispatcherObj = EventDispatcher()
        return self.dispatcherObj
