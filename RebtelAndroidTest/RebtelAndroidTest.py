from Common import *
from Device import *
from appium import webdriver


class RebtelAndroidTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        writeInfo('Setting up device ...')
        try:
            desired_caps = dict()
            desired_caps['platformName'] = device._platformName
            desired_caps['platformVersion'] = device._platformVersion
            desired_caps['udid'] = device._udid
            desired_caps['deviceName'] = device._deviceName
            ''' The absolute local path or remote http URL to an .ipa or .apk file. '''
            desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'app/' + device._app))
            desired_caps['appPackage'] = device._appPackage
            desired_caps['appActivity'] = device._appActivity
            ''' ToDo: collect appiumHost & appiumPort from config. '''
            host = 'localhost'
            port = '4723'
            self.driver = webdriver.Remote('http://'+ host +':'+ port +'/wd/hub', desired_caps)
        except:
            writeInfo('Failed to Setup device!')
            traceback.print_exc()
            raise


    @classmethod
    def tearDownClass(self):
        writeInfo('Shutting down Rebtel ...')
        try:
            self.driver.quit()
        except:
            writeInfo('Failed to shut down Rebtel!')
            traceback.print_exc()
            raise


    def setUp(self):
        writeInfo('Logging in ...')
        try:
            el = self.driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.rebtel.android:id/loginFlowButton']")
            el.click()
            time.sleep(3)
            el = self.driver.find_element_by_xpath("//android.widget.Spinner[@resource-id='com.rebtel.android:id/countrySpinner']")
            el.click()
            time.sleep(3)
            el0 = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Argentina (+54)']")
            el1 = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Ascension (+247)']")
            self.driver.scroll(el1, el0)
            time.sleep(3)
            el = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Bangladesh (+880)']")
            el.click()
            time.sleep(3)
            el = self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.rebtel.android:id/loginPhoneNumber']")
            el.send_keys("1713185052")
            el = self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.rebtel.android:id/loginEnterPin']")
            el.send_keys("3987")
            el = self.driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.rebtel.android:id/btnLoginFragmentNext']")
            el.click()
            time.sleep(10)
        except:
            writeInfo('Failed to Log in!')
            traceback.print_exc()
            raise


    def tearDown(self):
        writeInfo('Logging out ...')
        try:
            el = self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Open navigation drawer']")
            el.click()
            time.sleep(3)
            el = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Account']")
            el.click()
            time.sleep(3)
            el = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Log Out']")
            el.click()
            time.sleep(3)
            el = self.driver.find_element_by_xpath("//android.widget.Button[@text='OK']")
            el.click()
        except:
            writeInfo('Failed to Log out!')
            traceback.print_exc()
            raise


    def nevigateTo(self, label):
        writeInfo('Navigating to '+ label +' ...')
        try:
            el = self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Open navigation drawer']")
            el.click()
            time.sleep(3)
            el = self.driver.find_element_by_xpath("//android.widget.TextView[@text='"+ label +"']")
            el.click()
            time.sleep(3)
        except:
            writeInfo('Failed to Navigate!')
            traceback.print_exc()
            raise


    def dialDigit(self, digit):
        try:
            el = self.driver.find_element_by_xpath("//android.widget.TextView[@text='"+ digit +"']")
            el.click()
        except:
            writeInfo('Failed to Dial '+ digit +'!')
            traceback.print_exc()
            raise


    def test_RecentMenu(self):
        writeInfo('Running test_RecentMenu ...')

        self.nevigateTo('Dial Pad')

        writeInfo('Dialing phone number ...')
        digits = ['0', '1', '7', '1', '7', '3', '7', '9', '4', '8', '0']
        for each in digits:
            self.dialDigit(each)

        writeInfo('Call ...')
        el = self.driver.find_element_by_xpath("//android.widget.ImageButton[@resource-id='com.rebtel.android:id/button14']")
        el.click()
        time.sleep(1)
        el = self.driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.rebtel.android:id/next_button']")
        el.click()
        time.sleep(1)

        writeInfo('Hang up ...')
        el = self.driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.rebtel.android:id/hangupButton']")
        el.click()
        time.sleep(3)

        self.nevigateTo('Recent')

        writeInfo('Verifying the call in Recent menu ...')
        try:
            el = self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.rebtel.android:id/phoneNumber']")
            phoneNumber = el.text
        except:
            phoneNumber = None
        self.assertEqual(phoneNumber, '+8801717379480', "Dialed phone number doesn't exist in the Recent menu!")


if __name__ == 'RebtelAndroidTest':
    ''' Recruit the intended device to run at. '''
    d = Device()
    device = d.getDevice('RebtelAndroidTest')