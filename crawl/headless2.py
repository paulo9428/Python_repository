import time
from selenium import webdriver

TEST_URL = 'https://intoli.com/blog/making-chrome-headless-undetectable/chrome-headless-test.html'

options = webdriver.ChromeOptions()
options.add_argument('headless')
#options.add_argument('window-size=1920x1080')

options.add_argument("disable-gpu")
#options.add_argument("--disable-gpu")

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
options.add_argument("lang=ko_KR")

driver = webdriver.Chrome('C:/workspace/chromedriver.exe', options=options)

driver.get('about:blank')
driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")
driver.get(TEST_URL)
#time.sleep(2)

user_agent = driver.find_element_by_css_selector('#user-agent').text
plugins_length = driver.find_element_by_css_selector('#plugins-length').text

print('User-Agent: ', user_agent)
print('Plugin length: ', plugins_length)

driver.save_screenshot("ccc.png")
#driver.get_screenshot_as_file('bbb.png')
print(driver.title)

#driver.implicitly_wait(5)
driver.quit()
