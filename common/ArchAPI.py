import requests
import random
import string
import json
from common.ArchApiBase import ArchApiBase
from config.Config import Config
from common.AssertBase import Assertions
import jsonpath
from common.Log import Logger
import pytest
import yaml
import os
import time
import base64
from keycloak import KeycloakAdmin, KeycloakOpenID

config = Config()
logger = Logger()
assertion = Assertions()
# auth = None


class ArchAPI(ArchApiBase):

    # @classmethod
    def open_yaml(self, file):
        path = os.path.join(os.getcwd(), "data/WebAPI", file)
        logger.info("参数文件信息位置：%s" % path)
        return yaml.safe_load(open(path, encoding='UTF-8'))

    def assignment_yaml(self, params):

        for key, value in params.items():
            # print(key, value)

            # if type(value) is dict:
            #     self.assignment_yaml(value)  # 递归，返回都是key，value的形式
            # else:
            if key == "header":
                logger.debug("解析heaer")
                params[key] = self.assignment_header(value)

            elif key == "path":
                logger.debug("解析path")
                params[key] = self.assignment_path(value)

            elif key == "body":
                logger.debug("解析body")
                if value:
                    params[key] = self.assignment_body(value)

            elif key == "query":
                if value:
                    params[key] = self.assignment_query(value)

                # if value == "AUTH":
                #     if getattr(self, 'auth') == None:
                #         self.get_arch_auth()
                #         params[key] = getattr(self, 'auth')
                # elif value == "NAME":
                #     params[key] = name.lower()
            else:
                pass
        return params

    def assignment_path(self, path):
        """
        解析path
        :param path:
        :return:
        """
        while "{" in path:
            if "CLIENT_ID" in path:
                CLIENT_UUID,  CLIENT_SECRET, CLIENT_ID = self.get_client_id()
                path = path.replace("{CLIENT_ID}", CLIENT_UUID)
            elif "ALIAS" in path:
                ALIAS = "OIDC"
                path = path.replace("{ALIAS}", ALIAS)
            elif "LDAP_ID" in path:
                LDAP_ID = self.get_ldap_id()
                path = path.replace("{LDAP_ID}", LDAP_ID)
            elif "USER_ID" in path:
                USER_ID = self.get_user_id()
                path = path.replace("{USER_ID}", USER_ID)
            elif "WEBHOOK_ID" in path:
                WEBHOOK_ID = self.get_webhook_id()
                path = path.replace("{WEBHOOK_ID}", WEBHOOK_ID)
            else:
                pass
        logger.debug("path:%s" % path)

        return path

    def assignment_query(self, query):
        """
        :param query:
        :return:
        """
        NAME = ''.join(random.sample(string.ascii_letters + string.digits, 5))
        PLATFORM_NAME = "DaoCloud_" + NAME
        if query is None:
            return query
        else:
            for key, value in query.items():
                if value == "PLATFORM_NAME":
                    query[key] = PLATFORM_NAME
                else:
                    query[key] = value
            return query

    def assignment_header(self, header):
        """
        解析header
        :param header:
        :return:
        """

        _header = {
            "Accept-Language": "zh-CN",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        if header is None:
            return _header
        else:
            for key, value in header.items():
                if value == "AUTH":
                        # auth = self.arch_temp_info["arch_auth"]
                        # header = self._headers
                        # if auth is None:
                        #     header["Authorization"] = "Bearer " + self.get_arch_auth()
                        # else:
                        #     header["Authorization"] = "Bearer " + auth
                        # return header

                    AUTH = self.arch_temp_info["arch_auth"]
                    if AUTH is None:
                        _header["Authorization"] = "Bearer " + self.get_arch_auth()
                    else:
                        _header["Authorization"] = "Bearer " + AUTH

                    # if getattr(self, 'auth') == None:
                    #     self.get_arch_auth()
                    #     _header[key] = getattr(self, 'auth')
                elif value == "TOKEN":
                    CLIENT_UUID, CLIENT_SECRET, CLIENT_ID = self.get_client_id()
                    CLIENT_SECRET = self.get_client_secret(CLIENT_UUID)
                    token = "%s:%s" % (CLIENT_ID, CLIENT_SECRET)
                    bytes_auth = token.encode("utf-8")
                    final_token = bytes.decode(base64.b64encode(bytes_auth))
                    _header["Authorization"] = "Basic " + final_token
                elif value == "multipart/form-data":
                    del _header["Content-Type"]
                else:
                    _header[key] = value
            logger.debug("_header:%s" % _header)
            return _header

    def assignment_body(self, body):
        """
        解析body
        :param body:
        :return:
        """
        NAME = ''.join(random.sample(string.ascii_letters + string.digits, 5))
        EMAIL = NAME.lower() + "@163.com"

        IDP_TENANT_ID = config.arch_test_idp_tenant_id
        IDP_CLIENT_ID = config.arch_test_idp_client_id
        IDP_CLIENT_SECRET = config.arch_test_idp_client_secret

        LDAP_HOST = config.arch_test_ldap_host
        LDAP_USER = config.arch_test_ldap_user
        LDAP_PASSWORD = config.arch_test_ldap_password
        LDAP_DN = config.arch_test_ldap_dn

        TIME = int(time.time() - 30 * 24 * 60 * 60)

        PLATFORM_NAME = "Login_" + NAME

        if type(body) is str and body == "PORTAL_YAML":

            PORTAL_YAML ='categories:\n' \
                         '- name: Cloud Engine\n' \
                         '  enName: Cloud Engine\n' \
                         '  cnName: zh-Cloud Engine\n' \
                         '  menus:\n' \
                         '  - name: Container Management\n' \
                         '    enName: Container Management\n' \
                         '    cnName: zh-Container Management\n' \
                         '    url: https://www.daocloud.io/\n' \
                         '    iconName: dce\n'

            # print("body is str: %s" % str(PORTAL_YAML))
            logger.info("body is str: %s" % str(PORTAL_YAML))
            return str(PORTAL_YAML)

        for key, value in body.items():
            if type(value) is dict:
                self.assignment_body(value)  # 递归，返回都是key，value的形式
            else:
                if value == "NAME":
                    body[key] = NAME.lower()

                elif value == "CLIENT_NAME":
                    body[key] = "edit_" + NAME.lower()

                elif value == "IDP_NAME":
                    body[key] = "robot_" + NAME.lower()

                elif type(value) is str and "IDP_TENANT_ID" in value:
                    body[key] = value.replace("{IDP_TENANT_ID}", IDP_TENANT_ID)

                elif value == "IDP_CLIENT_ID":
                    body[key] = IDP_CLIENT_ID

                elif value == "IDP_CLIENT_SECRET":
                    body[key] = IDP_CLIENT_SECRET

                elif value == "LDAP_PASSWORD":
                    body[key] = LDAP_PASSWORD

                elif value == "LDAP_HOST":
                    body[key] = LDAP_HOST

                elif value == "LDAP_USER":
                    body[key] = LDAP_USER

                elif value == "LDAP_DN":
                    body[key] = LDAP_DN

                elif key == "connection_url":
                    body[key] = value.replace("{LDAP_HOST}", LDAP_HOST)

                elif value == "LDAP_ID":
                    LDAP_ID = self.get_ldap_id()
                    body[key] = LDAP_ID

                elif value == "PLATFORM_NAME":
                    body[key] = PLATFORM_NAME

                elif value == "EMAIL":
                    body[key] = EMAIL

                elif value == "TIME":
                    body[key] = TIME

                else:
                    pass
        logger.debug("body:%s" % body)
        return body

    def assignment_response(self, response):
        if isinstance(response, dict):
            _response = response
            _type = 'dict'
        elif isinstance(response, list):
            _response = response[0]
            _type = 'list'
        else:
            return response

        if _type == 'list':
            return [_response]
        return _response


    def exec_case(self, params):

        params = self.assignment_yaml(params)
        url = config.arch_url + params['path']
        header = params["header"]
        query = params["query"]
        expected_status_code = params["status_code"]
        expected_response = params["response"]

        if type(params["body"]) is str:

            data = params["body"]
        else:

            data = json.dumps(params["body"])

        if params['method'] == "GET":
            response = self._get(url=url, headers=header, query=query)

        elif params['method'] == "POST":
            response = self._post(url=url, headers=header, data=data, query=query)

        elif params['method'] == "PUT":
            response = self._put(url=url, headers=header, data=data, query=query)

        elif params['method'] == "HEAD":
            response = self._head(url=url, headers=header, query=query)

        elif params['method'] == "PATCH":
            response = self._patch(url=url, headers=header, data=data, query=query)

        elif params['method'] == "DELETE":
            data = {}
            response = self._delete(url=url, headers=header, data=data, query=query)
        else:
            logger.info("不支持method: %s" % params['method'])


        # 输出响应
        logger.info(u'状态码 %s' % response.status_code)
        try:
            logger.info(u'响应值 %s' % response.json())
        except Exception as e:
            # logger.debug(e)
            logger.info(u'响应值 %s' % response.text)

        # 验证状态码
        logger.info(u'预期状态码: %s' % expected_status_code)
        assertion.assert_code(response.status_code, expected_status_code)

        # 验证响应值
        logger.info(u'预期响应值: %s' % expected_response)
        assertion.assert_body_msg(response, expected_response)


    def get_keycloak_auth(self):
        """
        获取keycloak的auth
        :param body:
        :param expected_msg:
        :return:
        """
        server_url = self.keycloak_url + "/auth/"
        keycloak_openid = KeycloakOpenID(server_url=server_url,
                                         client_id=config.keycloak_client_id,
                                         realm_name="master")
        token = keycloak_openid.token(config.username, config.password)
        # "keycloak_client_secret": None,
        # "keycloak_auth": None
        self.arch_temp_info['keycloak_auth'] = token["access_token"]
        return token["access_token"]

    def get_keycloak_client_secret(self):
        # "http://10.10.121.11:30035/auth/admin/realms/dx-arch/clients?first=0&max=20&search=true"
        path = "/auth/admin/realms/%s/clients" % self.keycloak_realm
        param = {
            "clientId": "dx",
            "search": True,
            "first": 0,
            "max": 20
        }
        url = self.keycloak_url + path
        header = self._headers
        header["Authorization"] = "Bearer " + self.get_keycloak_auth()

        # print(header)
        # print(url)
        response = self._get(url=url, headers=header, query=param)
        # print("=======")
        # print(response.json())
        # print(response.json()[0]["id"])
        if response.status_code == 200:
            arch_client_uuid = response.json()[0]["id"]
            path = "/auth/admin/realms/%s/clients/%s/client-secret" % (self.keycloak_realm, arch_client_uuid)
            _get_secret_url = self.keycloak_url + path
            _response = self._get(url=_get_secret_url, headers=header)
            self.arch_temp_info['keycloak_client_secret'] = _response.json()["value"]
            return _response.json()["value"]

        else:
            logger.debug("获取keycloak_client_secret出现了错误")


    def delete_keycloak_ldap(self):
        path = "/auth/admin/realms/%s/components" % self.keycloak_realm
        param = {
            "parent": "dx-arch",
            "type": "org.keycloak.storage.UserStorageProvider"

        }
        url = self.keycloak_url + path
        header = self._headers

        header["Authorization"] = "Bearer " + self.get_keycloak_auth()
        response = self._get(url=url, headers=header, query=param)

        ldap_list = response.json()
        # 如果有ldap，则删除
        while(len(ldap_list)!=0):
            for i in response.json():
                # print(i)
                id = i["id"]
                _del_path = "/auth/admin/realms/%s/components/%s" % (self.keycloak_realm, id)
                _url = self.keycloak_url + _del_path
                _body = {}
                _response = self._delete(url=_url, headers=header, data=_body)
                if _response.status_code == 204:
                    ldap_list.remove(i)
                else:
                    return False

        return True



    def get_arch_auth(self):
        """
        获取arch的auth
        目前只能用__internal-dx-arch和secret 获取arch
        :return:
        """
        path = "/.well-known/openid-configuration"
        url = self.arch_url + path
        response = self._get(url=url, headers=self._headers)

        if response.status_code == 200:
            _arch_auth_url = response.json()['token_endpoint']

            _param = {
              "scope": "openid email profile"
            }

            if self.arch_temp_info["keycloak_client_secret"] is None:
                arch_client_secret = self.get_keycloak_client_secret()
            else:
                arch_client_secret = self.arch_temp_info["keycloak_client_secret"]

            _body = {
                "grant_type": "password",
                "client_id": config.arch_client_id,
                "client_secret": arch_client_secret,
                "username": config.username,
                "password": config.password
            }

            _header = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json"
            }

            _response = self._post(url=_arch_auth_url, headers=_header, data=_body, query=_param)

            if _response.status_code == 200:
                self.arch_temp_info["arch_auth"] = _response.json()["id_token"]
                return _response.json()["id_token"]
            else:
                logger.debug("获取arch token出现了错误")
                # print("Something is wrong")

        else:
            logger.debug("获取arch token url出现了错误")
            # print("Something is wrong")

            # print(response.json())

    def get_arch_header(self):

        auth = self.arch_temp_info["arch_auth"]
        header = self._headers
        if auth is None:
            header["Authorization"] = "Bearer " + self.get_arch_auth()
        else:
            header["Authorization"] = "Bearer " + auth
        return header


    def get_client_id(self):
        """
        获取client_id,如果不存在，则创建一个
        :return:
        """
        client_list = self.get_client_list()
        if len(client_list["data"]) == 0:
            logger.info("client列表为空")
            client_uuid, client_secret, client_id = self.create_client_id()
            logger.info("创建client, client_uuid为 %s" % client_uuid)
            return client_uuid, client_secret, client_id
        else:
            client_uuid = client_list["data"][0]["id"]
            client_secret = client_list["data"][0]["secret"]
            client_id = client_list["data"][0]["client_id"]
            logger.info("获取client, client_uuid为 %s" % client_uuid)
            self.arch_temp_info['client_uuid'] = client_uuid
            self.arch_temp_info['client_secret'] = client_secret
            self.arch_temp_info['client_id'] = client_id
            return client_uuid, client_secret, client_id

    def get_client_list(self):
        """
        获取sso列表
        :return:
        """
        path = "/admin/clients"
        url = self.arch_url + path
        header = self.get_arch_header()
        param = {
            "size": -1
        }
        # Authorization = "Bearer " + self.get_arch_auth()

        # auth = self.arch_temp_info["arch_auth"]
        # if auth is None:
        #     header["Authorization"] = "Bearer " + self.get_arch_auth()
        # else:
        #     header["Authorization"] = "Bearer " + auth

        response = self._get(url=url, headers=header, query=json.dumps(param))
        try:
            assert response.status_code == 200, logger.info("获取client列表失败")
        except AssertionError:
            logger.error("返回错误: %s" % response.text)
        else:
            logger.info("获取client列表成功: %s" % response.content)

        return response.json()

    def create_client_id(self):
        """
        创建测试sso
        :return:
        """
        client_name = ''.join(random.sample(string.ascii_letters + string.digits, 5))

        path = "/admin/clients"
        url = self.arch_url + path
        header = self.get_arch_header()
        # header = self._headers
        # header["Authorization"] = "Bearer " + self.get_arch_auth()
        body = {
            "client_id": client_name.lower(),
            "enabled": True,
            "name": client_name.lower()
        }
        response = self._post(url=url, headers=header, data=json.dumps(body))

        try:
            assert response.status_code == 200, print("something is wrong")
        except AssertionError:
            print("返回错误: %s" % response.text)
        else:
            print("创建sso成功: %s" % response.content)
            client_secret = response.json()["secret"]
            client_uuid = response.json()["id"]
            client_id = response.json()["client_id"]
            self.arch_temp_info['client_uuid'] = client_uuid
            self.arch_temp_info['client_secret'] = client_secret
            self.arch_temp_info['client_id'] = client_id
            return client_uuid, client_secret, client_id

    def get_ldap_id(self):
        """
        获取ldap_id, 如果不存在则创建
        :return:
        """
        response = self.get_ldap_info()
        if response.status_code == 200:
            self.arch_temp_info['ldap_id'] = response.json()["id"]
            return response.json()["id"]
        else:
            create_response = self.create_ldap()
            if create_response.status_code == 201:
                get_response = self.get_ldap_info()
                # print(get_response.json())
                self.arch_temp_info['ldap_id'] = get_response.json()["id"]
                return get_response.json()["id"]


        #
        # path = "/admin/ldap"
        # url = config.arch_url + path
        # header = self._headers
        # header["Authorization"] = "Bearer " + self.get_arch_auth()
        # response = self._get(url=url, headers=header)
        # try:
        #     assert response.status_code == 200, logger.debug("ldap不存在")
        # except AssertionError:
        #     logger.debug("返回错误：%s" % response.text)
        # else:
        #     return response.json()["id"]

    def test_ldap_conn(self):
        """
        测试ldap链接
        :return:
        """
        # 测试链接
        header = self.get_arch_header()

        # header = self._headers
        # header["Authorization"] = "Bearer " + self.get_arch_auth()
        url = self.arch_url + "/admin/ldap-test"
        body = {
            "action": "testAuthentication",
            "bind_credential": config.arch_test_ldap_password,
            "bind_dn": config.arch_test_ldap_user,
            "component_id": "",
            "connection_timeout": "300",
            "connection_url": "ldap://" + config.arch_test_ldap_host,
            "start_tls": "false",
            "use_truststore_spi": "ldapsOnly"
        }

        # 测试能否链接成功
        response = self._post(url=url, headers=header, data=json.dumps(body))
        return response

    def get_ldap_info(self):
        """
        获取ldap信息
        :return:
        """
        path = "/admin/ldap"
        url = config.arch_url + path
        header = self.get_arch_header()
        # header = self._headers
        # header["Authorization"] = "Bearer " + self.get_arch_auth()
        response = self._get(url=url, headers=header)
        # print("ldap信息：%s" % response.json())
        return response

    def create_ldap(self):

        """
        判断ldap是否存在
        如果存在，修改config，
        如果不存在，创建ldap，并修改config
        :return:
        """
        path = "/admin/ldap"
        url = self.arch_url + path
        header = self.get_arch_header()
        # header = self._headers
        # header["Authorization"] = "Bearer " + self.get_arch_auth()
        body = {
            "bind_credential": config.arch_test_ldap_password,
            "bind_dn": config.arch_test_ldap_user,
            "full_sync_period": "-1",
            "ldap_host": config.arch_test_ldap_host,
            "ldap_protocol": "ldap",
            "name": "ldap",
            "provider_type": "other",
            "start_tls": "false",
            "user_object_classes": "inetOrgPerson, organizationalPerson",
            "username_ldap_attribute": "uid",
            "users_dn": config.arch_test_ldap_dn
        }
        response = self._post(url=url, headers=header, data=json.dumps(body))

        return response

    def get_client_secret(self, client_uuid):
        """
        :return:
        """
        path = "/admin/clients/" + client_uuid
        url = self.arch_url + path
        header = self.get_arch_header()
        # header = self._headers
        # header["Authorization"] = "Bearer " + self.get_arch_auth()
        response = self._get(url=url, headers=header)
        try:
            assert response.status_code == 200, print("something is wrong")
        except AssertionError:
            print("返回错误: %s" % response.text)
        else:
            print("获取webhook列表成功: %s" % response.content)

        self.arch_temp_info['client_secret'] = response.json()["secret"]

        return response.json()["secret"]


    def get_webhook_id(self):
        """
        :return:
        """
        CLIENT_UUID, CLIENT_CECRET, CLIENT_ID = self.get_client_id()
        webhook_list = self.get_webhook_list(CLIENT_UUID)
        if webhook_list['data'] is None:
            webhook_uuid = self.create_webhook(CLIENT_UUID)
            self.arch_temp_info['webhook_uuid'] = webhook_uuid
            return webhook_uuid

        else:
            self.arch_temp_info['webhook_uuid'] = webhook_list['data'][0]['id']
            return webhook_list['data'][0]['id']



    def get_webhook_list(self, client_uuid):
        """
        获取webhook_list
        :return:
        """
        path = "/admin/client-webhooks"
        url = self.arch_url + path
        header = self.get_arch_header()
        # header = self._headers
        # header["Authorization"] = "Bearer " + self.get_arch_auth()

        param = {
            "client_id": client_uuid
        }
        response = self._get(url=url, headers=header, query=param)
        try:
            assert response.status_code == 200, print("something is wrong")
        except AssertionError:
            print("返回错误: %s" % response.text)
        else:
            print("获取webhook列表成功: %s" % response.content)

        return response.json()

    # def judge_webhook_exist(self, webhook_uuid):
    #     """
    #     判断webhook是否存在
    #     :return:
    #     """
    #     uuid_list = []
    #     webhook_list = self.get_webhook_list()
    #     # webhook_uuid = config.get_conf("Arch info", "arch_test_webhook_id")
    #     # if len(webhook_list["data"]) == 0 or webhook_list["data"] == None:
    #     if webhook_list["data"] == None:
    #         return False
    #     else:
    #         for i in range(0, len(webhook_list["data"])):
    #             result = jsonpath.jsonpath(webhook_list, '$.data[' + str(i) + '].id')  # 取到data里的第i个元素中的id
    #             uuid_list.extend(result)
    #         return webhook_uuid in uuid_list

    def create_webhook(self, client_uuid):
        """
        创建webhook
        :return:
        """
        webhook_name = ''.join(random.sample(string.ascii_letters + string.digits, 5))
        path = "/admin/client-webhooks"
        url = self.arch_url + path
        header = self.get_arch_header()
        # header = self._headers
        # header["Authorization"] = "Bearer " + self.get_arch_auth()
        # client_id = config.get_conf("Arch info", "arch_test_client_uuid")
        body = {
                "action": "CREATE",
                "client_id": client_uuid,
                "content_type": "application/json",
                "custom_json_data": "{\"id\": \"{{$$.ID$$}}\"}",
                "form_data": [],
                "headers": {
                    "test_action": "get",
                },
                "is_custom_content": True,
                "method": "GET",
                "name": webhook_name.lower(),
                "resource_type": "User",
                "url": "http://10.10.121.1"
            }

        response = self._post(url=url, headers=header, data=json.dumps(body))

        try:
            assert response.status_code == 200, print("something is wrong")
        except AssertionError:
            print("返回错误: %s" % response.text)
        else:
            print("创建webhook成功: %s" % response.content)
                # arch_test_webhook_id = response.json()["id"]
                # config.set_conf("Arch info", "arch_test_webhook_id", arch_test_webhook_id)
                # config.arch_test_webhook_id = arch_test_webhook_id
            return response.json()["id"]
        # else:
        #     return webhook_uuid
        # webhook_uuid = config.get_conf("Arch info", "arch_test_webhook_id")
        # try:
        #     assert self.judge_sso_exist(webhook_uuid), print("webhook_uuid 不存在")
        # except AssertionError:


    # def confirm_sso_info(self)
    def set_password(self, user_id):
        """
        创建密码
        :param user_id:
        :return:
        """
        path = "/admin/users/%s/set-password" % user_id
        url = self.arch_url + path

        header = self.get_arch_header()
        # header = self._headers
        # header["Authorization"] = "Bearer " + self.get_arch_auth()
        body = {
            "confirm_password": "Danger0us",
            "password": "Danger0us",
            "temporary": False
        }
        response = self._put(url=url, headers=header, data=json.dumps(body))
        # config.set_conf("Arch info", "arch_test_password", "Danger0us")
        return True if response.status_code == 200 else False

    def create_user(self):
        """
        创建用户
        :return:
        """
        path = "/admin/users"
        url = self.arch_url + path
        header = self.get_arch_header()
        # header = self._headers
        # header["Authorization"] = "Bearer " + self.get_arch_auth()
        last_name = ''.join(random.sample(string.ascii_letters + string.digits, 5))

        body = {
                "email": last_name.lower() + "@163.com",
                "enabled": True,
                "first_name": "arch",
                "last_name": last_name.lower(),
                "username": "arch"+last_name.lower()
            }

        response = self._post(url=url, headers=header, data=json.dumps(body))
        if response.status_code == 200:
            self.set_password(response.json()["id"])
            self.arch_temp_info['user_id'] = response.json()["id"]
            self.arch_temp_info['user_name'] = response.json()["username"]
            return response.json()["id"]
        else:
            return False

    def user_list(self):
        """
        查看用户列表
        :param user_id:
        :return:
        """
        path = "/admin/users"
        url = self.arch_url + path
        header = self.get_arch_header()
        # header = self._headers
        # header["Authorization"] = "Bearer " + self.get_arch_auth()

        response = self._get(url=url, headers=header)
        if response.status_code == 200:
            return response.json()
        else:
            return False

    def get_user_id(self):
        userList = self.user_list()
        if userList is False:
            logger.error("获取用户列表失败")
            return False
        else:
            if len(userList["data"]) > 1:
                self.arch_temp_info['user_id'] = userList["data"][1]["id"]
                return userList["data"][1]["id"]
            else:
                return self.create_user()

    #
    # def judge_user_exist(self, user_id):
    #     """
    #     判断webhook是否存在
    #     :return:
    #     """
    #     user_id_list = []
    #     user_list = self.user_list()
    #     # webhook_uuid = config.get_conf("Arch info", "arch_test_webhook_id")
    #     # if len(user_list["data"]) == 0:
    #     if user_list["data"] == None:
    #         return False
    #     else:
    #         for i in range(0, len(user_list["data"])):
    #             result = jsonpath.jsonpath(user_list, '$.data[' + str(i) + '].id')  # 取到data里的第i个元素中的id
    #             user_id_list.extend(result)
    #         return user_id in user_id_list


    def judge_ldap_exist(self, ldap_id):
        response = self.get_ldap_info()
        print("配置中的ldapid:%s" % ldap_id)
        if response.status_code == 204:
            return False
        else:
            print("获取的ldapid:%s" % response.json()["id"])
            if response.json()["id"] == ldap_id:
                return True
            else:
                return False




