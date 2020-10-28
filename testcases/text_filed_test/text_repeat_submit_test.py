# NOTE: Generated By HttpRunner v3.1.4
# FROM: har/text_repeat_submit.har


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseTextRepeatSubmit(HttpRunner):

    config = Config("testcase description").verify(False)

    teststeps = [
        Step(
            RunRequest("打开表单")
            .get("https://mo.jinshuju.net/f/FvUXs9")
            .with_headers(
                **{
                    "cache-control": "max-age=0",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                    "if-none-match": 'W/"92522910a30f6206c7692e6863d38172"',
                }
            )
            .with_cookies(
                **{
                    "jsj_uid": "91864945-fa8e-43da-a3b4-7d27a3382d66",
                    "start_filling_time_FvUXs9": "1603706485",
                    "Hm_lvt_47cd03e974df6869353431fe4f4d6b2f": "1603706487",
                    "Hm_lpvt_47cd03e974df6869353431fe4f4d6b2f": "1603706487",
                    "_ga": "GA1.2.1959073059.1603706487",
                    "_gid": "GA1.2.2099179606.1603706487",
                    "csrf_token": "0rXyRjmnwjaQJLOGg57+sDMtrKTHWZvZGfaMY19ppkBnOxEje3rbHR549sQVEC8suwvNCp2Xq9+XmY+lxpN0XA==",
                    "_gd_session": "STVPNGNkYlNUWUQ2anYrVGZMSHZwN09xdnNpSFVBR1NGWVltc0VINUZlc2JCeTcrazJCMVVhZjU3ZUNwYXBkdDIya1RTQ3B6RVRiV2pNc3NVSmNBdUpxYzlrMUZvQTBTQVZDZWxiajJhM3dLeGtMMEZwdFhjMDk0OFU2N3FrZG9KdXRWVkQxTFBPK2NteXY3UUVTTXdBPT0tLW05NTJ5MGtVWUJhdUdHRlNzV3A4OXc9PQ%3D%3D--ed0d121ea9db8646afb363e33a0cee26b1774a48",
                    "filled_form_scene": "form",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("第一次提交")
            .post("https://mo.jinshuju.net/graphql/f/FvUXs9")
            .with_headers(
                **{
                    "content-length": "464",
                    "accept": "*/*",
                    "x-csrf-token": "L04/HeAwNAUIYmvT9P5r4QaCexxeTRaU8UmnYIF60naawNx4ou0tLoY+LpFicLp9jqQasgSDJpJ/JqSmGIAAag==",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                    "content-type": "application/json;charset=UTF-8",
                    "origin": "https://mo.jinshuju.net",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mo.jinshuju.net/f/FvUXs9",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "jsj_uid": "91864945-fa8e-43da-a3b4-7d27a3382d66",
                    "Hm_lvt_47cd03e974df6869353431fe4f4d6b2f": "1603706487",
                    "_ga": "GA1.2.1959073059.1603706487",
                    "_gid": "GA1.2.2099179606.1603706487",
                    "filled_form_scene": "form",
                    "start_filling_time_FvUXs9": "1603706555",
                    "csrf_token": "L04/HeAwNAUIYmvT9P5r4QaCexxeTRaU8UmnYIF60naawNx4ou0tLoY+LpFicLp9jqQasgSDJpJ/JqSmGIAAag==",
                    "Hm_lpvt_47cd03e974df6869353431fe4f4d6b2f": "1603706556",
                    "_gat_gtag_UA_48208031_13": "1",
                    "_gd_session": "dzFBb0hvSW9MbU5vYnNTV1BTUVk1d3RRSW05elBwdEliS0R5NDFQM3dTMGhiZWdHeUkyL25haUhEdktvNzRKRnBaY3pyRzlnTWVhcytBS084NWpuY3pOMUlVK3Z0d1pZMzR4bkxQUDZ3dVFtRitiS1lENi9INGRoVGRwU3B4UlpsNWNaTzZnQmRwTXRZdjJlM0g2UkdRPT0tLTQydVN5bnBxOU9lOUR2Mmh0NWVoQUE9PQ%3D%3D--e7b2755a672639ec34a097da9899eedde096bd8b",
                }
            )
            .with_json(
                {
                    "operationName": "CreatePublishedFormEntry",
                    "variables": {
                        "input": {
                            "formId": "FvUXs9",
                            "entryAttributes": {"field_1": "${get_random_name()}"},
                            "captchaData": None,
                            "weixinAccessToken": None,
                            "xFieldWeixinOpenid": None,
                            "weixinInfo": None,
                            "prefilledParams": "",
                            "embedded": False,
                            "backgroundImage": False,
                            "formMargin": False,
                            "hasPreferential": False,
                            "fillingDuration": 3,
                        }
                    },
                    "extensions": {
                        "persistedQuery": {
                            "version": 1,
                            "sha256Hash": "4cd6a9aef2820b2c3215f6ddfa87093869461f76f3f2016738f4307268a7df98",
                        }
                    },
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("提交成功页面")
            .get("https://mo.jinshuju.net/f/FvUXs9/success")
            .with_params(
                **{
                    "e_token": "eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjpbIlRvaTZBYk1uIiwiNWY5NjllNTM1YjY1MTYyNmJlOGJiZjQyIl0sImV4cCI6MTYwMzc5Mjk2MH0.LhVj7eM2ceL_wnH4TaUnnj00yFkIPE69Cu0XVIbg51M"
                }
            )
            .with_headers(
                **{
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "referer": "https://mo.jinshuju.net/f/FvUXs9",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "entry_token": "Toi6AbMn",
                    "gd_ssf": "MTYwMzcwNjU2MA%3D%3D--9ab0135809109082c6c033a891ffc35c9b45d28b",
                    "formSubmitSuccess": "1",
                    "jsj_uid": "91864945-fa8e-43da-a3b4-7d27a3382d66",
                    "Hm_lvt_47cd03e974df6869353431fe4f4d6b2f": "1603706487",
                    "_ga": "GA1.2.1959073059.1603706487",
                    "_gid": "GA1.2.2099179606.1603706487",
                    "filled_form_scene": "form",
                    "csrf_token": "L04/HeAwNAUIYmvT9P5r4QaCexxeTRaU8UmnYIF60naawNx4ou0tLoY+LpFicLp9jqQasgSDJpJ/JqSmGIAAag==",
                    "Hm_lpvt_47cd03e974df6869353431fe4f4d6b2f": "1603706556",
                    "_gat_gtag_UA_48208031_13": "1",
                    "last_fill_entry_token": "Toi6AbMn",
                    "_gd_session": "MlRUUWlXbWhvaWt3QTg0ZTdaUHVZRzZacVlGaTlpbUFFSVc0MUdDM0lYNWRLRVZTVXovem1uaVIyMDNPdDFydzVXQ3FWNDVSWUFCVExiNTdhMUlVa1RyQ2tQaDFPTjNuMmIrSGJkSzRNemdxMCsyQUgrU3UwNUFFZzhSQm1JT0xhQzFhRUpTQ3RMWVB3UEh6SXFTYWRnPT0tLVhBM2FNdU15N0VLbVJoREJsV3ZCZ2c9PQ%3D%3D--1e7d30e73384f3704c29bc5463ac772f9f87228e",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("第二次提交")
            .post("https://mo.jinshuju.net/graphql/f/FvUXs9")
            .with_headers(
                **{
                    "content-length": "464",
                    "accept": "*/*",
                    "x-gd-ssf": "MTYwMzcwNjU2MA==--9ab0135809109082c6c033a891ffc35c9b45d28b",
                    "x-csrf-token": "7yDZv2fCI7roz5Wu0CSEyMotnsrwmfxaivi1xAToB5xarjraJR86kWaT0OxGqlVUQgv/ZKpXzFwEl7YCnRLVgA==",
                    "x-entry-token": "Toi6AbMn",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                    "content-type": "application/json;charset=UTF-8",
                    "origin": "https://mo.jinshuju.net",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mo.jinshuju.net/f/FvUXs9",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "jsj_uid": "91864945-fa8e-43da-a3b4-7d27a3382d66",
                    "Hm_lvt_47cd03e974df6869353431fe4f4d6b2f": "1603706487",
                    "_ga": "GA1.2.1959073059.1603706487",
                    "_gid": "GA1.2.2099179606.1603706487",
                    "filled_form_scene": "form",
                    "_gat_gtag_UA_48208031_13": "1",
                    "last_fill_entry_token": "Toi6AbMn",
                    "referer_url": "https%3A%2F%2Fmo.jinshuju.net%2Ff%2FFvUXs9",
                    "start_filling_time_FvUXs9": "1603706564",
                    "csrf_token": "7yDZv2fCI7roz5Wu0CSEyMotnsrwmfxaivi1xAToB5xarjraJR86kWaT0OxGqlVUQgv/ZKpXzFwEl7YCnRLVgA==",
                    "Hm_lpvt_47cd03e974df6869353431fe4f4d6b2f": "1603706565",
                    "_gd_session": "SER1dS9GWnBOWDVMdjdnOU5DSy9oK0NSaTZzVVFOeFZ0SXVFRThUemNjRE9Qc2lnRDBSb0dJc3hWTkcxTEtrS3U1ZnRZekQ2TFp0M0tPa0w4QUZBN05ISURURXI1VisyWUpWaER5OWNPYnBCK2FnQU8zQnB6U3o4ZEk4cmNLRmQ5SHBaRllsTzJ0N2dSYm5KSEtER253PT0tLU1HR1FNcGZQTTFLVnNZQnhGWjZ2d1E9PQ%3D%3D--27310416dc85efdf0a75966a2ba8f91408f4632f",
                }
            )
            .with_json(
                {
                    "operationName": "CreatePublishedFormEntry",
                    "variables": {
                        "input": {
                            "formId": "FvUXs9",
                            "entryAttributes": {"field_1": "${get_random_name()}"[1]},
                            "captchaData": None,
                            "weixinAccessToken": None,
                            "xFieldWeixinOpenid": None,
                            "weixinInfo": None,
                            "prefilledParams": "",
                            "embedded": False,
                            "backgroundImage": False,
                            "formMargin": False,
                            "hasPreferential": False,
                            "fillingDuration": 4,
                        }
                    },
                    "extensions": {
                        "persistedQuery": {
                            "version": 1,
                            "sha256Hash": "4cd6a9aef2820b2c3215f6ddfa87093869461f76f3f2016738f4307268a7df98",
                        }
                    },
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseTextRepeatSubmit().test_start()
