#!/usr/bin/env python

class EventDispatcher:
    __instance = None

    def __init__(self):
        self.listeners = {}
        if EventDispatcher.__instance:
#            raise EventDispatcher.__instance
            print "IF"
            pass
        else:
            print "ELSE"
            EventDispatcher.__instance = self
#        return EventDispatcher.__instance


    def call_user_func(self, functionName):
        functionName()

#    @staticmethod
#    def getInstance(self):
#        if EventDispatcher.__instance == None:
#            EventDispatcher.__instance = EventDispatcher()
#            print "test"

#        return EventDispatcher.__instance

    def connect(self, name, listener):
        if not self.listeners.has_key(name):
            self.listeners[name] = {}
        self.listeners[name][len(self.listeners[name]) + 1] = listener


    def disconnect(self, name, listener):
        if not self.listeners.has_key(name):
            return False

        for c, l in self.listeners[name]:
            if listener == l:
                del self.listeners[name][c]
            

    def notify(self, event):
        for listener in self.getListeners(event.getName()):
            self.call_user_func(self.getListeners(event.getName())[listener])
        return event
        

    def notifyUntil(self, event):
        for listener in self.getListeners(event.getName()):
            if(self.call_user_func(self.getListeners(event.getName())[listener])):
                event.setProcessed(True)
                break

        return event

    def filter(self, event, value = None):
        for listener in self.getListeners(event.getName()):
            value = call_user_func_array(self.call_user_func(self.getListeners(event.getName())[listener]), {0 : event, 1 : value})
        event.setReturnValue(value)
        return event

    def hasListeners(self, name):
        if not self.listeners.has_key(name):
            self.listeners[name] = {}
        
        return bool(len(self.listeners[name]))


    def getListeners(self, name):
        if not self.listeners.has_key(name):
            return {}
        return self.listeners[name]

