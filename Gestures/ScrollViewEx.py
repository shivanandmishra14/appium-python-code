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


driver =webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])

ele = wait.until(lambda  x: x.find_element_by_android_uiautomator('text("ScrollView")'))
ele.click()

wait.until(lambda  x: x.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON12"))')).click()

#driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON12"))').click()
driver.quit()

