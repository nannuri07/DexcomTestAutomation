import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

def regAutomation():
    driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
    driver.get("https://shrouded-lowlands-66853.herokuapp.com/")

    driver.find_element_by_id("user_first_name")
    elem.send_keys("Sam")
    driver.find_element_by_id("user_last_name")
    elem.send_keys("Test")


    select = Select(driver.find_element_by_id('user_suffix'))
    select.select_by_visible_text("PA")

    driver.find_element_by_id("user_title")
    elem.send_keys("Mr")

    driver.find_element_by_id("user_email")
    elem.send_keys("samtest@gmail.com")

    driver.find_element_by_id("user_phone_number")
    elem.send_keys("99999999")

    driver.find_element_by_id("user_business_name")
    elem.send_keys("Dexcom")

    driver.find_element_by_id("user_address_1")
    elem.send_keys("1111 nw test")

    driver.find_element_by_id("user_city")
    elem.send_keys("Portalnd")

    select = Select(driver.find_element_by_id('user_state'))
    select.select_by_visible_text("OR")

    driver.find_element_by_id("user_zip")
    elem.send_keys("11111")

    driver.find_element_by_id("user_agree_1").click()

    driver.find_element_by_id("user_agree_2").click()


    driver.find_element_by_name("commit").click()

    time.sleep(30)

    driver.close()

regAutomation()
