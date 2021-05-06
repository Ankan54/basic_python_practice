"""
script to automatically fil up a web form and open in Chrome
Author: Ankan Bera

prerequisite:
install selenium
install webdriver_manager
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

contact_info = {'user_name': "AnkanBera",
                'password': '1234',
                'email':'ankan.ber@email.com',
                'phone': '1234567890',
                }

browser= webdriver.Chrome(ChromeDriverManager().install())   # to get the latest ChromeDriver

browser.get('signup.html') # replace form link with full path, here given sample form

time.sleep(2)   # to give browser some time to render the HTML page

user_name= browser.find_element_by_xpath('/html/body/center/form/table/tbody/tr[1]/td[2]/input')
email = browser.find_element_by_xpath('/html/body/center/form/table/tbody/tr[2]/td[2]/input')
phn_number = browser.find_element_by_xpath('/html/body/center/form/table/tbody/tr[3]/td[2]/input')
password = browser.find_element_by_xpath('/html/body/center/form/table/tbody/tr[4]/td[2]/input')
conf_pwd = browser.find_element_by_xpath('/html/body/center/form/table/tbody/tr[5]/td[2]/input')

user_name.send_keys(contact_info['user_name'])
email.send_keys(contact_info['email'])
phn_number.send_keys(contact_info['phone'])
password.send_keys(contact_info['password'])
conf_pwd.send_keys(contact_info['password'])
