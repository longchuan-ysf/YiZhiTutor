import base64
import urllib
import requests
import json
import secret_key
import subprocess
import os
import random
import time
from config.env import TEMP_PATH,IMAGE_URL,ATTACHMENT_PATH
from django.core.files.storage import FileSystemStorage
from utils.file import mkdir
API_KEY = secret_key.asr_api_key
SECRET_KEY = secret_key.asr_secret_key


def asr_request(audio_file_path):
    url = "https://vop.baidu.com/server_api"
    audio_content, file_length = get_file_content_as_base64(audio_file_path, False)

    payload = json.dumps({
        "format": "wav",
        "rate": 16000,
        "channel": 1,
        "cuid": "d7zB9FPZ6iYYwwgCDTC9syeW5Xi3s1BL",
        "token": get_access_token(),
        "speech": audio_content,
        "len": file_length
    })
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()  # 如果请求出错，抛出HTTPError

        # 解析响应的JSON文本
        response_data = json.loads(response.text)
        if response_data['err_no'] == 0:
            # 请求成功，提取识别结果
            result_text = response_data['result'][0]  # 假设只关注第一个结果
            return {
                "success": True,
                "result": result_text,
                "sn": response_data['sn']
            }
        else:
            # 请求失败，返回错误信息
            return {
                "success": False,
                "error_message": response_data['err_msg'],
                "error_code": response_data['err_no']
            }
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return {
            "success": False,
            "error_message": str(e)
        }


def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码，并返回文件长度
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded
    :return: base64编码信息, 文件长度
    """
    with open(path, "rb") as f:
        file_content = f.read()
        file_length = len(file_content)
        content = base64.b64encode(file_content).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content, file_length


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    try:
        response = requests.post(url, params=params)
        response.raise_for_status()  # Raises stored HTTPError, if one occurred.
        return str(response.json().get("access_token"))
    except requests.exceptions.RequestException as e:
        print(f"Failed to get access token: {e}")
        return None


# def saveAudio(audio_data, filename='saved_audio.wav'):
#     """
#     接收上传的音频数据，使用ffmpeg转换格式，并保存到项目根目录
#     :param audio_data: 上传的音频文件对象
#     :param filename: 保存的文件名
#     :return: 转换后的音频文件路径
#     """
#     ffmpeg_path = 'E:\\3school\\GraduationDesign\\software\\ffmpeg-2024-02-26-git-a3ca4beeaa-full_build\\bin\\ffmpeg.exe'
#     # 生成原始文件路径
#     original_file_path = os.path.join(os.getcwd(), 'uploads', audio_data.name)
#
#     # 确保上传目录存在
#     os.makedirs(os.path.dirname(original_file_path), exist_ok=True)
#
#     # 保存上传的文件
#     fs = FileSystemStorage(location=os.path.dirname(original_file_path))
#     fs.save(audio_data.name, audio_data)
#     print(fs)
#     # 生成转换后的文件路径
#     converted_file_path = os.path.join(os.getcwd(), filename)
#     print(converted_file_path)
#
#     # 使用ffmpeg转换文件格式
#     command = [
#         ffmpeg_path, '-i', original_file_path,
#         '-acodec', 'pcm_s16le', '-ar', '16000', '-ac', '1',
#         converted_file_path
#     ]
#     subprocess.run(command, check=True)
#
#     # 转换完成后，删除原始文件
#     os.remove(original_file_path)
#
#     return converted_file_path
ffmpeg_path = 'E:\\3school\\GraduationDesign\\software\\ffmpeg-2024-02-26-git-a3ca4beeaa-full_build\\bin\\ffmpeg.exe'


def saveAudio(audio_data):
    """
    接收上传的音频数据（UploadedFile对象），使用ffmpeg转换格式，并保存到Nginx的临时存放区TEMP_PATH
    :param audio_data: 上传的音频文件对象
    :return: 转换后的音频文件在服务器上的路径
    """
    # 生成临时文件名，确保唯一性
    timestamp = time.strftime('%Y%m%d%H%M%S')
    random_part = '%04d' % random.randint(0, 9999)
    file_ext = '.wav'  # 目标格式
    unique_filename_prefix = f"{timestamp}_{random_part}"

    original_file_ext = os.path.splitext(audio_data.name)[1].lower()
    original_file_name = f"{unique_filename_prefix}_original{original_file_ext}"
    converted_file_name = f"{unique_filename_prefix}_converted{file_ext}"

    # 定义原始和转换后的文件路径
    save_path = os.path.join(TEMP_PATH,time.strftime('%Y%m%d'))
    mkdir(save_path)
    # 定义原始和转换后的文件路径
    original_file_path = os.path.join(save_path, original_file_name)
    converted_file_path = os.path.join(save_path, converted_file_name)
    print(f'original_file_path = {original_file_path}\nconverted_file_path = {converted_file_path}')

    # 保存原始上传的文件
    with open(original_file_path, 'wb') as f:
        for chunk in audio_data.chunks():
            f.write(chunk)

    # 使用ffmpeg进行格式转换
    command = [
        ffmpeg_path, '-i', original_file_path,
        '-acodec', 'pcm_s16le', '-ar', '16000', '-ac', '1',
        converted_file_path
    ]
    subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # 转换完成后，删除原始文件
    os.remove(original_file_path)
    file_url = IMAGE_URL + converted_file_path.replace(ATTACHMENT_PATH, "").replace("\\", "/")

    # 返回转换后的文件路径（相对于TEMP_PATH的路径，便于Nginx访问）
    return file_url,converted_file_path
