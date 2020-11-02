from selenium import webdriver




# 设置屏幕尺寸
WIDTH = 320
HEIGHT = 640
PIXEL_RATIO = 3.0

# 设置User-Agent ---重要
UA = "Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3"

# URL地址

url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx550b63b744e492ec&redirect_uri=https%3A%2F%2Fwx.jinshuju.net%2Fweixin_oauth%2Fcallback%3Fform_id%3DoIR3qk&response_type=code&scope=snsapi_base&state=published_form_base&connect_redirect=1#wechat_redirect"

# 设备信息
mobile_emulation = {
    "deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO},
    "userAgent": UA,
}

options = webdriver.ChromeOptions()
options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(options=options)
driver.get(url)

