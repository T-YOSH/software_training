from detector import AbstractGreeting


class SensorGreeting(AbstractGreeting):
    rawData = None
    def setRawData(self, data):
        rawData = data
    def showRawData(self):
        return 'currenct data is ( %s ) from Sensor ' % rawData
    