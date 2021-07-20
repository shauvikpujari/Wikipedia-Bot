from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyttsx3 as p
class info():
    def __init__(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
    def get_info(self,query):
        self.query = query;
        self.driver.get(url="https://wikipedia.org/")
        search=self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click();
        search.send_keys(query);
        enter =self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()
        info=self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/p[2]')

        readable=info.text

        engine=p.init()
        engine.say(readable)
        engine.runAndWait();






# dot=info();
# dot.get_info("hero");