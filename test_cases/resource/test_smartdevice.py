# -*- coding: utf-8 -*-


import json
from test_cases.resource import test_asset, test_configuration
from common import tools
from test_cases.ApiConst import RESOURCE
from test_cases import ApiCommon


def __resource_smartDevice_add_get_prepare_data(dict_params, category_id, category_type):
    '''智能设备添加前准备数据
    准备数据：类别接口-->平台接口-->平台协议接口-->类别属性接口
    '''
    ### 修改动态属性值
    time = tools.get_time_no_year()
    dict_object = test_configuration.resource_category_attribute_list({"categoryId": category_id})
    for i, item in enumerate(dict_object):
        # print(i, item['locationType'], item['type'], item['showed'], item['value'])
        if item['locationType'] == 'PAGE' and 'ADD' in item['showed']:
            if item['type'] in ['STRING', 'INTEGER', 'FLOAT']:
                # if item['reqired'] == True:    pass
                item['value'] = time
            elif item['type'] == 'BOOLEAN':
                item['value'] = True
            elif item['type'] == 'ENUM':
                item['value'] = 1
            else:
                print("文本类型（type）：'STRING', 'INTEGER', 'FLOAT', 'BOOLEAN', 'ENUM'不在这五种范围内")
        elif item['locationType'] == 'PAGE' and 'EDIT' in item['showed']:
            print("locationType是PAGE，且showed是EDIT")
        else:
            print("locationType不是PAGE，且showed不是ADD或EDIT")
    print("content内容自动输入完成")

    ###修改固定属性值
    list_platform = test_configuration.resource_platform_list({"deviceType": category_type})
    platform_id = list_platform['id']
    platform_name = list_platform['name']

    list_platform_protocol = test_configuration.resource_platform_protocol_list({"platformId": platform_id})
    platform_protocol_id = list_platform_protocol['id']
    platform_protocol_name = list_platform_protocol['name']

    dict_params['smartDeviceType'] = category_type
    dict_params['categoryId'] = category_id
    dict_params['platformId'] = platform_id
    dict_params['platformName'] = platform_name
    dict_params['platformProtocolId'] = platform_protocol_id
    dict_params['platformProtocolName'] = platform_protocol_name
    dict_params['content'] = json.dumps(dict_object)

    return dict_params


def test_smt_add_oneData(mark='a'):
    """固定数据新增一个智能设备数据，用于更新、删除接口使用"""
    print("---新增一条智能设备数据并获取其id---")
    # time = tools.get_time_no_year()
    # dict_params = {"deviceName": "o%s摄%s" % (mark, time)}
    # sid = resource_smartDevice_add(dict_params)
    # return sid


def test_smt_add(dict_params, category_id, category_type, dict_asset=None):
    dict_params = __resource_smartDevice_add_get_prepare_data(dict_params, category_id, category_type)
    url = RESOURCE.SMARTDEVICE_ADD
    response_object = ApiCommon.api_post_request(url, dict_params, dict_asset)
    if response_object is not None:
        sid = response_object['id']
        print(sid)
        return sid


def test_smt_edit(str_id, str_name, dict_asset=None):
    dict_params = test_asset.resource_asset_getbyid({"id": str_id})
    dict_params['name'] = str_name + str(tools.get_time_no_year())
    dict_params['content'] = json.dumps(test_asset.resource_attribute_value_asset_content({"id": str_id}))

    url = RESOURCE.SMARTDEVICE_EDIT
    response_object = ApiCommon.api_post_request(url, dict_params, dict_asset)
    # 数据库断言--获取每列的值拼接作为where语句
    if response_object is not None:
        sid = response_object['id']
        print(sid)
        return sid


def test_smt_page(dict_params, dict_asset=None):
    """资产数据接口
    /ener-resource/asset/page?categoryId=1&name=2021115&platformId=AD_SCREEN_REALTIME&isRelated=&platformProtocolId=AD_SCREEN_PROTOCOL_REALTIME&current=1&type=SMART_DEVICE"""
    url = RESOURCE.ASSET_PAGE
    return ApiCommon.api_get_request(url, dict_params, dict_asset)


def test_smt_deleteBatch(dict_params, dict_asset=None):
    url = RESOURCE.SMARTDEVICE_DELETEBATCH
    response_object = ApiCommon.api_delete_request(url, dict_params, dict_asset)


def test_smt_getAssociatedSmartDevicePage(dict_params, dict_asset=None):
    """智能设备关联设备选择界面参数：#/ener-resource/smartDevice/getAssociatedSmartDevicePage?current=1&size=999999&smartDeviceType=LAMP_POLE    """
    url = RESOURCE.SMARTDEVICE_GETASSOCIATEDSMARTDEVICEPAGE
    return ApiCommon.api_get_request(url, dict_params, dict_asset)


def test_smt_getFault(dict_params, dict_asset=None):
    """资产表-状态枚举参数：#/ener-resource/smartDevice/getFault返回值：# type=NORMAL;name=正常;value=NORMAL;"""
    url = RESOURCE.SMARTDEVICE_GETFAULT
    return ApiCommon.api_get_request(url, dict_params, dict_asset)


def test_smt_getAssetsBySpaceId(dict_params, dict_asset=None):
    """资产表-状态枚举参数：#/ener-resource/smartDevice/getAssetsBySpaceId?categoryIds=1&current=1&name=006&size=10&spaceIds=1"""
    url = RESOURCE.SMARTDEVICE_GETASSETSBYSPACEID
    return ApiCommon.api_get_request(url, dict_params, dict_asset)


def test_smt_camera_query(dict_params, dict_asset=None):
    """智能设备摄像头-查询(不分页)参数：#/ener-resource/smartDevice/camera/query"""
    url = RESOURCE.SMARTDEVICE_CAMERA_QUERY
    return ApiCommon.api_get_request(url, dict_params, dict_asset)


def test_smt_camera_panoramics(dict_params, dict_asset=None):
    """全景摄像头-查询(不分页)参数：#/ener-resource/smartDevice/camera/panoramics"""
    url = RESOURCE.SMARTDEVICE_CAMERA_PANORAMICS
    return ApiCommon.api_get_request(url, dict_params, dict_asset)


if __name__ == "__main__":
    # query_first_page={"categoryId":"1","name":"2021115","platformId":"AD_SCREEN_REALTIME","isRelated":None,"platformProtocolId":"AD_SCREEN_PROTOCOL_REALTIME","fault":"NORMAL","current":"1","type":"SMART_DEVICE"}
    # resource_smartDevice_page(query_first_page)
    pass
