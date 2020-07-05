from selenium import webdriver
#chromedriver = "/usr/local/bin/chromedriver"
#chrome_options = webdriver.ChromeOptions()

"""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=C:\\dev-app2")
driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
"""


class InstaBot:
	def __init__(self):
		self.driver = webdriver.Chrome()
		self.driver.get("https://instagram.com")
		return driver

InstaBot()
