from selenium import webdriver
from time import  sleep
import  pytest
class TestXueqiu:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.get('https://xueqiu.com/')

    def test_alibaba(self):
        driver = self.driver
        driver.maximize_window()
        driver.find_element_by_name("q").send_keys("阿里巴巴")
        sleep(2)
        driver.find_element_by_xpath('//*[@class="icon iconfont"]').click()
        driver.find_elements_by_css_selector('.follow__control .iconfont')[1].click()
        sleep(2)
        driver.find_element_by_name('username').send_keys("15013715713")
        driver.find_element_by_name('password').send_keys("yefeng")
        driver.find_element_by_css_selector('.modal__login__btn').click()
        sleep(2)
