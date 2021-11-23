from common.ArchApiBase import ArchApiBase
from config.Config import Config
from common.AssertBase import Assertions
from common.ArchAPI import ArchAPI
from common.Log import Logger
import pytest
import os
import allure
# logger = Logger()
config = Config()
assertion = Assertions()
request = ArchApiBase()
ArchAPI = ArchAPI()
logger = Logger()

pytestmark = pytest.mark.APITEST


@allure.feature("当前用户模块")
@pytest.mark.APITEST
class TestAccount(object):

    # def setup_class(self):
    #     self.file_path = "Clients/"
    #     # ArchAPI.setup_class()

    # @pytest.mark.parametrize('params', ArchAPI.open_yaml("Account/PATCH_account.yml"))
    # def test_patch_account(self, params):
    #     """
    #     :param params:
    #     :return:
    #     """
    #     ArchAPI.exec_case(params)

    @allure.story("获取当前用户信息")
    # @allure.title("{params[describe]}")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Account/GET_account.yml"))
    def test_get_account(self, params):
        ArchAPI.exec_case(params)

    @allure.story("修改当前用户语言")
    # @allure.title("{params[describe]}")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Account/PUT_account_language.yml"))
    def test_put_account_language(self, params):
        ArchAPI.exec_case(params)

    # @pytest.mark.parametrize('params', ArchAPI.open_yaml("Account/PUT_account_set-password.yml"))
    # def test_put_account_set_password(self, params):
    #     """
    #     :param params:
    #     :return:
    #     """
    #     ArchAPI.exec_case(params)


if __name__ == "__main__":
    # logger.debug("查看角色信息")
    print("test")

