from selenium import webdriver
import allure
import pytest

@allure.title("verify the title of webpage app.vwo.com")
def test_sample():
    driver = webdriver.Chrome()  #here the selenium mgr will create a instance of chrome by itself whre it will open the URL
    driver.get("https://sdet.live")
