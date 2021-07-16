#import materials needed for function to work
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#make a driver using webdriver and set it to chrome
driver = webdriver.Chrome()

#get link you plan to use.
driver.get('https://www.linkedin.com/feed/')

#find elements on webpage and eneter and submit some items.
enterText = driver.find_element_by_xpath('/html/body/div[1]/main/form/section/div[2]/input[1]')
enterText.send_keys('xxxxxxxxxxx@gmail.com')
enterText = driver.find_element_by_xpath('/html/body/div[1]/main/form/section/div[2]/input[2]')
enterText.send_keys('XXXXxxXXXxXxxXX')
clickAndContinueButton = driver.find_element_by_xpath('/html/body/div[1]/main/form/section/button')
clickAndContinueButton.click()
enterFirstName = driver.find_element_by_xpath('/html/body/div[1]/main/form/section/div[1]/input[1]')
enterFirstName.send_keys('John ')
enterLastName = driver.find_element_by_xpath('/html/body/div[1]/main/form/section/div[1]/input[2]')
enterLastName.send_keys('Doe')

#THIS WONT WORK BECAUSE OF CSP THAT PREVENTS INJECTION.
#wait for some elements to finish loading.
driver.implicitly_wait(5)

#find elements on webpage and eneter and submit some items.
ClickContinue = driver.find_element_by_xpath('//*[@id="join-form-submit"]')
ClickContinue.click()

#wait for some elements to finish loading.
element = WebDriverWait(driver,10).until(EC.presence_of_element_located(
  (By.XPATH, "/html/body/div[1]/main/section"))).click
phoneNumberWait = driver.find_element_by_xpath('//*[@id="register-verification-phone-number"]')
phoneNumberWait.send_keys('123-456-7891')
