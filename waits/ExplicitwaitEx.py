from appium import  webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Xiaomi'
desired_caps['app'] = ('/Users/shivanandmishra/Documents/PythonLearning/AppiumSeleniumLearning/app/DemoApp.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

#list of Selenium Exceptions
#https://www.selenium.dev/selenium/docs/api/py/common/selenium.common.exceptions.html
wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])

#ele = wait.until(lambda  x: x.find_element_by_id("com.code2lead.kwad:id/EnterValue"))
#ele.click()

#ele = wait.until(lambda  x: x.find_element_by_class_name("android.widget.EditText")).send_keys("Code2Lead")
#ele = wait.until(lambda  x: x.find_element_by_android_uiautomator('UiSelector().description("Btn3")'))
ele = wait.until(lambda  x: x.find_element_by_android_uiautomator('text("ENTER SOME VALUE")'))
ele.click()

time.sleep(4000)
driver.quit()

