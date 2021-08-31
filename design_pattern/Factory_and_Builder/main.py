from cameraDetector import CameraGreeting
from sensorDetector import SensorGreeting

CameraGreeting().setRawData('808088ddsafhdjksac')
SensorGreeting().setRawData('hvanmcklsapfuufdsa')

print(CameraGreeting().showRawData())
print(SensorGreeting().showRawData())