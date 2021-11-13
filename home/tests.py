from  django.test import LiveServerTestCase
from  selenium  import  webdriver

class  HomePageTest(LiveServerTestCase):
    def setUp(self):
        self.driver  = webdriver.Chrome()
    
    def  testhome(self):
        self.driver.get('http://127.0.0.1:8000/')
        self.assertIn('Home', self.driver.title)

    def testmanager(self):
        self.driver.get('http://127.0.0.1:8000/manager')
        self.assertIn('Manager', self.driver.title)

    def testorder(self):
        self.driver.get('http://127.0.0.1:8000/manager/order')
        self.assertIn('Billing', self.driver.title)
        