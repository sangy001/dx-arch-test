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


@allure.feature("角色模块")
@pytest.mark.APITEST
class TestRoles(object):

    # def setup_class(self):
    #     self.file_path = "Clients/"
    #     # ArchAPI.setup_class()

    @allure.feature("查看角色列表")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Roles/GET_admin_roles.yml"))
    def test_get_admin_roles(self, params):
        """
        查看角色类型
        :return:
        """
        ArchAPI.exec_case(params)


if __name__ == "__main__":
    # logger.debug("查看角色信息")
    print("test")
