import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\ski20\Desktop\selenium_test\chromedriver.exe")
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):
        main_page = page.MainPage(self.driver)
        self.assertTrue(main_page.is_title_matches(), "python.org title doesn't match.")
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        self.assertTrue(search_results_page.is_results_found(), "No results found.")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()