# -*- coding: utf-8 -*-

import json
from common import CONSTS
import logging
import time
from configparser import ConfigParser
import os
import os.path


class Config:
    def __init__(self):
        self.config = ConfigParser()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")

        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("找不到配置文件config.ini")
        self.config.read(self.conf_path)

        _S_MYSQL = "mysql"
        _S_SSH = "ssh"
        _S_WEB = "web"
        _S_MAIL = "mail"
        _HOST = "host"
        _PORT = "port"
        _USERNAME = "username"
        _PASSWORD = "password"
        _DATABASE = "database"
        _SENDER = "sender"
        _RECEIVER = "receiver"
        _SMTPSERVER = "smtpserver"

        self.mysql_host = self.config.get(_S_MYSQL, _HOST)
        self.mysql_port = self.config.get(_S_MYSQL, _PORT)
        self.mysql_username = self.config.get(_S_MYSQL, _USERNAME)
        self.mysql_password = self.config.get(_S_MYSQL, _PASSWORD)
        self.mysql_database = self.config.get(_S_MYSQL, _DATABASE)

        self.web_host = self.config.get(_S_WEB, _HOST)
        self.web_username = self.config.get(_S_WEB, _USERNAME)
        self.web_password = self.config.get(_S_WEB, _PASSWORD)

        self.ssh_host = self.config.get(_S_SSH, _HOST)
        self.ssh_port = self.config.get(_S_SSH, _PORT)
        self.ssh_username = self.config.get(_S_SSH, _USERNAME)
        self.ssh_password = self.config.get(_S_SSH, _PASSWORD)

        self.mail_sender = self.config.get(_S_MAIL, _SENDER)
        self.mail_receiver = self.config.get(_S_MAIL, _RECEIVER)
        self.mail_smtpserver = self.config.get(_S_MAIL, _SMTPSERVER)
        self.mail_username = self.config.get(_S_MAIL, _USERNAME)
        self.mail_password = self.config.get(_S_MAIL, _PASSWORD)

    def add_conf(self, section, key, value):
        self.config.add_section(section)
        self.config.set(section, key, value)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def set_conf(self, section, key, value):
        self.config.set(section, key, value)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def get_conf(self):
        self.config.read(self.conf_path, encoding="utf-8")
        conf = {}
        for section in self.config.sections():
            conf[section] = dict(self.config.items(section))
        return conf

    def get_conf_by_section(self, section):
        self.config.read(self.conf_path, encoding="utf-8")
        if section in self.config.sections():
            conf = self.config[section]
            return conf
        else:
            raise KeyError(section, "section值不存在")

    def get_conf_by_key(self, section, key):
        self.config.read(self.conf_path, encoding="utf-8")
        if section in self.config.sections():
            if key in self.config[section]:
                conf = self.config[section][key]
                return conf
            else:
                raise KeyError(key, "key值不存在")
        else:
            raise KeyError(section, "section值不存在")


class MyLog:
    LEVELS = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    logger = logging.getLogger()
    level = 'default'

    def create_file(self, filename):
        path = filename[0:filename.rfind('/')]
        if not os.path.isdir(path):
            os.makedirs(path)
        if not os.path.isfile(filename):
            fd = open(filename, mode='w', encoding='utf-8')
            fd.close()
        else:
            pass

    def set_handler(self, levels):
        if levels == 'error':
            self.logger.addHandler(MyLog.err_handler)
        self.logger.addHandler(MyLog.handler)

    def remove_handler(self, levels):
        if levels == 'error':
            self.logger.removeHandler(MyLog.err_handler)
        self.logger.removeHandler(MyLog.handler)

    def get_current_time(self):
        return time.strftime(MyLog.date, time.localtime(time.time()))

    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = path + '/Log/log.log'
    err_file = path + '/Log/err.log'
    logger.setLevel(LEVELS.get(level, logging.NOTSET))
    create_file(log_file)
    create_file(err_file)
    date = '%Y-%m-%d %H:%M:%S'

    handler = logging.FileHandler(log_file, encoding='utf-8')
    err_handler = logging.FileHandler(err_file, encoding='utf-8')

    @staticmethod
    def debug(self, log_meg):
        self.set_handler('debug')
        self.logger.debug("[DEBUG " + self.get_current_time() + "]" + log_meg)
        self.remove_handler('debug')

    @staticmethod
    def info(self, log_meg):
        self.set_handler('info')
        self.logger.info("[INFO " + self.get_current_time() + "]" + log_meg)
        self.remove_handler('info')

    @staticmethod
    def warning(self, log_meg):
        self.set_handler('warning')
        self.logger.warning("[WARNING " + self.get_current_time() + "]" + log_meg)
        self.remove_handler('warning')

    @staticmethod
    def error(self, log_meg):
        self.set_handler('error')
        self.logger.error("[ERROR " + self.get_current_time() + "]" + log_meg)
        self.remove_handler('error')

    @staticmethod
    def critical(self, log_meg):
        self.set_handler('critical')
        self.logger.error("[CRITICAL " + self.get_current_time() + "]" + log_meg)
        self.remove_handler('critical')


class Assertions:
    def __init__(self):
        self.log = MyLog()

    def assert_code(self, code, expected_code):

        try:
            assert code == expected_code
            return True
        except:
            self.log.error("statusCode error, expected_code is %s, statusCode is %s " % (expected_code, code))
            CONSTS.RESULT_LIST.append('fail')

            raise

    def assert_body(self, body, body_msg, expected_msg):
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            return True

        except:
            self.log.error(
                "Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body_msg))
            CONSTS.RESULT_LIST.append('fail')

            raise

    def assert_in_text(self, body, expected_msg):

        try:
            text = json.dumps(body, ensure_ascii=False)
            # print(text)
            assert expected_msg in text
            return True

        except:
            self.log.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)
            CONSTS.RESULT_LIST.append('fail')

            raise

    def assert_text(self, body, expected_msg):

        try:
            assert body == expected_msg
            return True
        except Exception as e:
            self.log.error("Response body != expected_msg, expected_msg is %s, body is %s" % (expected_msg, body))
            CONSTS.RESULT_LIST.append('fail')

            raise

    def assert_time(self, time, expected_time):

        try:
            assert time < expected_time
            return True

        except:
            self.log.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))
            CONSTS.RESULT_LIST.append('fail')

            raise


if __name__ == "__main__":
    # ast = Assertions()
    # ast.assert_code(2300, 200)

    # MyLog.debug("This is debug message")
    # MyLog.info("This is info message")
    # MyLog.warning("This is warning message")
    # MyLog.error("This is error")
    # MyLog.critical("This is critical message")

    # con = Config()
    # # print(con.get_conf())
    # print(con.web_host)
    pass
