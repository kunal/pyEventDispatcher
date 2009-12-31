#! /usr/bin/env python

class Event:

    def __init__(self, subject = None, name = '', parameters = None):
        self.subject = subject
        self.name = name
        self.parameters = parameters
        
        self.value = None
        self.processed = False

    def getSubject(self):
        return self.subject

    def getName(self):
        return self.name

    def setReturnValue(self, value = None):
        self.value = value

    def getReturnValue(self):
        return self.value

    def setProcessed(self, processed = False):
        self.processed = processed

    def isProcessed(self):
        return self.processed

    def getParameters(self):
        return self.parameters

    def offsetExists(self, name):
        return self.parameters.has_key(name)

    def offsetGet(self, name):
        if not self.parameters.has_key(name):
            raise KeyError(name)
        return self.parameters[name]

    def offsetSet(self, name, value):
        self.parameters[name] = value

    def offsetUnset(self, name):
        del parameters[name]

#if __name__ == "__main__":
#    evt = Event("A", "Kunal", "AA")
