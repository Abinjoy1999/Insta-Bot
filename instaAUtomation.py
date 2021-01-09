from selenium import webdriver
import time
browser=webdriver.Chrome(executable_path='C:\webdriver\chromedriver.exe')
browser.get('https://www.instagram.com/accounts/login/')
#time.sleep(2)
s=browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
s.click()
s.send_keys('ciet_camera_addicts')
s=browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
s.click()
s.send_keys('abinagul1999')

#time.sleep(2)
#browser.find_element_by_xpath('//*[@id="lga"]').click()
b=browser.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]')
b.click()
time.sleep(10)
noti=browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
noti.click()
tags=["ktmduke","motographer","r15v3"]
for i in tags:
    browser.get('https://www.instagram.com/explore/tags/'+i+'/')
    for j in range(10):
        first=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]').click()
        follow=browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
        like=browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
        nextp=browser.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click()
'''
s=browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
#s.click()

s.send_keys('#motographer')
tag=browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]/div')
tag.click()'''