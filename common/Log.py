#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

class Logger:
    def __init__(self):

        self.logger = logging.Logger("test_log.log")
        self.logger.setLevel(logging.NOTSET)

        formatter = logging.Formatter('%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s: %(message)s')

        # 设置file log
        file_log = logging.FileHandler("test_log.log")
        file_log.setLevel(logging.NOTSET)
        file_log.setFormatter(formatter)

        # 设置cmd log
        cmd_log = logging.StreamHandler()
        cmd_log.setLevel(logging.NOTSET)
        cmd_log.setFormatter(formatter)

        self.logger.addHandler(file_log)
        self.logger.addHandler(cmd_log)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


if __name__ == '__main__':
    print("test")
    logger = Logger()
    logger.debug("debug message")
    logger.info("info message")
    logger.error("error message")
    logger.warn("warn message")
