from  django.test import LiveServerTestCase
from  selenium  import  webdriver
from selenium.webdriver.common.keys import Keys

class  ContactUsPageTest(LiveServerTestCase):
    def setUp(self):
        self.driver  = webdriver.Chrome()
    
    def  testcontact(self):
        self.driver.get('http://127.0.0.1:8000/contact/')
        self.assertIn('ContactUs', self.driver.title)

    def testcontactform(self):
        self.driver.get('http://127.0.0.1:8000/contact/')
        subject = self.driver.find_element_by_id('id_subject')
        from_email = self.driver.find_element_by_id('id_from_email')
        message = self.driver.find_element_by_id('id_message')
        subject.send_keys('Check')
        from_email.send_keys('prajakta916mane1@gamil.com')
        message.send_keys('Test1')
        submit = self.driver.find_element_by_id('submit')
        submit.send_keys(Keys.RETURN)
        assert 'Submitted' in self.driver.title
    
    def  testsuccesscontact(self):
        self.driver.get('http://127.0.0.1:8000/contact/success/')
        self.assertIn('Submitted', self.driver.title)
  
  