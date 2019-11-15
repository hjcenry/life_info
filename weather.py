import json

import requests


def get_weather():
    url = "http://t.weather.sojson.com/api/weather/city/101010100"
    headers = {
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "t.weather.sojson.com",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    return json.loads(response.text)

# {
#     "message": "success感谢又拍云(upyun.com)提供CDN赞助",
#     "status": 200,
#     "date": "20191115",
#     "time": "2019-11-16 01:13:11",
#     "cityInfo": {
#         "city": "北京市",
#         "citykey": "101010100",
#         "parent": "北京",
#         "updateTime": "23:47"
#     },
#     "data": {
#         "shidu": "67%",
#         "pm25": 35.0,
#         "pm10": 67.0,
#         "quality": "良",
#         "wendu": "5",
#         "ganmao": "极少数敏感人群应减少户外活动",
#         "forecast": [
#             {
#                 "date": "15",
#                 "high": "高温 9℃",
#                 "low": "低温 2℃",
#                 "ymd": "2019-11-15",
#                 "week": "星期五",
#                 "sunrise": "06:57",
#                 "sunset": "16:59",
#                 "aqi": 64,
#                 "fx": "东南风",
#                 "fl": "<3级",
#                 "type": "晴",
#                 "notice": "愿你拥有比阳光明媚的心情"
#             },
#             {
#                 "date": "16",
#                 "high": "高温 9℃",
#                 "low": "低温 2℃",
#                 "ymd": "2019-11-16",
#                 "week": "星期六",
#                 "sunrise": "06:58",
#                 "sunset": "16:59",
#                 "aqi": 83,
#                 "fx": "东北风",
#                 "fl": "<3级",
#                 "type": "多云",
#                 "notice": "阴晴之间，谨防紫外线侵扰"
#             },
#             {
#                 "date": "17",
#                 "high": "高温 9℃",
#                 "low": "低温 -3℃",
#                 "ymd": "2019-11-17",
#                 "week": "星期日",
#                 "sunrise": "06:59",
#                 "sunset": "16:58",
#                 "aqi": 53,
#                 "fx": "西北风",
#                 "fl": "4-5级",
#                 "type": "多云",
#                 "notice": "阴晴之间，谨防紫外线侵扰"
#             },
#             {
#                 "date": "18",
#                 "high": "高温 5℃",
#                 "low": "低温 -5℃",
#                 "ymd": "2019-11-18",
#                 "week": "星期一",
#                 "sunrise": "07:01",
#                 "sunset": "16:57",
#                 "aqi": 47,
#                 "fx": "西风",
#                 "fl": "<3级",
#                 "type": "晴",
#                 "notice": "愿你拥有比阳光明媚的心情"
#             },
#             {
#                 "date": "19",
#                 "high": "高温 6℃",
#                 "low": "低温 -4℃",
#                 "ymd": "2019-11-19",
#                 "week": "星期二",
#                 "sunrise": "07:02",
#                 "sunset": "16:56",
#                 "aqi": 48,
#                 "fx": "北风",
#                 "fl": "<3级",
#                 "type": "晴",
#                 "notice": "愿你拥有比阳光明媚的心情"
#             },
#             {
#                 "date": "20",
#                 "high": "高温 7℃",
#                 "low": "低温 -3℃",
#                 "ymd": "2019-11-20",
#                 "week": "星期三",
#                 "sunrise": "07:03",
#                 "sunset": "16:56",
#                 "aqi": 90,
#                 "fx": "南风",
#                 "fl": "<3级",
#                 "type": "晴",
#                 "notice": "愿你拥有比阳光明媚的心情"
#             },
#             {
#                 "date": "21",
#                 "high": "高温 9℃",
#                 "low": "低温 -2℃",
#                 "ymd": "2019-11-21",
#                 "week": "星期四",
#                 "sunrise": "07:04",
#                 "sunset": "16:55",
#                 "fx": "北风",
#                 "fl": "<3级",
#                 "type": "晴",
#                 "notice": "愿你拥有比阳光明媚的心情"
#             },
#             {
#                 "date": "22",
#                 "high": "高温 10℃",
#                 "low": "低温 0℃",
#                 "ymd": "2019-11-22",
#                 "week": "星期五",
#                 "sunrise": "07:05",
#                 "sunset": "16:54",
#                 "fx": "西北风",
#                 "fl": "<3级",
#                 "type": "阴",
#                 "notice": "不要被阴云遮挡住好心情"
#             },
#             {
#                 "date": "23",
#                 "high": "高温 7℃",
#                 "low": "低温 0℃",
#                 "ymd": "2019-11-23",
#                 "week": "星期六",
#                 "sunrise": "07:06",
#                 "sunset": "16:54",
#                 "fx": "西北风",
#                 "fl": "<3级",
#                 "type": "多云",
#                 "notice": "阴晴之间，谨防紫外线侵扰"
#             },
#             {
#                 "date": "24",
#                 "high": "高温 4℃",
#                 "low": "低温 0℃",
#                 "ymd": "2019-11-24",
#                 "week": "星期日",
#                 "sunrise": "07:07",
#                 "sunset": "16:53",
#                 "fx": "北风",
#                 "fl": "<3级",
#                 "type": "阴",
#                 "notice": "不要被阴云遮挡住好心情"
#             },
#             {
#                 "date": "25",
#                 "high": "高温 7℃",
#                 "low": "低温 0℃",
#                 "ymd": "2019-11-25",
#                 "week": "星期一",
#                 "sunrise": "07:08",
#                 "sunset": "16:53",
#                 "fx": "北风",
#                 "fl": "<3级",
#                 "type": "雨夹雪",
#                 "notice": "道路湿滑，步行开车要谨慎"
#             },
#             {
#                 "date": "26",
#                 "high": "高温 3℃",
#                 "low": "低温 -2℃",
#                 "ymd": "2019-11-26",
#                 "week": "星期二",
#                 "sunrise": "07:10",
#                 "sunset": "16:52",
#                 "fx": "东风",
#                 "fl": "<3级",
#                 "type": "雨夹雪",
#                 "notice": "道路湿滑，步行开车要谨慎"
#             },
#             {
#                 "date": "27",
#                 "high": "高温 2℃",
#                 "low": "低温 -4℃",
#                 "ymd": "2019-11-27",
#                 "week": "星期三",
#                 "sunrise": "07:11",
#                 "sunset": "16:52",
#                 "fx": "西北风",
#                 "fl": "<3级",
#                 "type": "多云",
#                 "notice": "阴晴之间，谨防紫外线侵扰"
#             },
#             {
#                 "date": "28",
#                 "high": "高温 1℃",
#                 "low": "低温 -4℃",
#                 "ymd": "2019-11-28",
#                 "week": "星期四",
#                 "sunrise": "07:12",
#                 "sunset": "16:51",
#                 "fx": "西风",
#                 "fl": "<3级",
#                 "type": "晴",
#                 "notice": "愿你拥有比阳光明媚的心情"
#             },
#             {
#                 "date": "29",
#                 "high": "高温 3℃",
#                 "low": "低温 -3℃",
#                 "ymd": "2019-11-29",
#                 "week": "星期五",
#                 "sunrise": "07:13",
#                 "sunset": "16:51",
#                 "fx": "西北风",
#                 "fl": "<3级",
#                 "type": "晴",
#                 "notice": "愿你拥有比阳光明媚的心情"
#             }
#         ],
#         "yesterday": {
#             "date": "14",
#             "high": "高温 10℃",
#             "low": "低温 -2℃",
#             "ymd": "2019-11-14",
#             "week": "星期四",
#             "sunrise": "06:56",
#             "sunset": "17:00",
#             "aqi": 70,
#             "fx": "北风",
#             "fl": "<3级",
#             "type": "晴",
#             "notice": "愿你拥有比阳光明媚的心情"
#         }
#     }
# }
