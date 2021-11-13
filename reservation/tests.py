from datetime import time
from  django.test import LiveServerTestCase
from  selenium  import  webdriver
from selenium.webdriver.common.keys import Keys
from .models import Reservation

class  BlogPageTest(LiveServerTestCase):
    def setUp(self):
        self.driver  = webdriver.Chrome()
    
    def testreserve(self):
        self.driver.get('http://127.0.0.1:8000/reserve_table/')
        self.assertIn('Reserve Table', self.driver.title)

    def testreservtionform(self):
        self.driver.get('http://127.0.0.1:8000/reserve_table/')
        name = self.driver.find_element_by_id('id_name')
        email = self.driver.find_element_by_id('id_email')
        phone = self.driver.find_element_by_id('id_phone')
        no_of_persons = self.driver.find_element_by_id('id_number_of_persons')
        date = self.driver.find_element_by_id('id_Date')
        time = self.driver.find_element_by_id('id_time')
        submit = self.driver.find_element_by_id('submit')
        #populate the form with data
        name.send_keys('Test')
        email.send_keys('prajakta916mane1@gmail.com')
        phone.send_keys('9177878787')
        no_of_persons.send_keys('2')
        date.send_keys('2021-11-16')
        time.send_keys('12:00')
        submit.send_keys(Keys.RETURN)
        assert 'Test' in self.driver.page_source
    
    def testsucess(self):
        self.driver.get('http://127.0.0.1:8000/reserve_table/success/')
        self.assertIn('Sucess', self.driver.title)
        