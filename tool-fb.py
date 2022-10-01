from email import message
from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
from os import link
from selenium import webdriver
import time
message=input("Nội Dung Muốn Đăng Bài: ")
value="/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div"
#link Group
LinkGroup=['834787847917548','3275258786077478']
time.sleep(2)
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)
driver.find_element("name","email").send_keys("hanzoo4210@gmail.com")
driver.find_element("name","pass").send_keys("cvbn1114")
driver.find_element("name","login").click()
time.sleep(5)
for i in range (len(LinkGroup)):
    driver.get("https://www.facebook.com/groups/"+LinkGroup[i])
    element = driver.find_element("xpath","/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div[1]/span")
    element.click()
    time.sleep(3)
    element = driver.find_element("xpath","/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div").send_keys(message)
    time.sleep(5)
    dangbai=driver.find_element("xpath","/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div[1]").click()
    time.sleep(5)