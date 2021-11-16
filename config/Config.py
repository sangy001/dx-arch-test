
import configparser
import os
from filelock import FileLock


class Config:

    # titles:
    TITLE_ACCOUNT = "Account info"
    TITLE_ARCH = "Arch info"
    TITLE_KEYCLOAK = "Keycloak info"

    # values:
    # [Account info]
    VALUE_USERNAME = "username"
    VALUE_PASSWORD = "password"

    # [Arch info]
    VALUE_ARCH_WEB_URL = "arch_web_url"
    VALUE_ARCH_URL = "arch_url"
    VALUE_ARCH_CLIENT_ID = "arch_client_id"
    # VALUE_ARCH_CLIENT_SECRET = "arch_client_secret"
    # VALUE_ARCH_WEBHOOK_ID = "arch_webhook_id"
    #
    # VALUE_ARCH_TEST_CLIENT_ID = "arch_test_client_id"
    # VALUE_ARCH_TEST_CLIENT_SECRET = "arch_test_client_secret"
    # VALUE_ARCH_TEST_CLIENT_UUID = "arch_test_client_uuid"
    #
    # VALUE_ARCH_TEST_WEBHOOK_ID = "arch_test_webhook_id"
    #
    #
    # VALUE_ARCH_TEST_AUTH = "arch_test_auth"
    # VALUE_ARCH_TEST_USER_ID = "arch_test_user_id"
    #
    # VALUE_ARCH_TEST_USERNAME = "arch_test_username"
    # VALUE_ARCH_TEST_PASSWORD = "arch_test_password"

    VALUE_ARCH_TEST_IDP_TENANT_ID = "arch_test_idp_tenant_id"
    VALUE_ARCH_TEST_IDP_CLIENT_ID = "arch_test_idp_client_id"
    VALUE_ARCH_TEST_IDP_CLIENT_SECRET = "arch_test_idp_client_secret"
    # VALUE_ARCH_TEST_IDP_ID = "arch_test_idp_id"


    VALUE_ARCH_TEST_LDAP_HOST = "arch_test_ldap_host"
    VALUE_ARCH_TEST_LDAP_USER = "arch_test_ldap_user"
    VALUE_ARCH_TEST_LDAP_PASSWORD = "arch_test_ldap_password"
    VALUE_ARCH_TEST_LDAP_DN = "arch_test_ldap_dn"
    # VALUE_ARCH_TEST_LDAP_ID = "arch_test_ldap_id"


    # [Keycloak info]
    VALUE_KEYCLOAK_URL = "keycloak_url"
    VALUE_KEYCLOAK_REALM = "keycloak_realm"
    VALUE_KEYCLOAK_CLIENT_ID = "keycloak_client_id"

    # path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        """
        初始化
        """
        self.config = configparser.ConfigParser()
        self.config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        if not os.path.exists(self.config_path):
            raise FileNotFoundError("请确保配置文件存在！")

        self.config.read(self.config_path, encoding='utf-8')


        self.username = self.get_os_env("USERNAME", Config.TITLE_ACCOUNT, Config.VALUE_USERNAME)
        self.password = self.get_os_env("PASSWORD", Config.TITLE_ACCOUNT, Config.VALUE_PASSWORD)

        self.arch_web_url = self.get_os_env("ARCH_WEB_URL", Config.TITLE_ARCH, Config.VALUE_ARCH_WEB_URL)
        self.arch_url = self.get_os_env("ARCH_URL", Config.TITLE_ARCH, Config.VALUE_ARCH_URL)
        self.arch_client_id = self.get_os_env("ARCH_CLIENT_ID", Config.TITLE_ARCH, Config.VALUE_ARCH_CLIENT_ID)
        # self.arch_client_secret = self.get_os_env("ARCH_CLIENT_SECRET", Config.TITLE_ARCH, Config.VALUE_ARCH_CLIENT_SECRET)

        # self.arch_web_url = self.get_conf(Config.TITLE_ARCH, Config.VALUE_ARCH_WEB_URL)
        # self.arch_url = self.get_conf(Config.TITLE_ARCH, Config.VALUE_ARCH_URL)
        # self.arch_client_id = self.get_conf(Config.TITLE_ARCH, Config.VALUE_ARCH_CLIENT_ID)
        # self.arch_client_secret = self.get_conf(Config.TITLE_ARCH, Config.VALUE_ARCH_CLIENT_SECRET)

        self.arch_test_idp_tenant_id = self.get_os_env("ARCH_TEST_IDP_TENANT_ID",Config.TITLE_ARCH, Config.VALUE_ARCH_TEST_IDP_TENANT_ID)
        self.arch_test_idp_client_id = self.get_os_env("ARCH_TEST_IDP_CLIENT_ID", Config.TITLE_ARCH, Config.VALUE_ARCH_TEST_IDP_CLIENT_ID)
        self.arch_test_idp_client_secret = self.get_os_env("ARCH_TEST_IDP_CLIENT_SECRET", Config.TITLE_ARCH, Config.VALUE_ARCH_TEST_IDP_CLIENT_SECRET)
        # self.arch_test_idp_tenant_id = self.get_conf(Config.TITLE_ARCH, Config.VALUE_ARCH_TEST_IDP_TENANT_ID)
        # self.arch_test_idp_client_id = self.get_conf(Config.TITLE_ARCH, Config.VALUE_ARCH_TEST_IDP_CLIENT_ID)
        # self.arch_test_idp_client_secret = self.get_conf(Config.TITLE_ARCH, Config.VALUE_ARCH_TEST_IDP_CLIENT_SECRET)

        # self.arch_test_idp_id = self.get_conf(Config.TITLE_ARCH, Config.VALUE_ARCH_TEST_IDP_ID)

        self.arch_test_ldap_host = self.get_os_env("ARCH_TEST_LDAP_HOST", Config.TITLE_ARCH, Config.VALUE_ARCH_TEST_LDAP_HOST)
        self.arch_test_ldap_user = self.get_os_env("ARCH_TEST_LDAP_USER", Config.TITLE_ARCH, Config.VALUE_ARCH_TEST_LDAP_USER)
        self.arch_test_ldap_password = self.get_os_env("ARCH_TEST_LDAP_PASSWORD", Config.TITLE_ARCH, Config.VALUE_ARCH_TEST_LDAP_PASSWORD)
        self.arch_test_ldap_dn = self.get_os_env("ARCH_TEST_LDAP_DN", Config.TITLE_ARCH, Config.VALUE_ARCH_TEST_LDAP_DN)

        # self.arch_test_ldap_host = self.get_conf(Config.TITLE_ARCH, Config.VALUE_ARCH_TEST_LDAP_HOST)
        # self.arch_test_ldap_user = self.get_conf(Config.TITLE_ARCH, Config.VALUE_ARCH_TEST_LDAP_USER)
        # self.arch_test_ldap_password = self.get_conf(Config.TITLE_ARCH, Config.VALUE_ARCH_TEST_LDAP_PASSWORD)
        # self.arch_test_ldap_dn = self.get_conf(Config.TITLE_ARCH, Config.VALUE_ARCH_TEST_LDAP_DN)

        # self.arch_test_ldap_id = self.get_conf(Config.TITLE_ARCH, Config.VALUE_ARCH_TEST_LDAP_ID)
        self.keycloak_url = self.get_os_env("KEYCLOAK_URL", Config.TITLE_KEYCLOAK, Config.VALUE_KEYCLOAK_URL)
        self.keycloak_ream = self.get_os_env("KEYCLOAK_REALM", Config.TITLE_KEYCLOAK, Config.VALUE_KEYCLOAK_REALM)
        self.keycloak_client_id = self.get_os_env("KEYCLOAK_CLIENT_ID", Config.TITLE_KEYCLOAK, Config.VALUE_KEYCLOAK_CLIENT_ID)
        # self.keycloak_url = self.get_conf(Config.TITLE_KEYCLOAK, Config.VALUE_KEYCLOAK_URL)
        # self.keycloak_ream = self.get_conf(Config.TITLE_KEYCLOAK, Config.VALUE_KEYCLOAK_REALM)
        # self.keycloak_client_id = self.get_conf(Config.TITLE_KEYCLOAK, Config.VALUE_KEYCLOAK_CLIENT_ID)


    def get_os_env(self, env, title, value):
        if os.getenv(env) is None:
            return self.get_conf(title, value)
        else:
            return os.getenv(env)

    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)

        with FileLock(self.config_path):
            with open(self.config_path, "w+") as f:
                return self.config.write(f)

    def add_conf(self, title):
        """
        配置文件添加
        :param title:
        :return:
        """
        self.config.add_section(title)
        with FileLock(self.config_path):
            with open(self.config_path, "w+") as f:
                return self.config.write(f)
