from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from traceback import print_stack


#list of APIs created
    # 1. launch_url
    # 2. verify_title
    # 3. get_by_type
    # 4. get_element
    # 5. enter_text
    # 6. wait_for_element
    # 7. element_click
    # 8. is_element_present

class SeleniumDriver():

    def __init__(self, driver):
        self.driver = driver

    ##################################################################
    def launch_url(self, url):
        '''
            launch the url
            paramater: URL
            return value: None
        '''
        try:
            self.driver.get(url)
            print('URL: {} launch: success '.format(url))
        except Exception as e:
            print('URL: {} launch: fail... Exception error: {} '.format(url, e))

    ##################################################################

    def verify_title(self, text):
        '''
            verify the title
            paramater: title text to verify
            return value: True or False
        '''
        text = text.lower()
        captured_title = self.driver.title
        if text == captured_title.lower():
            print('title match - pass, title from the browser is ' + captured_title)
            return True
        else:
            print('title match - fail, title from the browser {}, excepted browser title: {} '.
                  format(captured_title,text))
            return False

    ##################################################################

    def get_by_type(self, locatortype):
        '''
            function to get locator type
            parameter: locator type like ID,XPATH, CSS.. et
            return value: by. ID, by.XPATH..etc
        '''
        locatortype = locatortype.lower()
        if locatortype == 'id':
            return By.ID
        elif locatortype == 'xpath':
            return By.XPATH
        elif locatortype =='css':
            return By.CSS_SELECTOR
        elif locatortype == 'name':
            return By.NAME
        elif locatortype == 'link':
            return By.LINK_TEXT
        elif locatortype == 'partiallink':
            return By.PARTIAL_LINK_TEXT
        elif locatortype == 'tagname':
            return By.TAG_NAME
        else:
            print('locator type: {} is invalid'.format(locatortype))
            return None

    ##################################################################

    def get_element(self, locator, locatortype = 'id'):
        '''
            enter the text in the editbox field
            parameters:  locatortype, locator
            return value: element or None
        '''
        element = None
        by_value = self.get_by_type(locatortype)
        try:
            element = self.driver.find_element(by_value,locator)
            print('Element with locator {} using locator type {} found status: success'.format(locator, locatortype))
            return element
        except NoSuchElementException as e:
            print('Element with locator {} using locator type {} found status: Fail, exception message: {}'
                  .format(locator,locatortype,e.message))
        except Exception as e:
            print('Element with locator {} using locator type {} found status: Fail, exception message: {}'
                  .format(locator,e.message))
        return element

    ##################################################################

    def enter_text(self, element, text):
        '''
        enter the value in the element
        :parameter: element,text
        return:
        '''
        try:
            self.driver.element.send_keys(text)
            print('enter text on the element : pass')
        except Exception as e:
            print('enter text status: fail, exception message:'+e)

    ##################################################################

    def wait_for_element(self, locator, timeout=10, locatortype='ID',poll_frequency=1):
        '''
            Explicit wait
            paramters: locator, locator type, timeout
            return:
        '''
        element = None
        try:
            locatortype= locatortype.lower()
            byType = self.get_by_type(locatortype)
            wait = WebDriverWait(self.driver, timeout, poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(ec.element_to_be_clickable((byType,locator)))
            print('Element with locator {} locator type {} appeared on the web page'.format(locator, locatortype))
        except Exception as e:
            print('Element with locator {} using locator type {} is not appeared on the web page, exception message: {}'
                  .format(locator,locatortype, e.message))
            print_stack()
        return element

    ##################################################################

    def element_click(self,locator, locatortype='id'):
        '''
        element to click
        :param locator: element locator
        :param locatortype: element locator type
        :return:
        '''
        try:
            self.get_element(locator,locatortype).click
            print('Element with locator {} using locator type {} click : success'.format(locator, locatortype))
        except Exception as e
            print('Element with locator {} locator type {}  click : fail, exception message :{}'
                  .format(locator, locatortype,e.message))
            print_stack()

    ##################################################################

    def is_element_present(self, locator, locatortype='id'):
        '''
        method to verify element is present
        :param locator:
        :param locatortype:
        :return: True or False
        '''
        try:
            element = self.get_element(locator, locatortype)
            if element is not None:
                print('Element with locator {} using locator type {} is present '.format(locator, locatortype))
                return True
            else:
                print('Element with locator {} using locator type {} is not present '.format(locator, locatortype))
                return False
        except:
            print_stack()
            return False