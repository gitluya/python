import HtmlTestRunner
import unittest
from ddt import ddt,data,file_data
from page_objects import PageObject, PageElement, MultiPageElement
from selenium import webdriver
import time

@ddt
class MyTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome()
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(10)

	#@data('unittest','ddt','selenium')
	@file_data('test_data_list.json')
	def test_baidu(self,keywords):	# 一组参数要加@unpack
		class BaiduPage(PageObject):
			keywords = PageElement(id_='kw')
			search = PageElement(id_='su')

		class BaiduResultPage(PageObject):
			keywords = PageElement(id_='kw')
			search = PageElement(id_='su')
			records = MultiPageElement(tag_name = 'h3')

		page = BaiduPage(self.driver,root_uri='http://www.baidu.com')
		page.get("/")
		page.keywords = keywords
		page.search.click()
		time.sleep(2)
		title = page.w.title
		self.assertEqual(title,keywords+'_百度搜索')

		resultPage = BaiduResultPage(self.driver)
		self.assertTrue(len(resultPage.records)>0)
		# self.driver.get
		# resultPage.w.get_screenshot_as_file(keywords+'.png')
		# resultPage.w.get_screenshot_as_file('/Screenshots/'+keywords+'.png')
		resultPage.w.get_screenshot_as_file('/Screenshots/foo.png')
		resultPage.w.get_screenshot_as_base64()
		print('截屏')

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
 
if __name__=="__main__":
	unittest.main(verbosity=2,testRunner=HtmlTestRunner.HTMLTestRunner(output='test3'))