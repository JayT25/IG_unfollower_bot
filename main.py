from selenium import webdriver
from time import sleep

# from secrets.py import the function pw.
# pw prints the password for the IG account
from secrets import pw as passwrd

#chromedriver = "/usr/local/bin/chromedriver"
#chrome_options = webdriver.ChromeOptions()

"""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=C:\\dev-app2")
driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
"""


class InstaBot:
	def __init__(self, username, password):
		self.driver = webdriver.Chrome()
		self.driver.get("https://instagram.com")
		# wait 2 secs
		sleep(2)
		
		# find username box, then send username credentials
		#
		# to find input type for the username and password box
		# simply right click the username or password box and select
		# inspect. right click body tag, expand.
		#
		#find identifiers for username, password and login

		self.driver.find_element_by_xpath('//input[@name=\"username\"]')\
		.send_keys(username)

		# find password box, then send pass credentials
		self.driver.find_element_by_xpath('//input[@name=\"password\"]')\
		.send_keys(password)

		# find log in button, click it
		self.driver.find_element_by_xpath('//button[@type="submit"]')\
		.click()
		# successfully logged in

		# wait 4 secs
		sleep(4)
		return driver

# instagram username: TestSB_1
InstaBot('TestSB_1',passwrd() )
