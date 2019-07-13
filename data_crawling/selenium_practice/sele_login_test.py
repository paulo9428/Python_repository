import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

drvPath = '/Users/jade/workspace/python/chromedriver'
driver = webdriver.Chrome(drvPath)
UserId = " "
UserPw = " "

#------------------------------------------------------------- 다음 

driver.get("https://www.daum.net")
time.sleep(2)

ifr = driver.find_element_by_id('loginForm')
driver.switch_to.frame(ifr)

id = driver.find_element_by_id('id')
id.send_keys(UserId)
pw = driver.find_element_by_id('inputPwd')
pw.send_keys(UserPw)
pw.send_keys(Keys.RETURN)

time.sleep(5)                # cf.  driver.implicitly_wait(5)
driver.quit()

# ----------------------------------------------------------- 네이버

driver.get("https://www.naver.com")

time.sleep(1)

driver.find_element_by_class_name('lg_local_btn').click()
print("click big button!!")
time.sleep(1)

id_switch = driver.find_element_by_id('id')
pw_switch = driver.find_element_by_id('pw')


driver.execute_script('document.getElementById("id").value = " "')

driver.execute_script('document.getElementById("pw").value = " "')



time.sleep(0.5)

pw_switch.send_keys(Keys.RETURN)

time.sleep(1)