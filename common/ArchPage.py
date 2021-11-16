from time import sleep
from common.Log import Logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from common.ArchPageBase import Browser
from common.ArchPageBase import headless_chrome
from config.Config import Config
from element import LoginPage, UserPage, IdentifyPage, LdapPage, AccessPage, SettingPage, AuditPage, KeyclockPage
import string
import random


logging = Logger()
driver = headless_chrome()
browser = Browser(driver)
config = Config()


class E2E(object):
    def clear_ldap(self):
        logging.info(">>>>>清理测试用例执行的环境")

        logging.info(">>>>>登录keyclock管理")
        driver.get(config.keycloak_url+"/auth/admin")
        try:
            WebDriverWait(driver, 30, 0.5).until(EC.title_contains("Log"))
            browser.find_loc(KeyclockPage.login)
            browser.send_text(KeyclockPage.username, config.username)
            browser.send_text(KeyclockPage.password, config.password)
            browser.click_button(KeyclockPage.login)
        except (NoSuchElementException, TimeoutException):
            logging.info(">>>>>已经登录")
        finally:
            logging.info(">>>>>选择租户")
            try:
                # WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element(loc)))
                logging.debug("开始查找元素: %s" % KeyclockPage.ns_arch)
                WebDriverWait(driver, 30, 0.5).until(lambda driver: driver.find_element_by_xpath(KeyclockPage.ns_arch))
            except BaseException as e:
                WebDriverWait(driver, 30, 0.5).until(EC.element_to_be_clickable((By.XPATH, KeyclockPage.ns)))
                WebDriverWait(driver, 30, 0.5).until(EC.element_to_be_clickable((By.XPATH, KeyclockPage.ns_selcet)))
            else:
                pass

            logging.info(">>>>>删除存在的ldap")
            browser.click_element(KeyclockPage.user_federation)
            browser.click_element(KeyclockPage.delete)
            browser.click_button(KeyclockPage.delete_confirm)
            sleep(5)



    def login(self):
        """
        打开网页并进行登录
        :return:
        """
        # 打开网址
        logging.info(">>>>>正在打开网页: %s" % config.arch_web_url)

        driver.get(config.arch_web_url)
        sleep(20)
        # 判断网页
        browser.find_title("Log")
        # browser.find_loc(LoginPage.login)
        browser.send_text(LoginPage.username, config.username)
        browser.send_text(LoginPage.password, config.password)
        browser.click_button(LoginPage.login)

        logging.info(">>>>>进入用户管理界面")
        browser.click_element(UserPage.header_gear)
        browser.click_element(UserPage.user_manage)

    def close_browser(self):
        logging.info(">>>>>关闭网页")
        driver.quit()
        logging.info(">>>>>关闭成功")


    def delete_user(self):
        logging.info(">>>>>禁用用户")
        browser.click_button(UserPage.more)
        browser.click_element(UserPage.disable)
        browser.check_loc("禁用用户")

        logging.info(">>>>>删除用户")
        browser.click_button(UserPage.more)
        browser.click_element(UserPage.delete)
        browser.send_text(UserPage.del_confirm, "CONFIRM DELETE")
        browser.click_button(UserPage.del_button)
        browser.check_loc("删除用户")
        sleep(3)


    def create_user(self):
        """
        创建用户
        :return:
        """
        # 进入user界面
        lastname = ''.join(random.sample(string.ascii_letters + string.digits, 5))
        name = "ui_" + lastname.lower()
        email = name + "@ui.com"
        password = "Danger0us"

        # logging.info("进入用户界面")
        # browser.click_element(UserPage.header_gear)
        # browser.click_element(UserPage.user_manage)
        browser.click_element(UserPage.user)

        # 点击创建user
        logging.info(">>>>>创建用户: %s" % name)
        browser.click_button(UserPage.create_user)
        browser.send_text(UserPage.username, name)
        browser.send_text(UserPage.lastname, lastname.lower())
        browser.send_text(UserPage.firstname, "ui")
        browser.send_text(UserPage.email, email)
        browser.send_text(UserPage.password, password)
        browser.send_text(UserPage.confirm_password, password)
        browser.click_button(UserPage.confirm)
        # 查看是否创建成功
        browser.check_loc(email)
        logging.info(">>>>>创建用户「%s」成功" % name)
        sleep(3)
        self.delete_user()


    def create_idp(self):
        name = "idp"
        well_known = "https://login.microsoftonline.com/"+config.arch_test_idp_tenant_id+"/v2.0/.well-known/openid-configuration"

        logging.info(">>>>>进入idp页面")
        browser.click_element(IdentifyPage.identity)
        browser.click_button(IdentifyPage.identity_add)

        logging.info(">>>>>创建idp: %s" % name)
        browser.send_text(IdentifyPage.identity_name, name)
        browser.send_text(IdentifyPage.identity_client_id, config.arch_test_idp_client_id)
        browser.send_text(IdentifyPage.identity_client_secret, config.arch_test_idp_client_secret)
        browser.click_button(IdentifyPage.quick_get)
        browser.send_text(IdentifyPage.wellknown_url, well_known)

        browser.click_button(IdentifyPage.get_confirm)

        browser.click_button(IdentifyPage.confirm, IdentifyPage.get_confirm)
        browser.check_loc(name)
        logging.info(">>>>>创建idp成功")

    def clear_idp(self):
        logging.info(">>>>>进入idp页面")
        browser.click_element(IdentifyPage.identity)

        logging.info(">>>>>删除idp页面")
        try:
            browser.find_loc(IdentifyPage.more)
        except BaseException:
            logging.info(">>>>>未接入idp")
        else:
            browser.click_button(IdentifyPage.more)
            browser.click_element(IdentifyPage.delete)
            browser.send_text(IdentifyPage.del_confirm, "CONFIRM DELETE")
            browser.click_button(IdentifyPage.del_button)
            sleep(5)


    def create_ldap(self):
        logging.info(">>>>>进入LDAP界面")

        browser.click_element(LdapPage.ldap)
        browser.click_button(LdapPage.ldap_add)

        logging.info(">>>>>进入创建LDAP界面")
        browser.send_text(LdapPage.ldap_address, config.arch_test_ldap_host)
        browser.send_text(LdapPage.ldap_username, config.arch_test_ldap_user)
        browser.send_text(LdapPage.ldap_password, config.arch_test_ldap_password)
        browser.send_text(LdapPage.ldap_dn, config.arch_test_ldap_dn)
        browser.click_button(LdapPage.confirm)
        browser.click_button(LdapPage.confirm)
        browser.check_loc(config.arch_test_ldap_host)
        logging.info(">>>>>创建LDAP成功")
        logging.info(">>>>>同步用户")
        browser.click_button(LdapPage.more)
        browser.click_element(LdapPage.ldap_sync)
        browser.check_loc("同步成功")
        sleep(5)

    def delete_sso(self, sso, webhook):
        """

        :return:
        """
        logging.info(">>>>>点击「设置」")
        browser.click_element(AccessPage.webhook_setting)

        logging.info(">>>>>点击「删除」")
        browser.click_element(AccessPage.webhook_del)

        logging.info(">>>>>输入「CONFIRM DELETE」")
        browser.send_text(AccessPage.del_confrm, "CONFIRM DELETE")
        browser.click_button(AccessPage.del_button)
        browser.check_loc("删除 %s 成功" % webhook)
        logging.info(">>>>>删除 %s 成功" % webhook)

        logging.info(">>>>>点击「更多操作」")
        sleep(5)
        browser.click_button(AccessPage.more)
        logging.info(">>>>>点击「删除」")
        browser.click_element(AccessPage.delete)
        browser.send_text(AccessPage.del_confrm, "CONFIRM DELETE")
        browser.click_button(AccessPage.del_button)
        browser.check_loc("删除客户端 %s 成功" % sso)
        logging.info(">>>>>删除客户端 %s 成功" % sso)


    def create_sso(self):
        """
        :return:
        """
        lastname = ''.join(random.sample(string.ascii_letters + string.digits, 5))
        sso_name = "ui" + lastname.lower()
        webhook_name = "webhook" + lastname.lower()

        logging.info(">>>>>进入「接入管理」界面")
        browser.click_element(AccessPage.sso)
        browser.click_button(AccessPage.sso_create)

        logging.info(">>>>>点击「接入产品」")
        browser.send_text(AccessPage.sso_client_id, sso_name)
        browser.click_button(AccessPage.confirm)
        browser.check_loc("客户端创建成功")

        logging.info(">>>>>点击「Webhook」")
        browser.click_element(AccessPage.webhook_info)

        logging.info(">>>>>点击「创建Webhook」")
        # sleep(5)
        browser.click_element(AccessPage.webhook_create)
        browser.send_text(AccessPage.webhook_name, webhook_name)
        browser.send_text(AccessPage.webhook_url, config.arch_web_url)
        browser.click_button(AccessPage.confirm)
        browser.check_loc("Webhook 创建成功")
        logging.info(">>>>>创建Webhook「%s」成功" % webhook_name)

        # 开始删除webhook
        self.delete_sso(sso_name, webhook_name)

    def login_setting(self):
        logging.info(">>>>>更新登录页配置")
        logging.info(">>>>>进入「登录页配置」界面")
        browser.click_element(SettingPage.login_setting)
        browser.click_button(SettingPage.edit)
        browser.text_clear(SettingPage.login_name)
        browser.send_text(SettingPage.login_name, "Log in")
        browser.text_clear(SettingPage.copyright)
        browser.send_text(SettingPage.copyright, "ui_test")
        browser.click_button(SettingPage.confirm)
        # browser.check_loc("配置更新成功")
        browser.check_loc("ui_test")
        logging.info(">>>>>配置成功成功")
        sleep(5)

    def webhook_setting(self):
        logging.info(">>>>>更新webhook设置")
        logging.info(">>>>>进入「设置」界面")
        browser.click_element(SettingPage.setting)

        logging.info(">>>>>设置自动清理")
        browser.click_button(SettingPage.auto_setting)
        browser.text_clear(SettingPage.max_days)
        browser.send_text(SettingPage.max_days, "100")
        browser.text_clear(SettingPage.max_logs)
        browser.send_text(SettingPage.max_logs, "1000")
        browser.click_button(SettingPage.confirm)
        browser.check_loc("自动清理设置成功")
        logging.info(">>>>>自动清理设置成功")

        logging.info(">>>>>设置手动清理")
        browser.click_button(SettingPage.clean_setting)
        browser.text_clear(SettingPage.specific_days)
        browser.send_text(SettingPage.specific_days, "10")
        browser.click_button(SettingPage.clean_confirm)
        browser.check_loc("清理 Webhook 记录成功")
        sleep(5)
        logging.info(">>>>>清理 Webhook 记录成功")

    def audit_setting(self):
        logging.info(">>>>>更新审计日志设置")
        logging.info(">>>>>进入「审计日志」界面")
        browser.click_element(AuditPage.audit)
        browser.click_element(AuditPage.setting)

        logging.info(">>>>>设置自动清理")
        browser.click_button(AuditPage.auto_setting)
        browser.text_clear(AuditPage.max_days)
        browser.send_text(AuditPage.max_days, "100")
        browser.text_clear(AuditPage.max_logs)
        browser.send_text(AuditPage.max_logs, "1000")
        browser.click_button(AuditPage.confirm)
        browser.check_loc("自动清理设置成功")
        logging.info(">>>>>自动清理设置成功")

        logging.info(">>>>>设置手动清理")
        browser.click_button(AuditPage.clean_setting, AuditPage.max_logs)
        browser.text_clear(AuditPage.specific_days)
        browser.send_text(AuditPage.specific_days, "10")
        browser.click_button(AuditPage.clean_confirm)
        # browser.check_loc("清理日志成功")
        sleep(5)
        logging.info(">>>>>清理日志成功")

    def ldap_check_clear(self):
        logging.info(">>>>>检查LDAP是否未接入")
        logging.info(">>>>>进入LDAP页面")
        browser.click_element(LdapPage.ldap)
        logging.info(">>>>>查找元素")
        browser.find_loc(LdapPage.no_ldap)
        logging.info(">>>>>LDAP未接入")
        sleep(5)

    def idp_check_clear(self):
        logging.info(">>>>>检查IDP是否未接入")
        logging.info(">>>>>进入IDP页面")
        browser.click_element(IdentifyPage.identity)
        logging.info(">>>>>查找元素")
        browser.find_loc(IdentifyPage.no_idp)
        logging.info(">>>>>IDP未接入")
        sleep(5)


if __name__ == "__main__":
    print("测试")
    obj = E2E()
    try:
        # obj.clear_ldap()
        # obj.close_browser()
        obj.login()
        # obj.create_user()
        # # obj.create_idp()
        # obj.create_ldap()
        obj.create_sso()
        # # obj.login_setting()
        # obj.audit_setting()
        # obj.webhook_setting()
    finally:
        # obj.clear_ldap_after()
        # obj.clear_idp()
        obj.close_browser()



