#!/usr/bin/env python

from pyEventDispatcher.EventDispatcher import EventDispatcher

class cdispatcher:
    def __init__(self):
        pass

    def getEventDispatcher(self):
        self.dispatcher = EventDispatcher()
        return self.dispatcher
