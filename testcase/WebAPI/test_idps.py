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


@allure.feature("身份供应商模块")
@pytest.mark.APITEST
class TestIDPS(object):

    # def setup_class(self):
    #     self.file_path = "Clients/"
    #     # ArchAPI.setup_class()
    @allure.story("接入IDP")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("IDP/POST_idps.yml"))
    def test_post_admin_idps(self, params):
        """
        创建idps
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("获取IDP详情")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("IDP/GET_idps.yml"))
    def test_get_admin_idps(self, params):
        """
        获取idps信息
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("获取IDP协议")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("IDP/GET_idps_alias.yml"))
    def test_get_admin_idps_alias(self, params):
        """
        获取idps详情
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("获取IDP-URL")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("IDP/GET_redirect-url.yml"))
    def test_get_admin_redirect_url(self, params):
        """
        获取redirect_url信息
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("修改IDP")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("IDP/PUT_idps_alias.yml"))
    def test_put_admin_idps_alias(self, params):
        """
        修改idps信息
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("删除IDP")
    @pytest.mark.run(order=-2)
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("IDP/DELETE_idps_alias.yml"))
    def test_delete_admin_idps_alias(self, params):
        """
        删除idps信息
        :return:
        """
        ArchAPI.exec_case(params)





if __name__ == "__main__":
    # logger.debug("查看角色信息")
    print("test")
