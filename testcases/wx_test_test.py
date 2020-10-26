# NOTE: Generated By HttpRunner v3.1.4
# FROM: har/wx_test.har


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseWxTest(HttpRunner):

    config = Config("testcase description").verify(False)

    teststeps = [
        Step(
            RunRequest("/connect/oauth2/authorize")
            .get("https://open.weixin.qq.com/connect/oauth2/authorize")
            .with_params(
                **{
                    "appid": "wx550b63b744e492ec",
                    "redirect_uri": "https://wx.jinshuju.net/weixin_oauth/callback?form_id=oIR3qk",
                    "response_type": "code",
                    "scope": "snsapi_base",
                    "state": "published_form_base",
                    "connect_redirect": "1",
                }
            )
            .with_headers(
                **{
                    "pragma": "no-cache",
                    "cache-control": "no-cache",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 micromessenger/7.0.17(0x17001127) NetType/WIFI Language/zh_CN",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "none",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .extract()
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseWxTest().test_start()
