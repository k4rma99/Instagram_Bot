from selenium import webdriver
from time import sleep

class instagram_unfollow_check:
    def __init__(self , username = "joke.peralta_", password = "creator123"):
        self.driver = webdriver.Chrome("C:/chromedriver.exe")
        self.driver.get("https://www.instagram.com/")
        sleep(5)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        sleep(1)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        sleep(1)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(5)~
        self.driver.find_element_by_xpath("//button[contains(text(),\"Not Now\")]").click()
        sleep(3)
        self.driver.find_element_by_xpath("//a[contains(text(), '" + username + "')]").click()
        sleep(20)

instagram_unfollow_check()
