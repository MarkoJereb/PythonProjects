__author__ = 'Marko'

# class test for five simple tests for www.coursera.com, test check search results, log in, select class, log out


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import unittest


class CourseraTest(unittest.TestCase):
    def setUp(self):
        ''' Firefox browser set up'''
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.coursera.org/")
        assert "Coursera" in self.driver.title

    def testLogIn(self):
        '''test for log in'''
        driver = self.driver
        email = "markojereb@yahoo.com"
        password = "orbit247"
        logInXpath = "/html/body/div[2]/div/div/div[1]/div[1]/nav/div/div[2]/ul/li[2]/a"
        emailXpath = "/html/body/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div/div/form/div[1]/div[1]/input"
        passwordXpath = "/html/body/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div/div/form/div[1]/div[2]/input"
        logInConfirmButtonXpath = "/html/body/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div/div/form/button"

        logInElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(logInXpath))
        logInElement.click()
        emailElement = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(emailXpath))
        passwordElement = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(passwordXpath))
        logInConfButtonElement = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(logInConfirmButtonXpath))

        emailElement.clear()#text field clear
        emailElement.send_keys(email)#sending string keyword
        passwordElement.clear()
        passwordElement.send_keys(password)
        logInConfButtonElement.click()

    def testSearch(self):
        '''test for course search with python keyword'''
        driver = self.driver
        searchXpath = "/html/body/div[3]/div/div[2]/div[1]/div[1]/nav/div/div[2]/span/form/span/span/input[2]"
        searchElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(searchXpath))
        searchElement.send_keys("python")
        searchElement.submit()

    def testSelect(self):
        '''test for selectin different courses'''
        driver = self.driver
        courseSelectXpath1 = "/html/body/div[2]/div/div[2]/div/div/div[2]/a[1]/div/div/div[2]/div/h2"
        courseSelectXpath2 = "/html/body/div[2]/div/div[2]/div/div/div[2]/a[5]/div/div/div[2]/div/h2"
        courseElement1 = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(courseSelectXpath1))
        courseElement1.click()
        driver.back()

        courseElement2 =  WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(courseSelectXpath2))
        courseElement2.click()

    def testLogOut(self):
        '''test for log out'''
        driver = self.driver
        dropDownButtonXpath = "/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[1]/nav/div/div[3]/ul/li[3]/a"
        logOutButtonXpath = "/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[1]/nav/div/div[3]/ul/li[3]/ul/li[5]/a/form/button"

        dropDownButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(dropDownButtonXpath))
        logOutButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(logOutButtonXpath))

        dropDownButtonElement.click()
        logOutButtonElement.click()

    def tearDown(self):
        self.driver.close()


if __name__=='__main__':
    #unittest.main()
    test = CourseraTest()
    test.setUp()
    test.testLogIn()
    test.testSearch()
    test.testSelect()
    test.testLogOut()
    test.tearDown()
