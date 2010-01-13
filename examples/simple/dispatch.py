#!/usr/bin/env python

from pyEventDispatcher.EventDispatcher import EventDispatcher
from pyEventDispatcher.Event import Event

def abc():
    print "hmm"

def pqr():
    print "test"

dispatcher = EventDispatcher()
event = Event(None, 'ucc', {})

print "Event parameters are: ", event.getParameters()
dispatcher.connect('ucc', abc)
dispatcher.connect('ucc', pqr)

dispatcher.notify(event)

#print ret.getReturnValue()
