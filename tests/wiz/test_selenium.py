
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



# instance of Options class allows
# us to configure Headless Chrome
options = Options()

# this parameter tells Chrome that
# it should be run without UI (Headless)
options.headless = True

# initializing webdriver for Chrome with our options
driver = webdriver.Chrome(options=options)

driver.get("file:///Users/chenfei/Downloads/_/253285927@qq.com_w2o/My Notes/随笔/【思考】提高效率.html")

print(driver.page_source)

body = driver.find_element(By.TAG_NAME, "body")

print(body.text)