from common.ArchApiBase import ArchApiBase
from config.Config import Config
from common.AssertBase import Assertions
from common.ArchAPI import ArchAPI
from common.Log import Logger
import pytest
import allure

# logger = Logger()
config = Config()
assertion = Assertions()
request = ArchApiBase()
ArchAPI = ArchAPI()
logger = Logger()

pytestmark = pytest.mark.APITEST


@allure.feature("登录页配置")
@pytest.mark.APITEST
class TestLoginPage(object):

    # def setup_class(self):
    #     self.file_path = "Clients/"
    #     # ArchAPI.setup_class()

    @allure.story("获取的登录页配置信息")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("LoginPage/GET_login_page.yml"))
    def test_get_login_page(self, params):
        """
        获取页面配置信息
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("获取的登录页版本")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("LoginPage/GET_login_page_version.yml"))
    def test_get_login_page_version(self, params):
        """
        获取页面配置信息
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("获取登录页配置详情")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("LoginPage/GET_login_page_info.yml"))
    def test_get_login_page_info(self, params):
        """
        获取页面配置信息
        :param params:
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("修改登录页配置")
    @pytest.mark.run(order=-2)
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("LoginPage/PATCH_login_page.yml"))
    def test_patch_login_page(self, params):
        """
        修改页面配置信息
        :param params:
        :return:
        """
        ArchAPI.exec_case(params)




if __name__ == "__main__":
    # logger.debug("查看角色信息")
    print("test")
