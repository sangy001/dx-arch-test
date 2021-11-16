from common.ArchApiBase import ArchApiBase
from config.Config import Config
from common.AssertBase import Assertions
from common.ArchAPI import ArchAPI
from common.Log import Logger
import pytest
import allure
import os

# logger = Logger()
config = Config()
assertion = Assertions()
request = ArchApiBase()
ArchAPI = ArchAPI()
logger = Logger()

pytestmark = pytest.mark.APITEST


@allure.feature("审计日志模块")
@pytest.mark.APITEST
class TestAudit(object):

    # def setup_class(self):
    #     self.file_path = "Clients/"
    #     # ArchAPI.setup_class()
    @allure.story("设置自动清理")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Audit/POST_admin_audit_clean.yml"))
    def test_post_admin_audit_clean(self, params):
        """
        :param params:
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("导出审计日志")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Audit/GET_admin_audit_export.yml"))
    def test_get_admin_audit_export(self, params):
        """
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("获取审计日志配置")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Audit/GET_admin_audit_prune-policy.yml"))
    def test_get_admin_audit_prune_policy(self, params):
        """
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("修改审计日志配置")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Audit/PUT_admin_audit_prune-policy.yml"))
    def test_put_admin_audit_prune_policy(self, params):
        """
        :param params:
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("获取审计日志信息")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Audit/GET_admin_audit_logs.yml"))
    def test_get_admin_audit_logs(self, params):
        """
        :param params:
        :return:
        """
        ArchAPI.exec_case(params)



if __name__ == "__main__":
    # logger.debug("查看角色信息")
    print("test")
    # ['test_GET_admin_audit_export.py', 'test_log.log', 'test_GET_admin_audit_prune-policy.py',
    # 'test_POST_admin_audit_clean.py', 'test_PUT_admin_audit_prune-policy.py',
    # 'test_GET_admin_audit_logs.py', 'test_audit.py']
