import json
import logging

from application.config.models import Config
from application.config_data.models import ConfigData
from config.env import IMAGE_URL
from utils import R
from utils.utils import getImageURL, saveImage


# 获取配置信息
def getConfigInfo(request):
    # 配置ID
    config_id = request.GET.get('config_id', 1)
    # 查询配置数据列表
    data_list = ConfigData.objects.filter(is_delete=False, status=1, config_id=config_id).order_by(
        "sort").values()

    # 实例化配置数据对象
    dataList = []
    if data_list:
        for v in data_list:
            # 数据类型
            type = v['type']

            data = {}
            data["id"] = v['id']
            data["title"] = v['title']
            data["code"] = v['code']
            data["value"] = v['value']
            data["type"] = v['type']

            if type == "checkbox":
                # 复选框
                itemList = {}
                options = v['options'].split(',')
                if len(options) > 0:
                    for val in options:
                        item = val.split('=')
                        itemList[item[0]] = item[1]
                data['itemList'] = itemList
            elif type == "radio":
                # 单选按钮
                itemList = {}
                options = v['options'].split(',')
                if len(options) > 0:
                    for val in options:
                        item = val.split('=')
                        itemList[item[0]] = item[1]
                data['itemList'] = itemList
            elif type == "select":
                # 下拉选择
                itemList = {}
                options = v['options'].split(',')
                if len(options) > 0:
                    for val in options:
                        item = val.split('=')
                        itemList[item[0]] = item[1]
                data['itemList'] = itemList
            elif type == "image":
                # 单图
                if v['value']:
                    data["value"] = getImageURL(v['value'])
            elif type == "images":
                # 多图
                if v['value']:
                    # 字符串分裂处理
                    list = v['value'].split(',')
                    itemList = []
                    for v in list:
                        image = getImageURL(v)
                        itemList.append(image)
                    # 图片数据
                    data["value"] = itemList
            # 加入数组
            dataList.append(data)

    # 获取配置列表
    configList = Config.objects.filter(is_delete=False).values()

    # 模板参数
    content = {
        'config_id': int(config_id),
        'configList': configList,
        'dataList': dataList,
    }
    # 返回结果
    return content


# 保存配置信息
def saveConfigInfo(request):
    try:
        # 接收请求参数
        json_data = request.body.decode()
        # 参数为空判断
        if not json_data:
            return R.failed("参数不能为空")
        # 数据类型转换
        dict_data = json.loads(json_data)
    except Exception as e:
        logging.info("错误信息：\n{}", format(e))
        return R.failed("参数错误")
    # 数据源处理
    if dict_data:
        for key in dict_data:
            # 参数值
            val = dict_data[key]
            if key.find('checkbox') != -1:
                # 复选框
                item = key.split('__')
                key = item[0]
            elif key.find('image') != -1:
                # 单图上传
                item = key.split('__')
                key = item[0]
                if val.find('temp') != -1:
                    image = saveImage(val, "config")
                    # 赋值
                    val = image
                else:
                    # 赋值
                    val = val.replace(IMAGE_URL, "")
            elif key.find('imgs') != -1:
                # 多图上传
                item = key.split('__')
                key = item[0]
                # 图片地址处理
                urlList = val.split(',')
                list = []
                if len(urlList) > 0:
                    for url in urlList:
                        if url.find('temp') != -1:
                            url = saveImage(url, "config")
                            # 加入数组
                            list.append(url)
                        else:
                            # 赋值
                            url = url.replace(IMAGE_URL, "")
                            list.append(url)
                # 图片地址逗号分割
                val = ','.join(list)
            elif key.find('ueditor') != -1:
                # 富文本
                item = key.split('__')
                key = item[0]

            # 根据编码查询配置项
            config_data = ConfigData.objects.filter(is_delete=False, code=key).first()
            if not config_data:
                continue
            # 设置
            config_data.value = val
            config_data.save()

        # 返回结果
        return R.ok()
