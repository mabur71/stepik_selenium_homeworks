from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math 


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

#Дождаться, когда цена дома уменьшится до 10000 RUR (ожидание нужно установить не меньше 12 секунд)
try:
    button = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"10000 RUR")
    )
finally:
  #Нажать на кнопку
  browser.find_element_by_id("book").click()
  x_element = browser.find_element_by_id("input_value")
  x = x_element.text
  input1 = browser.find_element_by_id("answer")
  input1.send_keys(str(calc(x)))
  browser.find_element_by_id("solve").click()












