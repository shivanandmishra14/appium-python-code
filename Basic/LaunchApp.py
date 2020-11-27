from appium import webdriver

def tap():
    """
    Perform  click on webElement
    :param: None
    :return: webElement
    """
    return "I have clicked on the elements"

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'uiautomator2'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['app'] = '/Users/shivanandmishra/Documents/PythonAutomation/mobile_test_python/app/simplilearn.apk'
driver= webdriver.Remote("http://localhost:4723/wd/hub", desired_caps )
ele_id = driver.find_element_by_id("com.mobile.simplilearn:id/btn_onb_explore_courses")
ele_id.click()
#ele_id.tap= tap
#ele_id.tap






