from abc import ABCMeta, abstractmethod

class AbstractGreeting(metaclass=ABCMeta):
    @abstractmethod
    def setRawData(self, data):
        pass
    def showRawData(self):
        pass
    def getStatus(self):
        pass
    def sendData(self, api):
        pass