if __name__ == "__main__":
    print("test")
    obj = ArchAPI()
    print(obj.delete_keycloak_ldap())
    # print(obj.get_ldap_id())

    # obj.create_client()
    # obj.get_keycloak_auth()
    # obj.create_client()
    # obj.test()
    # obj.get_arch_auth()
    # obj.get_sso()
    # obj.judge_sso_exist("b79d7510-b0d9-4b0c-b601-9fed23812190")
    # print(obj.create_sso())
    # print(obj.create_webhook())
    # obj.create_ldap()
    # ldap_id = config.arch_test_ldap_id
    # result = obj.judge_ldap_exist(ldap_id)
    # print(result)
    # f = open(r'../data/WebAPI/Account/GET_account.yml')
    # params = yaml.load(f, Loader=yaml.FullLoader)
    # print(params[0])
    # obj.setup_class()
    # test = obj.assignment_yaml(params[0])
    # print(test)
    # r = '/Users/min/Documents/DX-ARCH/web-api/data/WebAPI/Clients/POST_admin_clients.yml'
    # obj.open_yaml(r)

    # r = '/Users/min/Documents/DX-ARCH/web-api/data/WebAPI/Version/GET_version.yml'
    # params = yaml.safe_load(open(r, encoding='UTF-8'))

    # obj.get_keycloak_client_secret()

    # keycloak_admin = KeycloakAdmin(server_url="http://10.6.121.51:30035/auth/",
    #                                username='admin',
    #                                password='changeme',
    #                                # realm_name="master",
    #                                # user_realm_name="dx-arch",
    #                                verify=True)
    #
    # count_users = keycloak_admin.users_count()
    # realm_roles = keycloak_admin.get_realm_roles()
    #
    #
    # print(keycloak_admin)
    # print(count_users)
    # print(realm_roles)


    # keycloak_openid = KeycloakOpenID(server_url="http://10.6.121.51:30035/auth/",
    #                                  client_id="admin-cli",
    #                                  realm_name="master")
    # token = keycloak_openid.token("admin", "changeme")
    # print(token["access_token"])
    #
    #
    #
    # # "http://10.10.121.11:30035/auth/admin/realms/dx-arch/clients?first=0&max=20&search=true"
    # path = "/auth/admin/realms/dx-arch/clients"
    # param = {
    #     "clientId": "dx",
    #     "search": True,
    #     "first": 0,
    #     "max": 20
    # }
    # url = "http://10.6.121.51:30035/auth/admin/realms/dx-arch/clients"
    # header = {
    #     "accept": "application/json",
    #     "content-type": "application/json"
    # }
    # header["Authorization"] = "Bearer " + token["access_token"]
    #
    # # print(header)
    # # print(url)
    # response = ArchApiBase()._get(url=url, headers=header, query=param)
    # print("=======")
    # print(response.json())
    # print(response.json()[0]["id"])
    # if response.status_code == 200:
    #     arch_client_uuid = response.json()[0]["id"]
    #
    #     path = "/auth/admin/realms/dx-arch/clients/%s/client-secret" % (arch_client_uuid)
    #     _get_secret_url = "http://10.6.121.51:30035" + path
    #     _response = ArchApiBase()._get(url=_get_secret_url, headers=header)
    #     # print(_response.json()["value"])
    #     print(_response.json()["value"])
    # else:
    #     print("something is wrong")


