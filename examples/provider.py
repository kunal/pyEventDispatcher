#!/usr/bin/env python

from pyEventDispatcher.Event import Event
from pyEventDispatcher.EventDispatcher import EventDispatcher
from consumer import Consumer

class Main():
    def __init__(self):
        dispatcher = EventDispatcher()
        print dispatcher

        self.event = Event(self, 'ucc', {})
        dispatcher.notify(self.event)
        self.event = Event(self, 'uc', {})
        dispatcher.notify(self.event)

    def getEvent(self):
        return self.event

if __name__ == '__main__':
    c = Main()


#dispatcher.notify(event)
