import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

drvPath = 'c:/workspace/chromedriver'
driver = webdriver.Chrome(drvPath)

driver.get("https://www.naver.com")

time.sleep(1)

driver.find_element_by_class_name('lg_local_btn').click()
print("click big button!!")
time.sleep(1)

id_switch = driver.find_element_by_id('id')
pw_switch = driver.find_element_by_id('pw')


driver.execute_script('document.getElementById("id").value = "paulo9428"')

driver.execute_script('document.getElementById("pw").value = "dl014532dl"')



time.sleep(0.5)

pw_switch.send_keys(Keys.RETURN)

time.sleep(1)






