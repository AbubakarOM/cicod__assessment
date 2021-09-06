from selenium import webdriver


class Driver:
    """
    This creates the instance of a web driver
    to help automate the web app.
    """

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        