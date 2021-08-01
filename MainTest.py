from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time

class Logintest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome("D:/WebDrivers/chromedriver.exe")
        cls.driver.implicitly_wait(100)
        cls.driver.maximize_window()
        cls.driver.get("https://www.cruxintelligence.com")
        cls.driver.implicitly_wait(1000)
        # ACCEPT ALL COOKIES
        cls.driver.find_element_by_id("hs-eu-confirmation-button").click()

    def test_Login_check(self):    ####---> click on login -> check if logging in. save the error message
        self.driver.find_element_by_xpath("//a[@title='LOG IN']").click()
        time.sleep(3)

        userName = self.driver.find_element_by_xpath("//input[@id='userInput']")
        userName.clear()
        userName.send_keys("devmishra")
        self.driver.find_element_by_xpath("//div[@class='login-action']").click()
        time.sleep(3)
        assert self.driver.find_element_by_xpath("//div[@class='login__error']").is_displayed(), "Error Message Not Displayed! Testcase Failed."

        # if self.driver.find_element_by_xpath("//div[@class='login__error']").is_displayed() and self.driver.find_element_by_xpath("//div[@class='login__error']").is_enabled():
        #     print("Login Failed. Error message is present. Testcase Passed.")
        # else:
        #     print("Error message is not present. Testcase Failed.")

    def test_HompageButton(self):   ####---> Go back to homepage by clicking on logo
        self.driver.find_element_by_class_name("img-fluid").click()

    def test_Youtube_Video(self):   ####---> Click on the video of homepage and play it for 10 seconds then stop it.
        self.driver.find_element_by_xpath("//ol[@class='carousel-indicators']/li[1]").click()
        self.driver.find_element_by_xpath("//div[@class='d-home21-vdo']/div/iframe[1]").click()
        time.sleep(20)
        self.driver.find_element_by_xpath("//div[@class='d-home21-vdo']/div/iframe[1]").click()
        time.sleep(3)

    def test_AboutUs_NameCheck(self):   ####---> Go to about us -> check if Sumith Balagangadharan and Ganesh Subramanian name's are displayed correctly
        self.driver.find_element_by_xpath("//a[@title='About Us']").click()
        time.sleep(3)

        if self.driver.find_element_by_link_text(
                "Sumith Balagangadharan").is_displayed() and self.driver.find_element_by_link_text("Sumith Balagangadharan").is_enabled():
            print("NAME MATCHES! Sumith Balagangadharan is present. Testcase Passed.")
        else:
            print("NAME DID NOT MATCH! Testcase Failed.")

        if self.driver.find_element_by_link_text("Ganesh Subramanian").is_displayed() and self.driver.find_element_by_link_text("Ganesh Subramanian").is_enabled():
            print("NAME MATCHES! Ganesh Subramanian is present. Testcase Passed.")
        else:
            print("NAME DID NOT MATCH! Testcase Failed.")

        # assert driver.find_element_by_link_text("Sumith Balagangadharan").is_displayed(), "NAME DID NOT MATCH! Testcase Failed."
        # assert driver.find_element_by_link_text("Ganesh Subramanian").is_displayed(), "NAME DID NOT MATCH! Testcase Failed."

    def test_PlaystoreButton(self):    ####---> Check if opened in new tab when clicked on playstore and apple store buttons
        playStore = self.driver.find_element_by_xpath("//div[@class='col-md-6']/a[1]/img")
        assert playStore.is_enabled(), "LINK DID NOT OPEN IN NEW TAB!"
        playStore.click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        appleStore = self.driver.find_element_by_xpath("//div[@class='col-md-6']/a[2]/img")
        assert appleStore.is_enabled(), "LINK DID NOT OPEN IN NEW TAB!"
        appleStore.click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @classmethod
    def tearDownClass(cls):
        #cls.driver.delete_all_cookies()
        cls.driver.quit()