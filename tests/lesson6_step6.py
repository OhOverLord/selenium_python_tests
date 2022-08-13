from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome(r"C:\Users\ski20\Desktop\selenium_test\chromedriver.exe")
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("My answ")

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла