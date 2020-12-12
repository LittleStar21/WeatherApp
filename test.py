from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import unittest
import time

class MyWebsiteTest(unittest.TestCase):
    def setUp(self):
        # Change the path to where the geckodriver file exists
        self.browser = webdriver.Firefox(executable_path=r"C:\Users\fifia\Desktop\bahagian\Interview\iklim\geckodriver.exe")
    
    def tearDown(self):
        self.browser.quit()

    def test_for_checking_weather(self):
        print("Ian wants to check the new website, how is the weather 5 days from now?")
        self.browser.get("http://127.0.0.1:5000/")
        time.sleep(1)

        print("He notices the page title mentions Weather App")
        self.assertIn("Weather App", self.browser.title)

        print("He is asked to choose a country")
        city_options = Select(self.browser.find_element_by_id("country"))
        self.assertIn("Select a country", self.browser.page_source)
        time.sleep(1)
        
        print("He selected Singapore")
        city_options.select_by_visible_text("Singapore")
        time.sleep(1)

        print("When he hits enter, the pages returned the weather in Singapore for the next 5 days")
        search_button = self.browser.find_element_by_id("search")
        search_button.send_keys(Keys.ENTER)
        time.sleep(1)

        print("The title then changed into search result")
        self.assertIn("Search result", self.browser.page_source) 

        print("He finds a single table")
        table = self.browser.find_element_by_tag_name("table")
        
        print("That table consists of weather info for the next 5 days")
        th = table.find_elements_by_tag_name("th")
        header_texts = [header.text for header in th]
        self.assertIn("Temperature", header_texts)
        self.assertIn("Max Difference", header_texts)

        td = table.find_elements_by_tag_name("td")
        self.assertEqual(len(td), 18)

        print("He finished the test")
        time.sleep(5)

if __name__ == "__main__":
    unittest.main(warnings="ignore")