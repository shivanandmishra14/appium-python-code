from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'IOS'
desired_caps['platformVersion'] = '14.1'
desired_caps['deviceName'] = 'iPhone 11 Pro'
desired_caps['automationName'] = 'XCUITest'
desired_caps['app'] = (
    '/Users/shivanandmishra/Documents/PythonLearning/AppiumSeleniumLearning/IOSAutomation/IOS_App/UICatalog.app')
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
original_ele = driver.find_element_by_accessibility_id("AAPLAlertViewController")
destination_ele = driver.find_element_by_accessibility_id("AAPLWebViewController")

driver.scroll(original_ele, destination_ele)

destination_ele.click()
