import json

import requests


def get_hitokoto():
    url = "https://v1.hitokoto.cn"
    headers = {
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "v1.hitokoto.cn",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    return json.loads(response.text)

# {
#     "id": 4629,
#     "hitokoto": "千军万马滚滚来，不知何人留情怀！",
#     "type": "a",
#     "from": "Other",
#     "creator": "Sariay",
#     "created_at": "1567970631"
# }
