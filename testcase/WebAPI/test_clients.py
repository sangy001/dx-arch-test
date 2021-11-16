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


@allure.feature("接入管理模块")
@pytest.mark.APITEST
class TestClients(object):

    # def setup_class(self):
    #     self.file_path = "Clients/"
    #     # ArchAPI.setup_class()
    @allure.story("创建客户端")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Clients/POST_admin_clients.yml"))
    def test_post_admin_clients(self, params):
        """
        创建sso
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("获取客户端列表")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Clients/GET_admin_clients.yml"))
    def test_get_admin_clients(self, params):
        """
        查看sso
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("获取客户端详情")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Clients/GET_admin_clients_id.yml"))
    def test_get_admin_clients_id(self, params):
        """
        查看clients详情
        :param params:
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("修改客户端详情")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Clients/PATCH_admin_clients_id.yml"))
    def test_patch_admin_clients_id(self, params):
        """
        修改clients详情
        :param params:
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("删除客户端")
    @pytest.mark.run(order=-2)
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Clients/DELETE_admin_clients_id.yml"))
    def test_delete_admin_clients_id(self, params):
        """
        删除clients
        :param params:
        :return:
        """
        ArchAPI.exec_case(params)



if __name__ == "__main__":
    # logger.debug("查看角色信息")
    print("test")
