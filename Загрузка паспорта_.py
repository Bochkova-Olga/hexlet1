# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_(self):
    self.driver.get("https://qa.neapro.site/cabinet/documents")
    self.driver.set_window_size(1200, 800)
    self.driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1) > .document-name").click()
    self.driver.find_element(By.CSS_SELECTOR, ".document-page").click()
    self.driver.find_element(By.ID, "surname").send_keys("Василисова")
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("Василиса")
    self.driver.find_element(By.CSS_SELECTOR, ".fieldsets:nth-child(1) > .fieldset").click()
    self.driver.find_element(By.ID, "patronymic").send_keys("Василисовна")
    self.driver.find_element(By.NAME, "date").click()
    self.driver.find_element(By.NAME, "date").send_keys("15.12.1975")
    self.driver.find_element(By.ID, "passportSeries").click()
    self.driver.find_element(By.ID, "passportSeries").send_keys("11-23")
    self.driver.find_element(By.ID, "passportNumber").click()
    self.driver.find_element(By.ID, "passportNumber").send_keys("123456")
    self.driver.find_element(By.CSS_SELECTOR, "#dateOfIssue .mx-input").click()
    self.driver.find_element(By.CSS_SELECTOR, "#dateOfIssue .mx-input").send_keys("15.12.1989")
    self.driver.find_element(By.ID, "code").click()
    self.driver.find_element(By.ID, "code").send_keys("000-000")
    self.driver.find_element(By.ID, "cardId").click()
    self.driver.find_element(By.ID, "cardId").send_keys("123-456-789 00")
    self.driver.find_element(By.ID, "issued").click()
    self.driver.find_element(By.ID, "issued").send_keys("ОВД Пупкино")
    self.driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys("г Москва, г Зеленоград, поселок Рожки, д 10, кв 1")
    self.driver.find_element(By.CSS_SELECTOR, ".outline").click()
    self.driver.find_element(By.XPATH, "//input[@type=\'file\']").send_keys("C:\\Users\\Сергей\\Desktop\\Tulips.jpg")
    self.driver.find_element(By.CSS_SELECTOR, ".fill").click()
    time.sleep(NaN)
    assert self.driver.find_element(By.CSS_SELECTOR, ".form-title").text == "Персональные данные"
  
