import requests
import json
import re


def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """

    url = ("https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&"
           "client_id=qIYVwQtAnxYnjuH9MT6vkB3f&client_secret=gcgEjrP3rCFWu4cQcB2J2bMaiOUTjstl")
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


def get_response(file_path):
    url = ("https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/"
           "completions_pro?access_token=") + get_access_token()
    file_content = open(file_path, "r").read()
    file_content = re.sub(r"\s+", " ", file_content)[:1000]
    prompt = open("prompt.txt", "r").read()

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": file_content + prompt
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return json.loads(response.text)["result"]
