import requests

url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx550b63b744e492ec&redirect_uri=https%3A%2F%2Fwx.jinshuju.net%2Fweixin_oauth%2Fcallback%3Fform_id%3DoIR3qk&response_type=code&scope=snsapi_base&state=published_form_base&connect_redirect=1#wechat_redirect"

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 micromessenge/7.0.17(0x17001127) NetType/WIFI Language/zh_CN",
    "accept-language": "zh-cn",
    "accept-encoding": "gzip, deflate, br",
}
re = requests.get(url=url, headers=headers)

print(re.text)
