import pytest
import os



if __name__ == "__main__":

    # pytest.main(["-q", "./testcase/WebUI/", "--alluredir", "./temp"])

    # pytest.main(["-q", "./testcase/WebAPI/test_account.py", "--alluredir", "./temp"])

    # pytest.main(["-q", "./testcase/WebAPI/Clients/test_clients.py", "--alluredir", "./temp"])


    # 执行API的测试
    pytest.main(["-q", "./testcase/WebAPI/", "-m", "APITEST", "--alluredir", "./temp"])

    # 执行UI的测试
    pytest.main(["-q", "./testcase/WebUI/", "-m", "WEBTEST", "--alluredir", "./temp"])

    os.system('allure generate ./temp -o ./report --clean')
