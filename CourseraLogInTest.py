__author__ = 'Marko'

# log in test class for coursera webpage, testing login with correct password and email, only correct password
# and only correct email

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class CorseraLogIn(unittest.TestCase):

    def setUp(self):
        ''' Firefox browser set up, open login page on coursera'''
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.coursera.org/?authMode=login")

    def testCorrectPassAndEmail(self):
        driver = self.driver
        email = ""
        password = ""
        loginLogoXpath = "/html/body/div[3]/div/div[2]/div[1]/div[1]/nav/div/div[3]/ul/li[2]/a/div/div/div/div/p"
        emailXpath = "/html/body/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div/div/form/div[1]/div[1]/input"
        passwordXpath = "/html/body/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div/div/form/div[1]/div[2]/input"
        logInConfirmButtonXpath = "/html/body/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div/div/form/button"

        emailElement = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(emailXpath))
        passwordElement = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(passwordXpath))
        logInConfButtonElement = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(logInConfirmButtonXpath))

        emailElement.clear()#text field clear
        emailElement.send_keys(email)#sending string keyword
        passwordElement.clear()
        passwordElement.send_keys(password)
        logInConfButtonElement.click()

        WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath(loginLogoXpath))

    def testCorrectPass(self):
        driver = self.driver
        # random emails
        emailList = ["ok@gmail.com", "test@gmail.com", "incorrect@gmail.com", "1253@gmail.com", ".,5758!!?@gmail.com"]
        password = "" #suppose this is correct password
        emailXpath = "/html/body/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div/div/form/div[1]/div[1]/input"
        passwordXpath = "/html/body/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div/div/form/div[1]/div[2]/input"
        logInConfirmButtonXpath = "/html/body/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div/div/form/button"
        wrongEmailMessageXpath = "/html/body/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div/div/div[2]/span"
        passwordElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(passwordXpath))
        emailElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(emailXpath))
        logInConfButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(logInConfirmButtonXpath))

        for email in emailList:
            emailElement.clear()
            emailElement.send_keys(email)
            passwordElement.clear()
            passwordElement.send_keys(password)
            logInConfButtonElement.click()
            WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(wrongEmailMessageXpath))

    def testCorrectEmail(self):
        driver = self.driver
        email = "" #suppose this is correct password
        passwordList = ["25879fdsg", "fdskhtor", "12.!!56", "abc5867po", "" ]
        emailXpath = "/html/body/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div/div/form/div[1]/div[1]/input"
        passwordXpath = "/html/body/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div/div/form/div[1]/div[2]/input"
        logInConfirmButtonXpath = "/html/body/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div/div/form/button"
        wrongEmailMessageXpath = "/html/body/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div/div/div[2]/span"
        passwordElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(passwordXpath))
        emailElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(emailXpath))
        logInConfButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(logInConfirmButtonXpath))

        for password in passwordList:
            emailElement.clear()
            emailElement.send_keys(email)
            passwordElement.clear()
            passwordElement.send_keys(password)
            logInConfButtonElement.click()
            WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(wrongEmailMessageXpath))

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()



