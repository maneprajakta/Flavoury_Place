from  django.test import LiveServerTestCase
from  selenium  import  webdriver

class  MealPageTest(LiveServerTestCase):
    def setUp(self):
        self.driver  = webdriver.Chrome()
    
    def  testmeal(self):
        self.driver.get('http://127.0.0.1:8000/meals/')
        self.assertIn('Meals', self.driver.title)