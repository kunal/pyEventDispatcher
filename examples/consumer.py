#!/usr/bin/env python                                                                        

from pyEventDispatcher.EventDispatcher import EventDispatcher

class Consumer:
    def __init__(self):
        self.dispatcher = EventDispatcher()
        self.dispatcher.connect('uc', self.abc)
        self.dispatcher.connect('ucc', self.pqr)

    def getDispatcher(self):
        return self.dispatcher

    def abc(self):
        print "hmm"

    def pqr(self):
        print "test"




