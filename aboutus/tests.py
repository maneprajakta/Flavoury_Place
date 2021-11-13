from  django.test import LiveServerTestCase
from  selenium  import  webdriver

class  AboutUsPageTest(LiveServerTestCase):
    def setUp(self):
        self.driver  = webdriver.Chrome()
    
    def  testabout(self):
        self.driver.get('http://127.0.0.1:8000/about-us/')
        self.assertIn('AboutUs', self.driver.title)