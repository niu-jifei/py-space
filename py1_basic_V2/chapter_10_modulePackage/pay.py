# 支付超时时间
timeout = 1800


# 微信支付
def wechat_pay():
    print("我是微信支付！")


# 支付宝支付
def ali_pay():
    print("我是支付宝支付！")


# 提示函数
def show_info():
    print("我是来自【支付】模块的提示！")


__all__ = ["wechat_pay", "ali_pay", "show_info"]


print("我的模块名是：" + __name__)


if __name__ == "__main__":
    ### 测试
    wechat_pay()
    ali_pay()
    show_info()
