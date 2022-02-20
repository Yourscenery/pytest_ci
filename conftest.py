import datetime

# Hooks方法
# def pytest_configure(config):
#     """更改生成报告和日志的路径"""
#     htmlpath = config.getoption('htmlpath')
#     log_file = config.getoption('log_file') or config.getini('log_file') or '{}.log'
#     now = datetime.now()
#     config.option.htmlpath = os.path.join(config.rootdir, 'reports', htmlpath.format(now.strftime('%Y%m%d_%H%M%S')))
#     config.option.log_file = os.path.join(config.rootdir, 'logs', log_file.format(now.strftime('%Y%m%d')))


def pytest_addoption(parser):
    """注册新的命令行选项和ini文件参数"""
    # parser.addoption("--send-email", action="store_true", help="发送邮件")
    parser.addini('base_api_url', help='地址')
    parser.addini('base_api_username', help='用户')
    parser.addini('base_api_password', help='密码')


