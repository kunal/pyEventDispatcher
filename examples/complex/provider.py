#!/usr/bin/env python

from pyEventDispatcher.Event import Event
from pyEventDispatcher.EventDispatcher import EventDispatcher

from consumer import Consumer
from dispatcher import dispatcher

class Main():
    def __init__(self):
        self.dispatcherObj = dispatcher()
        self.dispatcher = self.dispatcherObj.getEventDispatcher()

        self.event = Event(self, 'ucc', {})
        self.dispatcher.notify(self.event)
        self.event = Event(self, 'uc', {})
        self.dispatcher.notify(self.event)

    def getEvent(self):
        return self.event

if __name__ == '__main__':
    c = Main()


#dispatcher.notify(event)
