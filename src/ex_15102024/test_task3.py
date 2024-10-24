from selenium import webdriver
import allure
import pytest

@allure.title("verify the title of webpage ")
def test_task():
    driver = webdriver.Chrome()  #here the selenium mgr will create a instance of chrome by itself whre it will open the URL
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    print(driver.title)  # GET Request
    assert driver.title == "CURA Healthcare Service"


    driver.current_url == "https://katalon-demo-cura.herokuapp.com/"

    driver.page_source.__contains__("CURA Healthcare Service")
    driver.quit()



