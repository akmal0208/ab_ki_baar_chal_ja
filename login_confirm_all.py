from sys_config import *
import time
from selenium.webdriver.common.keys import Keys
from keys import *

driver = webdriver.Chrome(path,chrome_options = chrome_options)
driver.get('http://www.facebook.com/login')

time.sleep(1)

driver.find_element_by_name("email").send_keys(username)
time.sleep(1)

driver.find_element_by_xpath("//input[@name= 'pass']").send_keys(password)
time.sleep(1)

driver.find_element_by_name("login").click()

# requests = driver.find_element_by_name('requests')
# requests.click()

# time.sleep(3)
# accept = driver.find_elements_by_name('actions[accept]')
# for i in accept:
# 	accept[0].send_keys(Keys.END)

# print('number of reqs:',len(accept))


## IT CONTAINS CONFIRM BUTTONS AND THEN SEND REQUEST BUTTONS ALSO
## SHOWS RECENT 50 IN CONFIRM
## RUN MULTIPLE TIMES (LOOP) TO ACCEPT ALL AND SEND TO MANY
# print(len(confirm_button_list))
time.sleep(1)
counter = 0
for i in range(0,3):
	driver.get('https://www.facebook.com/friends/requests/?fcref=jwl')
	time.sleep(3)
# confirm_button_list = driver.find_elements_by_link_text('Confirm')
	confirm_button_list = driver.find_elements_by_css_selector('._42ft._4jy0._4jy3._4jy1.selected._51sy')
	
	for i in confirm_button_list:
		try:
			i.click()
			time.sleep(0.2) # too fast otherwise 
			counter += 1
		except Exception as e:
			print('ERROR:',e,'probably element not visible')
	print('clicked',counter,'buttons')
	# driver.refresh()