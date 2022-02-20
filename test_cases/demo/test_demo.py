def test_demo(pytestconfig):
    print('test_demo')
    base_api_url = pytestconfig.getini('base_api_url')
    print(base_api_url)
    base_api_username = pytestconfig.getini('base_api_username')
    base_api_password = pytestconfig.getini('base_api_password')
    print(base_api_url, base_api_username, base_api_password)