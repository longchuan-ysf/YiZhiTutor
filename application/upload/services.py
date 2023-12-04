import logging
import os
import random
import time

from config.env import TEMP_PATH, IMAGE_URL, ATTACHMENT_PATH
from utils.file import mkdir


# 上传图片
def uploadImage(request):
    # 获取文件对象
    file = request.FILES.get('file')
    # 文件扩展名
    file_ext = os.path.splitext(file.name)[1].lower()
    # file_ext = file.name.split('.')[-1].lower()
    if file_ext not in [".jpeg", ".png", ".gif"]:
        logging.info("文件格式不正确")

    # 定义文件名，年月日时分秒随机数
    file_name = time.strftime('%Y%m%d%H%M%S') + '%05d' % random.randint(0, 100)
    # 重写合成文件名
    file_name = os.path.join(file_name + file_ext)

    # 保存文件
    save_path = TEMP_PATH + "/" + time.strftime('%Y%m%d')
    # 创建存放目录
    mkdir(save_path)
    # 拼接文件路径
    # path = os.path.join(save_path, file_name)
    path = save_path + "/" + file_name
    # 写入文件
    with open(path, 'wb') as f:
        for line in file:
            f.write(line)

    # 文件地址
    file_url = IMAGE_URL + path.replace(ATTACHMENT_PATH, "")
    # 返回结果
    result = {
        'fileName': file.name,
        'fileUrl': file_url,
    }
    # 返回结果
    return result
