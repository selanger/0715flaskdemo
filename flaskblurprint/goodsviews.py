from flask import Flask,Blueprint,request
from flask import current_app,g
g_views = Blueprint("goods_views",__name__)


@g_views.before_request
def demo01():
    user_name = request.args.get("username")
    g.user_name = user_name


def outer(func):
    def inner():
        ##  通过request 获取了用户的username
        ## 查询到了用户的  user_id
        user_id = 1
        g.user_id = user_id

        return func()
    return inner

@g_views.route("/index/")
@outer
def index():
    ###  也需要获取用户id
    ###    request 获取到用户的username
    ##    查询用户   user_id
    user_id = g.user_id
    user_name = g.user_name
    print (user_id)
    print (user_name)
    mymd5()
    return "goods views index"


def mymd5():
    ## md5   需要密钥
    ##从app的配置文件中 取到 密钥
    ## 第一种 导入app  从app中取配置信息    app.config["SECRET_KEY"]

    #
    config = current_app.config
    value = config.get("SECRET_KEY")
    print(value)


    return "我是加密后的结果"
