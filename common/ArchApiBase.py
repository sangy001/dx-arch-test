#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import logging
import configparser
import json
import requests
from common.Log import Logger
from config.Config import Config

logger = Logger()
config = Config()



class ArchApiBase(object):

    def __init__(self):
        self.username = config.username
        self.password = config.password

        self.arch_url = config.arch_url
        self.arch_client_id = config.arch_client_id
        # self.arch_client_secret = config.arch_client_secret

        self.keycloak_url = config.keycloak_url
        self.keycloak_realm = config.keycloak_ream
        self.keycloak_client_id = config.keycloak_client_id



        self._session = requests.session()
        self._headers = {
            "accept": "application/json",
            "content-type": "application/json",
        }
        self._response = dict()

        self._none = {
            "arch_auth": None,
            "client_uuid": None,
            "client_secret": None,
            "client_id": None,
            "ldap_id": None,
            "user_id": None,
            "user_name": None,
            "webhook_uuid": None,
            "keycloak_client_secret": None,
            "keycloak_auth": None
        }
        # self.robot_env = RolotEnv()
        self.arch_temp_info = self._none


    def get_config(self):
        config_path = "config/config.ini"
        env = configparser.ConfigParser()
        env.read(config_path)


    # def config_headers(self, header_key: str, header_value):
    #     """
    #     配置头信息
    #     :param header_key:
    #     :param header_value:
    #     :return:
    #     """
    #     self._headers[header_key] = header_value

    @staticmethod
    def _generate_curl_headers(headers: dict):
        _headers = list()
        for _key in headers.keys():
            _headers.append('"%s:%s"' % (_key, headers[_key]))
        return '-H ' + ' -H '.join(_headers)

    def _post(self, url: str, headers: dict, data: dict, query=None):
        logger.debug("==========================")
        logger.debug('Method: POST')
        logger.debug('URL: %s' % url)
        logger.debug('Query: %s' % query)
        logger.debug('Header: %s' % headers)
        logger.debug('Body: %s' % data)
        _data = json.dumps(data)
        _response = self._session.post(url=url, headers=headers, params=query, data=data, verify=False)
        logger.info('curl -s -v -X POST %s -d \'%s\' %s'
                 % (self._generate_curl_headers(headers), _data, _response.url))
        logger.info('Response_Body: %s' % _response.text)
        return _response

    def _put(self, url: str, headers: dict, data, query=None):
        logger.debug("==========================")
        logger.debug('Method: PUT')
        logger.debug('URL: %s' % url)
        logger.debug('Query: %s' % query)
        logger.debug('Header: %s' % headers)
        logger.debug('Body: %s' % data)
        _data = json.dumps(data)
        _response = self._session.put(url=url, headers=headers, params=query, data=data, verify=False)
        logger.info('curl -s -v -X PUT %s -d \'%s\' %s'
                 % (self._generate_curl_headers(headers), _data, _response.url))
        logger.info('Response_Body: %s' % _response.text)
        return _response

    def _get(self, url: str, headers: dict, query=None):
        logger.debug("==========================")
        logger.debug("Method: GET")
        logger.debug('URL: %s' % url)
        logger.debug('Query: %s' % query)
        logger.debug('Header: %s' % headers)
        _response = self._session.get(url=url, headers=headers, params=query, verify=False)
        logger.info('curl -s -v -X GET %s %s' % (self._generate_curl_headers(headers), _response.url))
        logger.info('Response_Body: %s' % _response.text)
        return _response

    def _head(self, url: str, headers: dict, query=None):
        logger.debug("==========================")
        logger.debug('Method: HEAD')
        logger.debug('URL: %s' % url)
        logger.debug('Query: %s' % query)
        logger.debug('Header: %s' % headers)
        _response = self._session.head(url=url, headers=headers, params=query, verify=False)
        logger.info('curl -s -v -X HEAD %s %s' % (self._generate_curl_headers(headers), _response.url))
        logger.info(_response.text)
        return _response

    def _patch(self, url: str, headers: dict, data=None, query=None,):
        logger.debug("==========================")
        logger.debug('Method: PATCH')
        logger.debug('URL: %s' % url)
        logger.debug('Query: %s' % query)
        logger.debug('Header: %s' % headers)
        logger.debug('Body: %s' % data)
        _data = json.dumps(data)

        _response = self._session.patch(url=url, headers=headers, params=query, data=data, verify=False)
        logger.info(
            'curl -s -v -X PATCH %s -d \'%s\' %s' % (self._generate_curl_headers(headers), _data, _response.url)
        )
        logger.info('Response_Body: %s' % _response.text)
        return _response

    def _delete(self, url: str, headers: dict, data: dict, query=None):
        logger.debug("==========================")
        logger.debug('Method: DELETE')
        logger.debug('URL: %s' % url)
        logger.debug('Query: %s' % query)
        logger.debug('Header: %s' % headers)
        logger.debug('Body: %s' % data)
        _data = json.dumps(data)
        _response = self._session.delete(url=url, headers=headers, params=query, data=data, verify=False)
        logger.info(
            'curl -s -v -X DELETE %s -d \'%s\' %s' % (self._generate_curl_headers(headers), _data, _response.url)
        )
        logger.info('Response_Body: %s' % _response.text)
        return _response


if __name__ == '__main__':
    print('This is a script for Arch Base REST API')
    # logger.debug("Method: GET")