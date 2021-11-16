import requests
import os


def send_message():

    # url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=62002e06-2ebf-41c3-a17f-b99b31b284c2"  # test 机器人
    # url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=7e39ce84-77c9-4882-b637-314a8ceb52bd"  # dce406机器人

    if os.getenv("WEIXIN_URL") is None:
        url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=62002e06-2ebf-41c3-a17f-b99b31b284c2"
    else:
        url = os.getenv("WEIXIN_URL")

    header = {
        "Content-Type": "application/json"
    }

    body = {
        "msgtype": "markdown",
        "markdown": {
            "content":
                f"DX-ARCH冒烟测试完成\n"
                f"请登录[Jenkins](http://10.6.111.2:8080/job/dx-arch-test/)查看测试报告\n"
            }
    }
    response = requests.post(url=url, json=body, headers=header)
    print(response.content)


if __name__ == "__main__":
    # initLogging()
    print("run")
    send_message()