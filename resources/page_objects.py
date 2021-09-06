from webconfig import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support.ui import Select


class PageObjects:

    def __init__(self):
        self.browse = Driver()
        self.site = self.browse.driver
        self.wait = Wait(self.site, 30)

    def launch_browser(self, url):
        """
        This will help launch any browser and a url
        :param url: any url needed
        """
        self.site.get(url)

    def click_an_element(self, selector, element):
        """This method can click any element with any selector
        :param selector: the Element locator type
        :param element: the Element ID
        """
        self.site.find_element(selector, element).click()    

    def page_load(self, selector, element):
        """This method can help wait for a page to load
        :param selector: the Element locator type
        :param element: the Element ID to select an element to wait for
        """
        self.wait.until(EC.visibility_of_element_located((selector, element)))

    def insert_a_text(self, selector, field, text):
        """This method can click any element with any selector
        :param selector: the Element locator type for the text field
        :param field: the text field
        :param text: the text to enter
        """
        self.site.find_element(selector, field).send_keys(text)

    def select_an_item(self, selector, element, identifier):
        """
        This uses the selenium select option to pick an element
        :param selector: This specifies the identifier type
        :param element: Element to be queried
        :param identifier: This could be a value, index, or visible text
        :return:
        """
        select = Select(self.site.find_element(selector, element))
        select.select_by_visible_text(identifier)

    def scroll_down(self):
        self.site.execute_script("window.scrollTo(0, document.body.scrollHeight);")
