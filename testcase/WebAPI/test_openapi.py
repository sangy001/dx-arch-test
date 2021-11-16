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


@allure.feature("OpenAPI模块")
@pytest.mark.APITEST
class TestOpenAPI(object):

    # def setup_class(self):
    #     self.file_path = "Clients/"
    #     # ArchAPI.setup_class()

    @allure.story("创建webhook")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("OpenAPI/POST_product_client-webhooks.yml"))
    def test_post_product_client_webhooks(self, params):
        """
        :param params:
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("获取webhook信息")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("OpenAPI/GET_product_client-webhooks.yml"))
    def test_get_product_client_webhooks(self, params):
        """
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("获取webhook结构")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("OpenAPI/GET_product_client-webhook-struct.yml"))
    def test_get_product_client_webhook_struct(self, params):
        """
        :param params:
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("获取webhook详情")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("OpenAPI/GET_product_client-webhooks_id.yml"))
    def test_get_product_client_webhooks_id(self, params):
        """
        :param params:
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("修改webhook详情")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("OpenAPI/PUT_product_client-webhooks_id.yml"))
    def test_put_product_client_webhooks_id(self, params):
        """
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("删除webhook")
    @pytest.mark.run(order=-3)
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("OpenAPI/DELETE_product_client-webhooks_id.yml"))
    def test_delete_product_client_webhooks_id(self, params):
        """
        :param params:
        :return:
        """
        ArchAPI.exec_case(params)



if __name__ == "__main__":
    # logger.debug("查看角色信息")
    print("test")
    # ['test_PUT_product_client-webhooks_id.py', 'test_log.log', 'test_openapi.py',
    # 'test_DELETE_product_client-webhooks_id.py',
    # 'test_GET_product_client-webhook-struct.py',
    # 'test_POST_product_client-webhooks.py',
    # 'test_GET_product_client-webhooks.py', 'test_GET_product_client-webhooks_id.py']
    # file_dir = "/Users/min/Documents/DX-ARCH/web-api/testcase/WebAPI/OpenAPI"
    # for root, dirs, files in os.walk(file_dir):
    #     print(root)  # 当前目录路径
    #     print(dirs)  # 当前路径下所有子目录
    #     print(files)  # 当前路径下所有非目录子文件
