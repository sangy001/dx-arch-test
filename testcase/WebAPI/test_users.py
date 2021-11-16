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


@allure.feature("用户管理模块")
@pytest.mark.APITEST
class TestUsers(object):

    # def setup_class(self):
    #     self.file_path = "Clients/"
    #     # ArchAPI.setup_class()

    @allure.story("创建用户")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Users/POST_admin_users.yml"))
    def test_post_admin_users(self, params):
        """
        创建用户
        :param params:
        :return:
        """
        ArchAPI.exec_case(params)

    # @pytest.mark.skip()
    # @pytest.mark.parametrize('params', ArchAPI.open_yaml("Users/POST_admin_users_id_federated-identities.yml"))
    # def test_post_admin_users_id_federated(self, params):
    #     ArchAPI.exec_case(params)

    @allure.story("获取用户详情")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Users/GET_admin_users_id.yml"))
    def test_get_admin_users_id(self, params):
        """
        获取用户信息
        :param params:
        :return:
        """
        ArchAPI.exec_case(params)

    @allure.story("获取用户的权限")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Users/GET_admin_users_id_permissions.yml"))
    def test_get_admin_users_id_permissions(self, params):
        ArchAPI.exec_case(params)

    @allure.story("获取用户列表")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Users/GET_admin_users.yml"))
    def test_get_admin_users(self, params):
        ArchAPI.exec_case(params)

    @allure.story("获取用户身份认证")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Users/GET_admin_users_id_federated-identities.yml"))
    def test_get_admin_users_id_federated(self, params):
        ArchAPI.exec_case(params)

    @allure.story("获取用户角色")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Users/GET_admin_users_id_roles.yml"))
    def test_get_admin_users_id_roles(self, params):
        ArchAPI.exec_case(params)

    @allure.story("修改用户密码")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Users/PUT_admin_users_id_set-password.yml"))
    def test_put_admin_users_id_set_password(self, params):
        ArchAPI.exec_case(params)

    @allure.story("修改用户详情")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Users/PATCH_admin_users_id.yml"))
    def test_patch_admin_users_id(self, params):
        ArchAPI.exec_case(params)

    @allure.story("设置用户角色")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Users/PUT_admin_users_id_set-roles.yml"))
    def test_put_admin_users_id_set_roles(self, params):
        ArchAPI.exec_case(params)

    @allure.story("删除用户")
    @pytest.mark.run(order=-2)
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Users/DELETE_admin_users_id.yml"))
    def test_delete_admin_users_id(self, params):
        ArchAPI.exec_case(params)

    # @pytest.mark.skip()
    # @pytest.mark.parametrize('params', ArchAPI.open_yaml("Users/DELETE_admin_users_id_federated-identities_alias.yml"))
    # def test_delete_admin_users_id_federated(self, params):
    #     ArchAPI.exec_case(params)


if __name__ == "__main__":
    # logger.debug("查看角色信息")
    print("test")
    # ['test_GET_admin_users_id.py', 'test_POST_admin_users_id_federated-identities.py', 'test_log.log',
    # 'test_GET_admin_users_id_roles.py', 'test_DELETE_admin_users_id.py',
    # 'test_DELETE_admin_users_id_federated-identities_alias.py',
    # 'test_PUT_admin_users_id_set-password.py', 'test_PATCH_admin_users_id.py',
    # 'test_POST_admin_users.py', 'test_GET_admin_users_id_permissions.py',
    # 'test_users.py', 'test_GET_admin_users.py', 'test_GET_admin_users_id_federated-identities.py',
    # 'test_PUT_admin_users_id_set-roles.py']
    # file_dir = "/Users/min/Documents/DX-ARCH/web-api/testcase/WebAPI/Users"
    # for root, dirs, files in os.walk(file_dir):
    #     print(root)  # 当前目录路径
    #     print(dirs)  # 当前路径下所有子目录
    #     print(files)  # 当前路径下所有非目录子文件

