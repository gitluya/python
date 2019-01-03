from page_objects import PageObject, PageElement
from selenium import webdriver
import unittest
import time
 
class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        #self.base_url = "http://www.baidu.com"
    
    def test_baidu(self):
        class BaiduPage(PageObject):
            keywords = PageElement(id_='kw')
            search = PageElement(id_='su')

        page = BaiduPage(self.driver,root_uri='http://www.baidu.com')
        page.get("/")
        page.keywords = 'unittest'
        page.search.click()
        time.sleep(2)
        title = page.w.title
        self.assertEqual(title,'unittest_百度搜索')
 
    def tearDown(self):
        self.driver.quit()
 
if __name__=="__main__":
    unittest.main()