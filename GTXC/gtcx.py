import requests
import random

"""
ip：添加的服务器
token：登录高铁平台后f12获取 “Authorization” 值
"""

ip = "http://192.168.30.51"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOlsiMTM3MTcxNjI4NjIwNzA0OTcyOSIsInd6bDEyMyIsInBjIiwiVGh1IEp1biAyNCAwNjoyOTowMCBVVEMgMjAyMSJdLCJleHAiOjE2MjQ1MTk3NDAsImlhdCI6MTYyNDUxNjE0MH0.8nnJazAGtSWUdj1UUoQOz8hOPqe8xn6yJIsbb2JEzXE"
dict_headers = {"Authorization": token, "Content-Type": "application/json"}


def add_space():
    """
    添加空间
    1、准备数据有：categoryId
    2、name：递增"space_" + range(101, 501)，101到500
    """
    url = '/resource/spaceData/add'
    params = {"name": "", "parentId": "0", "categoryId": "1375358012327714817", "desc": "", "attributeInfos": [],
              "insertRelationDeviceIds": [], "insertRelationXassetIds": []}

    for item in range(101, 501):
        params['name'] = "space_" + str(item)
        #response_data = requests.post(ip + url, json=params, headers=dict_headers)
        #print(str(item) + response_data.text)


def add_device():
    """
    添加设备
    1、准备数据有：categoryId（设备类型）
    2、name：递增"device_" + range(201, 501)，201到500
    3、code类似name
    4、positionDesc类似name
    【设备类型如下：】
    1338365285718155265	LAMP_FANGDA	方大PLC
    1338365285718155266	SINGLE_LAMP_CONTROLLER_FANGDA	方大单灯控制器
    1338365285718155268	CONCENTRATOR_FANGDA	方大集中器
    1372376412172951553	AD_SCREEN_XIXUN	熙讯广告屏
    1372836241920319489	BROADCAST_SPON	世邦广播
    1372836241920319490	LAMP_POLE_LANDSKY	良业灯杆
    """
    url = "/resource/deviceData/add"
    categoryid = ["1338365285718155265", "1338365285718155266", "1338365285718155268",
                  "1372376412172951553", "1372836241920319489", "1372836241920319490"]
    params = {"name": "", "code": "", "positionDesc": "", "categoryId": "",
              "storageTime": "2021-04-01", "spaceId": "", "longitude": "120.157894", "latitude": "30.173141", "maintainCycle": "3",
              "attributeInfos": None, "insertRelationDeviceIds": [], "insertRelationXassetIds": [],
              "parentControlDeviceId": None, "insertControlDeviceIds": []}
    for item in range(201, 501):
        params['name'] = "device_" + str(item)
        params['code'] = "1106" + str(item)
        params['positionDesc'] = "wz_" + str(item)
        params['categoryId'] = random.choice(categoryid)
        #response_data = requests.post(ip + url, json=params, headers=dict_headers)
        #print(str(item) + response_data.text)


def add_project():
    """
    添加项目
    1、准备数据有：categoryId（类别类型）
    2、name：递增"project_" + range(1, 51)，1到50
    """
    url = '/resource/projectData/add'
    params = {"name": "", "positionDesc": "", "categoryId": "1401808017992716289",
              "projectTime": "2021-06-24", "attributeInfos": [], "personId": ""}

    for item in range(5, 101):
        params['name'] = "project_" + str(item)
        params['positionDesc'] = "positionDesc_" + str(item)
        response_data = requests.post(ip + url, json=params, headers=dict_headers)
        print(str(item) + response_data.text)


def add_asset():
    """
    添加其他资产
    1、准备数据有：categoryId（类别类型）
    2、name：递增"asset_" + range(1, 51)，1到50
    """
    url = '/resource/xAssetData/add'
    params = {"name": "", "code": "", "positionDesc": "", "categoryId": "1400333133366169602", "storageTime": "2021-06-24",
              "spaceId": "", "longitude": "", "latitude": "", "maintainCycle": "", "factoryDesc": "", "attributeInfos": None}

    for item in range(1, 5):
        params['name'] = "asset_" + str(item)
        params['positionDesc'] = "positionDesc_" + str(item)
        response_data = requests.post(ip + url, json=params, headers=dict_headers)
        print(str(item) + str(response_data.status_code))


if __name__ == '__main__':
    pass
    # add_space()
    # add_device()
    # add_project()
    add_asset()
