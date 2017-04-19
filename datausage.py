from getpass import getpass
from bs4 import BeautifulSoup
from selenium import webdriver
import time
user=input("Enter your Netid")
pwd=getpass("Enter you password")


driver=webdriver.PhantomJS(executable_path="C:\Program Files\phantomjs.exe")
driver.get("http://myaccount.snu.edu.in/login.php")

username=driver.find_element_by_id("snuNetId")
password=driver.find_element_by_id("password")

username.send_keys(user)
password.send_keys(pwd)

driver.find_element_by_id("submit").click()


time.sleep(3)


start=driver.find_element_by_id("startDate")
end=driver.find_element_by_id("endDate")

sd = input("Start Date: ")
ed = input("End Date: ")

start.send_keys(sd)
end.send_keys(ed)

driver.find_element_by_id("submit").click()

time.sleep(2)

soup=BeautifulSoup(driver.page_source,"html.parser")

abc=soup.find_all("th",align="right")

i = 0
output = [" (Download)", " (Upload)", " (Total)"]

for element in abc[-3:]:
	print(element.text, output[i])
	i = i + 1

driver.quit()














