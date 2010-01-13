#!/usr/bin/env python

from pyEventDispatcher.EventDispatcher import EventDispatcher

import dispatcher

class Consumer:
    def __init__(self):
        self.dispatcherObj = dispatcher()
        self.dispatcher = dispatcherObj.getEventDispatcher()
        self.dispatcher.connect('uc', self.abc)
        self.dispatcher.connect('ucc', self.pqr)

    def getDispatcher(self):
        return self.dispatcher

    def abc(self):
        print "hmm"

    def pqr(self):
        print "test"
