# 登录用户


import pytest
import base64
from common.ArchApiBase import ArchApiBase
from common.Log import Logger
from config.Config import Config
from common.ArchPage import E2E


import json

logger = Logger()
config = Config()
request = ArchApiBase()
e2e = E2E()

@pytest.mark.WEBTEST
class TestE2E(object):

    def setup_class(self):
        """
        :return:
        """
        logger.info(">>>>>>>>>>开始登录")
        e2e.login()
        logger.info(">>>>>>>>>>检查LDAP是否已经接入")
        e2e.ldap_check_clear()
        logger.info(">>>>>>>>>>检查IDP是否已经接入")
        e2e.idp_check_clear()

    def test_e2e(self):
        """
        :return:
        """
        logger.info(">>>>>>>>>>开始创建用户")
        e2e.create_user()
        logger.info(">>>>>>>>>>开始设置审计日志")
        e2e.audit_setting()
        logger.info(">>>>>>>>>>开始创建LDAP")
        e2e.create_ldap()
        logger.info(">>>>>>>>>>开始创建IDP")
        e2e.create_idp()
        logger.info(">>>>>>>>>>开始创建sso")
        e2e.create_sso()
        logger.info(">>>>>>>>>>开始设置登录页配置")
        e2e.login_setting()
        logger.info(">>>>>>>>>>开始设置webhook")
        e2e.webhook_setting()


    def teardown_class(self):
        logger.info(">>>>>>>>>>测试完成，开始清理环境")
        try:
            e2e.clear_idp()
            e2e.clear_ldap()
        finally:
            e2e.close_browser()


if __name__ == "__main__":
    print("Account")
    # logger.debug("Export Audit Logs")



