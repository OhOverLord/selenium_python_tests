import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class FirstSampleTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'LT:Options': {
                "build": "UnitTest-Selenium-Sample",
                "name": "UnitTest-Selenium-Test",
                "platformName": "Windows 11",
                "selenium_version": "4.0.0"
            },
            "browserName": "Chrome",
            "browserVersion": "latest",
        }

        self.driver = webdriver.Chrome(executable_path=r"C:\Users\ski20\Desktop\selenium_test\chromedriver.exe")

    def tearDown(self):
        self.driver.quit()

    def test_unit_user_should_able_to_add_item(self):
        driver = self.driver
        driver.get("https://lambdatest.github.io/sample-todo-app/")
        check_box_one = driver.find_element(By.NAME, "li1")
        check_box_one.click()
        check_box_two = driver.find_element(By.NAME, "li2")
        check_box_two.click()
        textfield = driver.find_element(By.ID, "sampletodotext")
        textfield.send_keys("Yey, Let's add it to list")
        add_button = driver.find_element(By.ID, "addbutton")
        add_button.click()
        added_item = driver.find_element(By.XPATH, "//span[@class='done-false']").text
        print(added_item)


if __name__ == "__main__":
    unittest.main()