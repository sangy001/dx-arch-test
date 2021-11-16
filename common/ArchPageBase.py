import os
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import platform

from common.Log import Logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import allure
logging = Logger()


def headless_chrome(width: int = 1920, high: int = 1200):
    """
    设置参数 --headless 和 --no-sandbox 以启动 Headless 版 Chrome
    并将浏览器窗口放大至 1920*1200
    :return:
    """
    logging.info(u'启动 HEADLESS 版 Chrome 浏览器')
    _options = Options()
    _options.add_argument('--headless')
    _options.add_argument('--no-sandbox')
    _options.add_argument('--lang=zh-CN')
    _options.add_argument('--disable-gpu')
    _options.add_argument('--disable-dev-shm-usage')
    _options.add_argument('--ignore-certificate-errors')

    # _options.add_argument('--disable-gpu')
    # _options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(chrome_options=_options)
    browser.set_window_size(width, high)
    return browser


def chrome(width: int = 1920, high: int = 1200):
    """
    设置参数 -lang=zh-cn 启动 Chrome
    并将浏览器窗口放大至 1920*1200
    :return:
    """
    logging.info(u'启动 Chrome 浏览器')
    _options = Options()
    _options.add_argument('-lang=zh-cn')
    browser = webdriver.Chrome(chrome_options=_options)
    browser.set_window_size(width, high)
    return browser


def launch_browser():
    if platform.system() == 'Linux':
        return headless_chrome()
    else:
        return chrome()


