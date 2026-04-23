"""
使用传统方式下载图片：
如下代码的特点：图片是一张一张下载的，当前图片没有下载完成，后一张图片的下载就不能开始，这属于典型的同步下载。
"""

import requests
import time


def download_picture(url):
    print(f"开始下载：{url}")
    # 发送网络请求，获取这张图片
    response = requests.get(url)
    print("下载完毕")
    # 保存图片到本地
    with open(url[-10:], "wb") as file:
        file.write(response.content)


def main():

    print("开始下载图片")
    start = time.time()

    url_list = [
        "https://n.sinaimg.cn/spider20260129/217/w600h417/20260129/3e26-917ee55a8a42b8626807c332c24981de.png",
        "https://n.sinaimg.cn/finance/transform/97/w630h267/20260129/97c4-b211cc51784830f09ee19e450475c93b.png",
        "https://n.sinaimg.cn/spider20260129/539/w1439h700/20260129/e09a-cc2ca319e00f701ccfca3ebc62aa8772.png",
    ]
    for url in url_list:
        download_picture(url)

    end = time.time()
    print(f"下载完毕，耗时：{end - start}")


main()
