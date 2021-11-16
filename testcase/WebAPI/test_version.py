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


@allure.feature("版本信息模块")
@pytest.mark.APITEST
class TestVersion(object):

    # def setup_class(self):
    #     self.file_path = "Clients/"
    #     # ArchAPI.setup_class()

    @allure.feature("查看版本信息")
    @pytest.mark.parametrize('params', ArchAPI.open_yaml("Version/GET_version.yml"))
    def test_get_version(self, params):
        """
        查看角色类型
        :return:
        """
        ArchAPI.exec_case(params)


if __name__ == "__main__":
    # logger.debug("查看角色信息")
    print("test")