class Browser(object):
    def __init__(self, driver):
        self.driver = driver

    def screen(self, driver, name):
        if name is not None:
            allure.attach(driver.get_screenshot_as_png(), name, allure.attachment_type.PNG)  # 保存截图为allure的附件

    # 判断网页是否成功打开
    def find_title(self, loc):
        try:
            logging.debug("判断网页是否打开")
            WebDriverWait(self.driver, 30, 0.5).until(EC.title_contains(loc))
            sleep(5)
            self.screen(self.driver, "%s元素存在" % loc)
        except (NoSuchElementException, TimeoutException) as e:
            logging.error("页面上没有找到该元素: %s" % loc)
            logging.error(">>> NoSuchElementException or TimeoutException")
            logging.error(e)
            self.screen(self.driver, "%s元素不存在 或 超时" % loc)
            raise
        except BaseException as e:
            logging.error("页面上没有找到该元素: %s" % loc)
            logging.error(">>> BaseException")
            logging.error(e)
            self.screen(self.driver, "%s元素不存在" % loc)
            raise
        else:
            logging.debug("网页打开成功")

    # 查找元素是否存在
    # loc为xpath
    def find_loc(self, loc):
        try:
            # WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element(loc)))
            logging.debug("开始查找元素: %s" % loc)
            WebDriverWait(self.driver, 30, 0.5).until(lambda driver: driver.find_element_by_xpath(loc))
        except (NoSuchElementException, TimeoutException) as e:
            logging.error("页面上没有找到该元素: %s" % loc)
            logging.error(">>> NoSuchElementException or TimeoutException")
            logging.error(e)
            self.screen(self.driver, "%s元素不存在 或 超时" % loc)
            raise
        except BaseException as e:
            logging.error("页面上没有找到该元素: %s" % loc)
            logging.error(">>> BaseException")
            logging.error(e)
            self.screen(self.driver, "%s元素不存在" % loc)
            raise
        else:
            logging.debug("在该页面上找到元素: %s" % loc)

    # 判断元素是否可点击
    # loc 为Xpath
    def verify_loc_click(self, loc):
        try:
            logging.debug("判断元素「%s」是否可点击" % loc)
            WebDriverWait(self.driver, 30, 0.5).until(EC.element_to_be_clickable((By.XPATH, loc)))
        except (NoSuchElementException, TimeoutException) as e:
            logging.error("页面上没有找到该元素: %s" % loc)
            logging.error(">>> NoSuchElementException or TimeoutException")
            logging.error(e)
            self.screen(self.driver, "%s元素不存在" % loc)
            raise
        except BaseException as e:
            logging.error("元素无法点击: %s" % loc)
            logging.error(">>> BaseException")
            logging.error(e)
            self.screen(self.driver, "%s元素无法点击" % loc)
            raise
        else:
            logging.debug("元素「%s」可点击" % loc)
            # return True

    # 判断元素是否已经消失
    def verify_loc_disappear(self, loc):
        try:
            logging.debug("判断元素 %s 页面上不可见" % loc)
            WebDriverWait(self.driver, 30, 0.5).until(EC.invisibility_of_element((By.XPATH, loc)))
        except BaseException as e:
            logging.error("元素 %s 页面上存在" % loc)
            logging.error(">>> BaseException")
            logging.error(e)
            self.screen(self.driver, "%s元素存在" % loc)
            raise
        else:
            logging.debug("元素 %s 已经消失" % loc)


    def click_element(self, latest_loc):

        try:
            self.find_loc(latest_loc)
        except BaseException as e:
            logging.error("该元素存在问题: %s" % latest_loc)
            logging.error(">>> BaseException")
            logging.error(e)
            raise
        else:
            self.driver.find_element_by_xpath(latest_loc).click()

    # loc 为Xpath
    # 先判断元素是否存在，是否可点击
    # 并点击元素
    def click_button(self, latest_loc, pre_loc=None):
        if pre_loc is None:
            try:
                self.find_loc(latest_loc)
                self.verify_loc_click(latest_loc)
            except BaseException as e:
                logging.error("该元素存在问题: %s" % latest_loc)
                logging.error(">>> BaseException")
                logging.error(e)
                raise
            else:
                self.driver.find_element_by_xpath(latest_loc).click()
        else:
            try:
                self.verify_loc_disappear(pre_loc)
                self.find_loc(latest_loc)
                self.verify_loc_click(latest_loc)
            except BaseException as e:
                logging.error("该元素存在问题: %s" % latest_loc)
                logging.error(">>> BaseException")
                logging.error(e)
                raise
            else:
                self.driver.find_element_by_xpath(latest_loc).click()

    # 下拉框选择
    def click_select_loc(self, select_loc, select_content):
        try:
            self.find_loc(select_loc)
            self.verify_loc_click(select_loc)
            # driver.find_element_by_xpath(select_loc).click()
        except BaseException as e:
                logging.error("该元素存在问题: %s" % select_loc)
                logging.error(">>> BaseException")
                logging.error(e)
                raise
        else:
            self.driver.find_element_by_xpath(select_loc).click()
            self.driver.find_element_by_xpath(select_content).click()

    # 输入数据
    def send_text(self, loc, content):
        try:
            self.find_loc(loc)
            self.verify_loc_click(loc)
        except BaseException as e:
            logging.error("该元素存在问题: %s" % loc)
            logging.error(">>> BaseException")
            logging.error(e)
            raise
        else:
            logging.info("输入参数:%s" % content)
            self.driver.find_element_by_xpath(loc).send_keys(content)

    # 清除元素
    def text_clear(self, loc):
        try:
            self.find_loc(loc)
        except BaseException as e:
            logging.error(">>> BaseException")
            logging.error(e)
            raise
        else:
            self.driver.find_element_by_xpath(loc).clear()

    # 判断元素是否现在界面上存在, 是否创建成功
    def check_loc(self, name):
        loc = '//div[contains(text(),"'+name+'")]'
        try:
            # WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element(loc)))
            logging.debug("开始查找元素: %s" % loc)
            WebDriverWait(self.driver, 30, 0.5).until(lambda driver: driver.find_element_by_xpath(loc))
        except (NoSuchElementException, TimeoutException) as e:
            logging.error("页面上没有找到该元素: %s" % loc)
            logging.error(">>> NoSuchElementException or TimeoutException")
            logging.error(e)
            self.screen(self.driver, "%s元素不存在" % loc)
            raise
        except BaseException as e:
            logging.error("页面上没有找到该元素: %s" % loc)
            logging.error(">>> BaseException")
            logging.error(e)
            self.screen(self.driver, "%s元素不存在" % loc)
            raise
        else:
            logging.debug("元素存在「%s」存在" % loc)

    # 判断提示是否现在界面上存在, 是否删除成功
    # def check_del_loc(self, name):
    #     loc = '//div[contains(text(),"'+name+'")]'
    #     try:
    #         # WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element(loc)))
    #         logging.info("开始查找元素: %s" % loc)
    #         WebDriverWait(self.driver, 30, 0.5).until(lambda driver: driver.find_element_by_xpath(loc))
    #     except (NoSuchElementException, TimeoutException) as e:
    #         logging.info("页面上没有找到该元素: %s" % loc)
    #         logging.info(">>> NoSuchElementException or TimeoutException")
    #         logging.info(e)
    #         raise
    #     except BaseException as e:
    #         logging.info("页面上没有找到该元素: %s" % loc)
    #         logging.info(">>> BaseException")
    #         logging.info(e)
    #         raise
    #     else:
    #         logging.info("元素存在「%s」存在，删除成功" % loc)







