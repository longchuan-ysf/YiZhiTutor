import os
import re
import time

from config.env import IMAGE_URL, CHAT_MULTIMEDIA_PATH, TEMP_PATH, ATTACHMENT_PATH
from utils.file import mkdir

def save_chat_image(imageURL, dirname):
    # 判断文件地址是否为空
    if not imageURL:
        return "文件地址不能为空"
    # 判断是否是本站图片
    if imageURL.find(IMAGE_URL) != -1:
        # 本站图片
        if imageURL.find("temp") != -1:
            # 临时图片
            path = CHAT_MULTIMEDIA_PATH + "/" + dirname + "/" + time.strftime('%Y%m%d')
            # 创建存储目录
            mkdir(path)
            # 原始图片地址
            oldPath = imageURL.replace(IMAGE_URL, ATTACHMENT_PATH)
            # 目标目录地址
            newPath = CHAT_MULTIMEDIA_PATH + "/" + dirname + oldPath.replace(TEMP_PATH, "")
            # 移动文件
            os.rename(oldPath, newPath)
            # 返回结果
            return newPath.replace(ATTACHMENT_PATH, "")
        else:
            # 非临时图片
            return imageURL.replace(IMAGE_URL, "")
    else:
        # 远程图片
        print("远程图片处理")
    # 返回空字符串
    return ""
