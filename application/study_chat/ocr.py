import base64
import urllib
import requests
import secret_key

API_KEY = secret_key.ocr_api_key
SECRET_KEY = secret_key.ocr_secret_key


def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded
    :return: base64编码信息
    """
    try:
        with open(path, "rb") as f:
            content = base64.b64encode(f.read()).decode("utf8")
            if urlencoded:
                content = urllib.parse.quote_plus(content)
        return content
    except Exception as e:
        print("Error reading file:", e)
        return None


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    try:
        response = requests.post(url, params=params).json()
        return response.get("access_token")
    except Exception as e:
        print("Error retrieving access token:", e)
        return None







def get_ocr_results(path):
    """
    提交图像进行OCR识别
    :param path: 图像文件路径
    :return: 字典，包含code、msg和data键
    """
    access_token = get_access_token()
    if access_token is None:
        return {"code": 1, "msg": "No access token retrieved, can't proceed with OCR.", "data": ""}

    url = f"https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token={access_token}"
    payload = 'image=' + get_file_content_as_base64(path, True)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()  # Raises HTTPError for bad requests
        ocr_result = response.json()

        # Check if words_result is in the JSON response
        if 'words_result' in ocr_result:
            # Join the words from all items in the words_result list
            words = '\n'.join(item['words'] for item in ocr_result['words_result'])
            return {"code": 0, "msg": "OCR succeeded.", "data": words}
        else:
            return {"code": 2, "msg": "No words_result in response.", "data": ""}

    except requests.exceptions.HTTPError as http_err:
        return {"code": 3, "msg": f"HTTP error occurred: {http_err}", "data": ""}
    except Exception as e:
        return {"code": 4, "msg": f"Other error occurred: {e}", "data": ""}



#
# if __name__ == '__main__':
#     # path = r"E:\3school\GraduationDesign\software\uploads\chat\image\20231124_122144_0001.jpg"
#     path = r"E:\Pictures\照片\2023-03-05 073212.jpg"
#     text = get_ocr_results(path)
#     print(text)

