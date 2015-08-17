from Common import *
from Device import *
import xml.etree.ElementTree as ET


class Program(Device):
    def __init__(self, _config_file):
        writeInfo('Parsing configuration file: ' + _config_file)
        self.conf = ET.parse(_config_file)
        self.cRoot = self.conf.getroot()


    def collectDeviceInfo(self):
        suite = self.cRoot.get('suite')
        platformName = self.cRoot.find('device').get('platformName')
        platformVersion = self.cRoot.find('device').get('platformVersion')
        udid = self.cRoot.find('device').get('udid')
        deviceName = self.cRoot.find('device').get('deviceName')
        app = self.cRoot.find('./device/app').text
        appPackage = self.cRoot.find('./device/appPackage').text
        appActivity = self.cRoot.find('./device/appActivity').text
        ''' Initialize a Device.'''
        Device.setDevice(suite, platformName, platformVersion, udid, deviceName, app, appPackage, appActivity)


    def getSuite(self, _case):
        ''' Returns the suite about to execute. '''
        ''' Add-up more suites here when available. Such as RebteliOSTest. '''
        ## from RebteliOSTest import RebteliOSTest as iSuite ##
        from RebtelAndroidTest import RebtelAndroidTest as aSuite

        if (_case == 'RebtelAndroidTest'):
            return aSuite
        elif (_case == 'RebteliOSTest'):
            ## return iSuite ##
            return None
        ''' and so on ... '''


    def runTest(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(self.getSuite(self.cRoot.get('suite')))
        # unittest.TextTestRunner(verbosity=2).run(suite)
        # Activate the following line in order to have JUnit output. And deactivate the above line please.
        xmlrunner.XMLTestRunner().run(suite)



if __name__ == '__main__':
    p = Program("../test.config")
    p.collectDeviceInfo()
    p.runTest()