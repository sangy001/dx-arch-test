"""
封装Assert方法
"""
from common.Log import Logger
import json
logger = Logger()


class Assertions:
    def __init__(self):
        self.logger = Logger()

    def assert_code(self, code, expected_code):
        """
        验证response状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert code != 500, self.logger.error('StatusCode error: %s' % code)
            assert code == expected_code
            return True
        except:
            self.logger.error("StatusCode error, expected_code is %s, statusCode is %s " % (expected_code, code))
            # Consts.RESULT_LIST.append('fail')
            raise

    def assert_body_msg(self, response, expected_response):
        """
        返回值
        dict/json 判断键值对
        text 判断str
        list 判断数据

        :param response:
        :param expected_response:
        :return:
        """
        if isinstance(expected_response, list):
            expected_response = expected_response[0]
            try:
                _actual_response = response.json()[0]
            except json.JSONDecodeError:
                raise AssertionError(u'响应值不符合预期: [预期]%s [实际]%s' % (expected_response, response.text))
        elif isinstance(expected_response, dict):
            try:
                _actual_response = response.json()
            except json.JSONDecodeError:
                raise AssertionError(u'响应值不符合预期: [预期]%s [实际]%s' % (expected_response, response.text))
        elif isinstance(expected_response, str):
            _actual_response = response.text
            assert expected_response in _actual_response, \
                u'响应值不符合预期: [预期]%s [实际]%s' % (expected_response, _actual_response)
            return True
        else:
            return True

        for _key in expected_response.keys():
            assert _key in _actual_response.keys(), u'响应值不符合预期: [预期]%s [实际]No This Key' % _key
            if expected_response[_key] is not None:
                if expected_response[_key] == u'请求无效':
                    assert expected_response[_key] in _actual_response[_key], \
                        u'响应值不符合预期: [预期]%s [实际]%s' % (expected_response[_key], _actual_response[_key])
                else:
                    assert expected_response[_key] == _actual_response[_key], \
                        u'响应值 %s 的值不符合预期: [预期]%s [实际]%s' \
                        % (_key, expected_response[_key], _actual_response[_key])
                logger.info(u'响应值 %s 符合预期: %s' % (_key, expected_response[_key]))


    # def assert_str(self, response, expected_response):
    #     """
    #     :param response:
    #     :param expected_response:
    #     :return:
    #     """
    #
    # def assert_list(self, response, expected_response):
    #     """
    #     :param response:
    #     :param expected_response:
    #     :return:
    #     """



    def assert_body(self, body, body_msg, expected_msg):
        """
        验证response body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        :return:
        """
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            return True

        except:
            self.logger.error("Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body_msg))
            # Consts.RESULT_LIST.append('fail')

            raise

    def assert_in_text(self, body, expected_msg):
        """
        验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(body, ensure_ascii=False)
            # print(text)
            assert expected_msg in text
            return True

        except:
            self.logger.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)
            # Consts.RESULT_LIST.append('fail')

            raise

    def assert_text(self, body, expected_msg):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            return True

        except:
            self.logger.error("Response body != expected_msg, expected_msg is %s, body is %s" % (expected_msg, body))
            # Consts.RESULT_LIST.append('fail')

            raise

    # def assert_json(self, body, expected_json):
    #

    def assert_time(self, time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_time
            return True
        except:
            self.logger.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))
            # Consts.RESULT_LIST.append('fail')
            raise

