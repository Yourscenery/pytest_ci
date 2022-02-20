class LIGHTSHADOW:
    PLACE_ADD = "/ener-lightshadow/place/add"  # 场所-添加
    # PLACE_ADDLOCATIONANDASSET = "/ener-lightshadow/place/addLocationAndAsset"  # 场所-绑定位置码和设备
    # PLACE_ADDPLANEIMAGE = "/ener-lightshadow/place/addPlaneImage"  # 场所-添加平面图
    PLACE_ADDSPACERELATION = "/ener-lghtshadow/place/addSpaceRelation"  # 场所-关联空间
    # PLACE_ASSETLISTBYCATEGORY = "/ener-lightshadow/place/assetListByCategory"  # 场所-根据场所id和设备类型ID查询设备列表
    PLACE_ASSETPAGE = "/ener-lightshadow/place/assetPage"  # 根据场所id查询关联的设备信息
    PLACE_DELETE = "/ener-lightshadow/place/delete"  # 场所表-通过id删除
    PLACE_DELETEBATCH = "/ener-lightshadow/place/deleteBatch"  # 场所表-通过ids批量删除
    PLACE_EDIT = "/ener-lightshadow/place/edit"  # 场所-编辑
    # PLACE_GETLOCATIONANDASSET = "/ener-lightshadow/place/getLocationAndAsset"  # 场所-获取场所下位置码和设备关联信息
    PLACE_LIST = "/ener-lightshadow/place/list"  # 根据场所类型Id查询所有场所
    # PLACE_LOCATIONLIST = "/ener-lightshadow/place/locationList"  # 场所-根据场所id查询未绑定设备的位置码列表
    PLACE_PAGE = "/ener-lightshadow/place/page"  # 场所表-根据名称或者类型Id查询
    PLACE_QUERYBYID = "/ener-lightshadow/place/queryById"  # 场所-根据Id查询场所基本信息
    # PLACE_REMOVELOCATIONANDASSET = "/ener-lightshadow/place/removeLocationAndAsset"  # 场所-解除位置码和设备关联信息
    # PLACE_REMOVELOCATIONANDASSETALL = "/ener-lightshadow/place/removeLocationAndAssetAll"  # 场所-解除位置码和设备关联信息
    PLACE_REMOVESPACERELATION = "/ener-lightshadow/place/removeSpaceRelation"  # 场所-删除关联空间
    PLACE_SPACECATEGORYLIST = "/ener-lightshadow/place/spaceCategoryList"  # 根据场所id查询关联的空间的类型列表
    # PLACE_SPACELIST = "/ener-lightshadow/place/spaceList"  # 根据场所id查询关联的空间列表
    PLACE_SPACELISTBYPARENTID = "/ener-lightshadow/place/spaceListByParentId"  # 根据父空间id查询已经关联场所的子空间列表
    PLACE_SPACELISTBYPARENTIDALL = "/ener-lightshadow/place/spaceListByParentIdAll"  # 根据父空间id查询子空间列表
    PLACE_SPACEPAGE = "/ener-lightshadow/place/spacePage"  # 根据场所id查询关联的空间信息
    PLACE_SPACEPAGEALL = "/ener-lightshadow/place/spacePageAll"  # 查询所有可关联场所的空间信息
    PLACECATEGORY_LIST = "/ener-lightshadow/placeCategory/list"


class RESOURCE:
    SMARTDEVICE_CAMERA_PANORAMICS = "/ener-resource/smartDevice/camera/panoramics"  # 全景摄像头-查询(不分页)
    SMARTDEVICE_CAMERA_QUERY = "/ener-resource/smartDevice/camera/query"  # 智能设备摄像头-查询(不分页)
    SMARTDEVICE_ADD = "/ener-resource/smartDevice/add"  # 智能设备-添加
    SMARTDEVICE_DELETEBATCH = "/ener-resource/smartDevice/deleteBatch"  # 智能设备-批量删除
    SMARTDEVICE_EDIT = "/ener-resource/smartDevice/edit"  # 智能设备-编辑
    SMARTDEVICE_GETASSETSBYSPACEID = "/ener-resource/smartDevice/getAssetsBySpaceId"  # 获取设备by空间id
    SMARTDEVICE_GETASSOCIATEDSMARTDEVICEPAGE = "/ener-resource/smartDevice/getAssociatedSmartDevicePage"  # 智能设备关联设备选择界面
    SMARTDEVICE_GETFAULT = "/ener-resource/smartDevice/getFault"  # 资产表-状态枚举

    ASSET_PAGE = "/ener-resource/asset/page"  # 其他资产、智能设备列表
    ASSET_GETBYID = "/ener-resource/asset/getById"  # 资产表-根据id获取类别
    ASSET_ATTRIBUTEVALUE_ASSET_CONTENT = "/ener-resource/attribute-value/asset/content"  # 根据资产id获得对应扩展属性

    CONFIG_CATEGORY_LIST = "/ener-resource/resourceCategory/list"  # 类别表-列表查询
    CONFIG_CATEGORY_ATTRIBUTE_LIST = "/ener-resource/category-attribute/list"  # 类别属性列表
    CONFIG_PLATFORM_PROTOCOL_LIST = "/ener-resource/platform/protocol-list"  # 平台协议列表
    CONFIG_PLATFORM_LIST = "/ener-resource/platform/list"  # 平台列表
    CONFIG_CATEGORY_GETBYID = "/ener-resource/resourceCategory/getById"  # 类别表-根据id获取类别
