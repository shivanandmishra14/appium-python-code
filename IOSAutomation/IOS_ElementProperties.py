from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'IOS'
desired_caps['platformVersion'] = '14.1'
desired_caps['deviceName'] = 'iPhone 11 Pro'
desired_caps['automationName'] = 'XCUITest'
desired_caps['app'] = ('/Users/shivanandmishra/Documents/PythonLearning/AppiumSeleniumLearning/IOSAutomation/IOS_App/UICatalog.app') 

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

element = driver.find_element_by_accessibility_id("AAPLDatePickerController") # Accessibility ID

print("Is Displayed : ",element.is_displayed())
print("Is Enabled : ",element.is_enabled())
print("Is selected : ",element.is_selected())
print("Size : ",element.size)
print("Location : ",element.location)