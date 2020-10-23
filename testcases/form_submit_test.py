# NOTE: Generated By HttpRunner v3.1.4
# FROM: har/form_submit.har


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseFormSubmit(HttpRunner):

    config = Config("testcase description").verify(False)
    teststeps = [
        Step(
            RunRequest("/f/hZNPmD")
            .get("https://mo.jinshuju.net/f/hZNPmD")
            .with_headers(
                **{
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "none",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-dest": "document",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "if-none-match": 'W/"b5aa248aa3838e020aa204fa9af9829b"',
                }
            )
            .with_cookies(
                **{
                    "entry_token": "qHADiKuC",
                    "gd_ssf": "MTYwMjIzMjQzMQ%3D%3D--c5a5e463344d7e9d8829c2c08e63101611439d18",
                    "_ga": "GA1.2.669479930.1597286832",
                    "need_show_switch_modal_to_user": "false",
                    "_smt_uid": "5f4c6fcb.35bf55f7",
                    "show_template_for_double_zero_user": "true",
                    "first_login": "true",
                    "change_theme_btn_clicked_midautumn": "1579600505",
                    "clone_form_QHP5W8": "true",
                    "clone_form_kBqmBB": "true",
                    "_gd_sid_cny": "IjVmNmFkOWY3ZmM1MzI5MjcwZTYxMGJlZCI%3D--8d510789bdb388e4645532f0fc26f80332db16a1",
                    "gSi1YT_scenable_system_warning_modal_showed": "true",
                    "trial_just_started": "true",
                    "jsj_locale": "zh-CN",
                    "dashboard_layout": "thumbnail",
                    "filled_form_scene": "form",
                    "_gd_sid": "IjVmNzI5MTJmNjE5NGUyMjhmZTRhMGIzYyI%3D--a1f970135e5c5ce583536e7d6147d90c06a54f5e",
                    "_jinshuju_ut": "IjVkZDYyNjU0NjZhYjMzNDZhNzI5MjA3MiI%3D--8f535c3330099d30d8078fe3be96ec08f00eb321",
                    "_gd_m_t": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI4YjlhY2I1My0xZjcxLTRmZGMtYmY0OS1lNDk0MzhhZGE0NWEifQ.8MavzmAqhcUIQmeER1MafItvYyAA2W9h3tsqG4RS9lk",
                    "preferred_dashboard_order": "manual",
                    "_gd_sid_mo": "IjVmNzJjOTg1NWI2NTE2N2UwNjk5MGZiMyI%3D--fc5024e433b05d5587141d6507fc5bb93f5cb1c1",
                    "jsj_uid": "ec5ce3b2-5149-4620-b475-e2a633d5dccf",
                    "country_code": "CN",
                    "_gd_sid_usd": "IjVmNzNlNjUzZTVjZGM0MjlkZDRiN2RmNyI%3D--e94c00da46872bc61395523f6815fb36551bc6be",
                    "_gd_sid_uat": "IjVmNzQyNThhZDQ5NmNlNWNkMTBhYjY2ZSI%3D--b38773184151a68778b8d168e97605c6e498608b",
                    "clone_form_rd6aeD": "true",
                    "clone_form_rDMr79": "true",
                    "_gid": "GA1.2.762739099.1602208326",
                    "has_visited_dashboard_in_two_days": "true",
                    "gd_registered_from": ".com",
                    "Hm_lvt_47cd03e974df6869353431fe4f4d6b2f": "1602212241,1602214492,1602224981,1602225263",
                    "start_filling_time_rInXUo": "1602232142",
                    "mixpanel_event_history": "form_created",
                    "last_fill_entry_token": "qHADiKuC",
                    "_gd_session": "UE9GUFBOSmM3OHh5bVJiTE5BelRKSHRKblZvR3dRSTNxOVBkaitORnlkNnlNaUpnTEg4bTQ2YlVqamdwdW9JR1VwaGdOcGJWM2JLb1F1amJYQzQwRjYzcTVCdVVQSjVTRDMydXhjSXRTTElsaElrY1hISDJlTmNPb2IvUUhrWHBqTDgreWxOZWF1MlBRa1JzYkhnQlFScXlab2RwK2tQdGhlZThJbExnYWpkSEFBYXlVbHcvbjBCcExDSnRvSGpkcnl6T0QvSEkyS3JkaFd5YXd1WSt3WHFGR0pTZmY4R3dZallLemJoSXY3TnVNSGk0c3R2UmxPZjg5VGRBT1hQSVBrUUZtRmZUSjVzbkt2TE9PUjV5Q2RNZkJETUZjZU9pQ09pL1J4eGthaHVDazVMSFo1NjZNMjlwOW1keW4vT2RqcHd2dHMyUGlrRnlhYWtWWHBYUlRRPT0tLTM4OFArQ2tmOUJjajBiNGI4bGtJd0E9PQ%3D%3D--e520158728213628ad3d043e60ec9d75ea36f380",
                    "_caid": "IjVjZDRkZjdlYzNlZDFlNWUwNjQ4OWQzNyI%3D--c382a7d50514d8634098ec5aa5461b1f0e4e28a7",
                    "Hm_lpvt_47cd03e974df6869353431fe4f4d6b2f": "1602234152",
                    "_gat_gtag_UA_48208031_13": "1",
                    "csrf_token": "6C9C68g5nFJbgIAngAi//uQrZOYLBHBuWe8ptgCxMNgMFN24v0TYJHB/ho7751m03oKQmSrBA3QOpuWbGaWodQ==",
                }
            )
            .validate()

            .assert_equal("status_code", 200)

        ),
        Step(
            RunRequest("/graphql/f/hZNPmD")
            .post("https://mo.jinshuju.net/graphql/f/hZNPmD")
            .with_headers(
                **{
                    "content-length": "488",
                    "accept": "*/*",
                    "x-gd-ssf": "MTYwMjIzMjQzMQ==--c5a5e463344d7e9d8829c2c08e63101611439d18",
                    "x-csrf-token": "yRbhDDKL8wvkks9Z6deHtvdFEh9iX0YN/So0I9UPnvUtLX5fRfa3fc9tyfCSOGH8zezmYEOaNReqY/gOzBsGWA==",
                    "x-entry-token": "qHADiKuC",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
                    "content-type": "application/json;charset=UTF-8",
                    "origin": "https://mo.jinshuju.net",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mo.jinshuju.net/f/hZNPmD",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            )
            .with_cookies(
                **{
                    "_ga": "GA1.2.669479930.1597286832",
                    "need_show_switch_modal_to_user": "false",
                    "_smt_uid": "5f4c6fcb.35bf55f7",
                    "show_template_for_double_zero_user": "true",
                    "first_login": "true",
                    "change_theme_btn_clicked_midautumn": "1579600505",
                    "clone_form_QHP5W8": "true",
                    "clone_form_kBqmBB": "true",
                    "_gd_sid_cny": "IjVmNmFkOWY3ZmM1MzI5MjcwZTYxMGJlZCI%3D--8d510789bdb388e4645532f0fc26f80332db16a1",
                    "gSi1YT_scenable_system_warning_modal_showed": "true",
                    "trial_just_started": "true",
                    "jsj_locale": "zh-CN",
                    "dashboard_layout": "thumbnail",
                    "filled_form_scene": "form",
                    "_gd_sid": "IjVmNzI5MTJmNjE5NGUyMjhmZTRhMGIzYyI%3D--a1f970135e5c5ce583536e7d6147d90c06a54f5e",
                    "_jinshuju_ut": "IjVkZDYyNjU0NjZhYjMzNDZhNzI5MjA3MiI%3D--8f535c3330099d30d8078fe3be96ec08f00eb321",
                    "_gd_m_t": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI4YjlhY2I1My0xZjcxLTRmZGMtYmY0OS1lNDk0MzhhZGE0NWEifQ.8MavzmAqhcUIQmeER1MafItvYyAA2W9h3tsqG4RS9lk",
                    "preferred_dashboard_order": "manual",
                    "_gd_sid_mo": "IjVmNzJjOTg1NWI2NTE2N2UwNjk5MGZiMyI%3D--fc5024e433b05d5587141d6507fc5bb93f5cb1c1",
                    "jsj_uid": "ec5ce3b2-5149-4620-b475-e2a633d5dccf",
                    "country_code": "CN",
                    "_gd_sid_usd": "IjVmNzNlNjUzZTVjZGM0MjlkZDRiN2RmNyI%3D--e94c00da46872bc61395523f6815fb36551bc6be",
                    "_gd_sid_uat": "IjVmNzQyNThhZDQ5NmNlNWNkMTBhYjY2ZSI%3D--b38773184151a68778b8d168e97605c6e498608b",
                    "clone_form_rd6aeD": "true",
                    "clone_form_rDMr79": "true",
                    "_gid": "GA1.2.762739099.1602208326",
                    "has_visited_dashboard_in_two_days": "true",
                    "gd_registered_from": ".com",
                    "Hm_lvt_47cd03e974df6869353431fe4f4d6b2f": "1602212241,1602214492,1602224981,1602225263",
                    "start_filling_time_rInXUo": "1602232142",
                    "mixpanel_event_history": "form_created",
                    "last_fill_entry_token": "qHADiKuC",
                    "_gat_gtag_UA_48208031_13": "1",
                    "_caid": "IjVkZDYyNjU0NjZhYjMzNDZhNzI5MjA3NCI%3D--d141bd1f24ec3955b11ea186700716f2a6e71db6",
                    "start_filling_time_hZNPmD": "1602234175",
                    "_gd_session": "anVVaHFFa015OUtqRXpyY2piM2tDS3ZBZnlIRzdUR2M4THlSY2duVy9FdWZGSkhCY0F5aDdWY3NPbjJHU25iWVQxcGQ0UEF3Q1FRM1dSNHkwWmRkditTdlNFYkh0VzVTU2tSaVNMVnpNZ0kxL3VFN2drcGpSQ0JYanJJRlhnRlV0SkxTdTJybWhNTWpreHQwbCt5RHlSTVBEemwvSENWakMrOEdCVnptKzBtUVF6S3JtMThBdWRLbTdiK2tMcnczOG9rUkEwSkpvOHFCcHZMZHpFTTNtOHloM2VEUU5TcDh1SytaRGVIUHpvd0VZMGZmbmh1SitWMitIaVRZMDNGZHJwZXpzM29RdGx6QXR2eGJqeVJZeGwxZlhvVFd6SmhhZVoxK1lsMEpSd3dwR2lGd2VzRzVMZGZIeDg5RmRCbER6T2hSNHhxVHB4MkgvUERNNE11ZGFnPT0tLUo4ZG81cmlFVjZHdnZ1UGxkK0FKV3c9PQ%3D%3D--9bd9b5ec9b799ef2109de85effec6a0e86a47980",
                    "csrf_token": "yRbhDDKL8wvkks9Z6deHtvdFEh9iX0YN/So0I9UPnvUtLX5fRfa3fc9tyfCSOGH8zezmYEOaNReqY/gOzBsGWA==",
                    "Hm_lpvt_47cd03e974df6869353431fe4f4d6b2f": "1602234176",
                }
            )
            .with_json(
                {
                    "operationName": "CreatePublishedFormEntry",
                    "variables": {
                        "input": {
                            "formId": "hZNPmD",
                            "entryAttributes": {
                                "field_1": "张三123",
                                "field_2": "18383157715",
                            },
                            "captchaData": None,
                            "weixinAccessToken": None,
                            "xFieldWeixinOpenid": None,
                            "weixinInfo": None,
                            "prefilledParams": "",
                            "embedded": False,
                            "backgroundImage": False,
                            "formMargin": False,
                            "hasPreferential": False,
                            "fillingDuration": 7,
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
            RunRequest("/f/hZNPmD/success")
            .get("https://mo.jinshuju.net/f/hZNPmD/success")
            .with_headers(
                **{
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "referer": "https://mo.jinshuju.net/f/hZNPmD",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "if-none-match": 'W/"e848d68446991a7cef27de422fe6f4b2"',
                }
            )
            .with_cookies(
                **{
                    "entry_token": "fhZ4Y08X",
                    "gd_ssf": "MTYwMjIzNDE4NA%3D%3D--df99a821e9428b6cd14ba8222556e153f12096c8",
                    "formSubmitSuccess": "1",
                    "_ga": "GA1.2.669479930.1597286832",
                    "need_show_switch_modal_to_user": "false",
                    "_smt_uid": "5f4c6fcb.35bf55f7",
                    "show_template_for_double_zero_user": "true",
                    "first_login": "true",
                    "change_theme_btn_clicked_midautumn": "1579600505",
                    "clone_form_QHP5W8": "true",
                    "clone_form_kBqmBB": "true",
                    "_gd_sid_cny": "IjVmNmFkOWY3ZmM1MzI5MjcwZTYxMGJlZCI%3D--8d510789bdb388e4645532f0fc26f80332db16a1",
                    "gSi1YT_scenable_system_warning_modal_showed": "true",
                    "trial_just_started": "true",
                    "jsj_locale": "zh-CN",
                    "dashboard_layout": "thumbnail",
                    "filled_form_scene": "form",
                    "_gd_sid": "IjVmNzI5MTJmNjE5NGUyMjhmZTRhMGIzYyI%3D--a1f970135e5c5ce583536e7d6147d90c06a54f5e",
                    "_jinshuju_ut": "IjVkZDYyNjU0NjZhYjMzNDZhNzI5MjA3MiI%3D--8f535c3330099d30d8078fe3be96ec08f00eb321",
                    "_gd_m_t": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI4YjlhY2I1My0xZjcxLTRmZGMtYmY0OS1lNDk0MzhhZGE0NWEifQ.8MavzmAqhcUIQmeER1MafItvYyAA2W9h3tsqG4RS9lk",
                    "preferred_dashboard_order": "manual",
                    "_gd_sid_mo": "IjVmNzJjOTg1NWI2NTE2N2UwNjk5MGZiMyI%3D--fc5024e433b05d5587141d6507fc5bb93f5cb1c1",
                    "jsj_uid": "ec5ce3b2-5149-4620-b475-e2a633d5dccf",
                    "country_code": "CN",
                    "_gd_sid_usd": "IjVmNzNlNjUzZTVjZGM0MjlkZDRiN2RmNyI%3D--e94c00da46872bc61395523f6815fb36551bc6be",
                    "_gd_sid_uat": "IjVmNzQyNThhZDQ5NmNlNWNkMTBhYjY2ZSI%3D--b38773184151a68778b8d168e97605c6e498608b",
                    "clone_form_rd6aeD": "true",
                    "clone_form_rDMr79": "true",
                    "_gid": "GA1.2.762739099.1602208326",
                    "has_visited_dashboard_in_two_days": "true",
                    "gd_registered_from": ".com",
                    "Hm_lvt_47cd03e974df6869353431fe4f4d6b2f": "1602212241,1602214492,1602224981,1602225263",
                    "start_filling_time_rInXUo": "1602232142",
                    "mixpanel_event_history": "form_created",
                    "_gat_gtag_UA_48208031_13": "1",
                    "_caid": "IjVkZDYyNjU0NjZhYjMzNDZhNzI5MjA3NCI%3D--d141bd1f24ec3955b11ea186700716f2a6e71db6",
                    "csrf_token": "yRbhDDKL8wvkks9Z6deHtvdFEh9iX0YN/So0I9UPnvUtLX5fRfa3fc9tyfCSOGH8zezmYEOaNReqY/gOzBsGWA==",
                    "Hm_lpvt_47cd03e974df6869353431fe4f4d6b2f": "1602234176",
                    "last_fill_entry_token": "fhZ4Y08X",
                    "_gd_session": "MHNLQVVBVk5nVmtXdkQxODlSQUlaQk9mOUZvTy8zcXJqcmNpS0xWSXhFTzIvbmlETkR2OVVTQXRMY0xsSGNpcDVYR291NFRydVhIaTUyZk1VTHRkQ2VUa2dsT2RzeU5YY2tyNEMxNTNBMHVmdnBwOVAwM0MxOXhWUjZlS25GRXRCVHNGN014YTFnOUQ5VGdDSlZMclhJR0xJMXNaUXUrTHNXOWlBczVpVnVyVzFDYjJZSWhMak5aU040RS90MHZRdkVFY280eWRObFRaYjl6N2JJYXkyK0hDYmJDQkhQNTFva0I5VU9XcWQzNVZFOWtZYkVhcUlWRUM4YkhBbHhmQjZoaGp2VCt0dzBJMFJiRFVFZWdqL29JV0VyOUoxYi9ENG9HdnB1K3ZKaUtDcExTT3FUVnNnblJlK05OS0oyVzFLRjVFUHNOQWRkQldNdFF5MVRSVU9RPT0tLVJaRnIwUmRPbllFZGlkbG10eEVhOFE9PQ%3D%3D--0f75c1c93106be4328b75c8c080ae1f6a73dfd07",
                }
            )
            .validate()
            .assert_equal("status_code", 200)

        ),
    ]


if __name__ == "__main__":
    TestCaseFormSubmit().test_start()