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
class TestPortals(object):

    # def setup_class(self):
    #     self.file_path = "Clients/"
    #     # ArchAPI.setup_class()
    @allure.story("获取nav默认yaml")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Portals/GET_portal_product-nav_default-yaml.yml"))
    def test_get_portal_product_nav_default_yaml(self, params):
        """
        GET /portal/product-nav/default-yaml
        :param params:
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("获取顶部导航栏信息")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Portals/GET_portal_top-nav.yml"))
    def test_get_portal_top_nav(self, params):
        """
        GET /portal/top-nav
        :param params:
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("获取顶部导航栏详情")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Portals/GET_portal_top-nav_info.yml"))
    def test_get_portal_top_nav_info(self, params):
        """
        GET /portal/top-nav/info
        :param params:
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("获取nav详情")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Portals/GET_portal_product-nav_info.yml"))
    def test_get_portal_product_nav_info(self, params):
        """
        GET /portal/product-nav/info
        :param params:
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("获取nav-yaml")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Portals/GET_portal_product-nav_yaml.yml"))
    def test_get_portal_product_nav_yaml(self, params):
        """
        GET /portal/product-nav/yaml
        :param params:
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("修改nav信息")
    @pytest.mark.run(order=-2)
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Portals/PUT_portal_product-nav_yaml.yml"))
    def test_put_portal_product_nav_yaml(self, params):
        """
        PUT /portal/product-nav/yaml
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("修改顶部nav信息")
    @pytest.mark.run(order=-1)
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Portals/PATCH_portal_top-nav.yml"))
    def test_patch_portal_top_nav(self, params):
        """
        Patch /portal/top-nav
        :param params:
        :return:
        """
        ArchAPI.exec_case(params)


if __name__ == "__main__":
    # logger.debug("查看角色信息")
    print("test")