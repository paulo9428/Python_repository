import time
from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")    # or.   options.add_argument("--disable-gpu")
# UserAgent값을 바꿔줍시다!
options.add_argument("user-agent= Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")

driver = webdriver.Chrome('c:/workspace/chromedriver.exe', options=options)
# driver = webdriver.Chrome('/Users/jade/workspace/python/chromedriver', options=options)

driver.implicitly_wait(3)

driver.get("https://www.naver.com")
time.sleep(2)

driver.save_screenshot("bbb.png")   # or.  driver.get_screenshot_as_file('bbb.png')
driver.implicitly_wait(5)
driver.quit()
