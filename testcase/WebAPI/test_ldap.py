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


@allure.feature("用户目录模块")
@pytest.mark.APITEST
class TestLDAP(object):

    # def setup_class(self):
    #     self.file_path = "Clients/"
    #     # ArchAPI.setup_class()
    @allure.story("测试LDAP链接")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("LDAP/POST_ldap_test.yml"))
    def test_post_ldap_test(self, params):
        """
        ldap链接测试
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("接入LDAP")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("LDAP/POST_ldap.yml"))
    def test_post_ldap(self, params):
        """
        创建ldap
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("修改LDAP")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("LDAP/PUT_ldaps_id.yml"))
    def test_put_ldaps_id(self, params):
        """
        修改ldap信息
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("同步LDAP")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("LDAP/POST_ldaps_id_sync.yml"))
    def test_post_ldaps_id_sync(self, params):
        """
        同步ldap用户
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("获取LDAP信息")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("LDAP/GET_ldap.yml"))
    def test_get_ldap(self, params):
        """
        获取ldap信息
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("获取LDAP详情")
    @pytest.mark.run(order=-2)
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("LDAP/GET_ldaps_id_mappers.yml"))
    def test_get_ldaps_id_mappers(self, params):
        """
        获取ldap信息
        :return:
        """
        ArchAPI.exec_case(params)

    def teardown_class(self):
        """
        删除ldap
        :return:
        """
        ArchAPI.delete_keycloak_ldap()


if __name__ == "__main__":
    # logger.debug("查看角色信息")

    # ['test_PUT_ldaps_id.py', 'test_ldap.py', 'test_log.log', 'test_POST_ldap.py', 'test_POST_ldaps_id_sync.py',
    #  'test_POST_ldap_test.py', 'test_GET_ldap.py', 'test_GET_ldaps_id_mappers.py']
    print("test")
    file_dir = "/Users/min/Documents/DX-ARCH/web-api/testcase/WebAPI/LDAP"
    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件

