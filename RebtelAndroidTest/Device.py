from builtins import dict

class Device(object):

    global device 
    device = dict()

    def __init__(self, platformName=None, platformVersion=None, udid=None, deviceName=None, app=None, appPackage=None, appActivity=None):
        self._platformName = platformName
        self._platformVersion = platformVersion
        self._udid = udid
        self._deviceName = deviceName
        self._app = app
        self._appPackage = appPackage
        self._appActivity = appActivity


    def setDevice(self, suite, platformName, platformVersion, udid, deviceName, app, appPackage, appActivity):
        device[suite] = Device(platformName, platformVersion, udid, deviceName, app, appPackage, appActivity)


    def getDevice(self, suite):
        return device[suite]