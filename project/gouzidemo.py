from flask import Flask
from flask import request
app = Flask(__name__)

####
@app.before_first_request  #### 当第一个请求到达的时候执行
def demo01():
    """
    demo01 这个函数：  做一些项目的初始化配制
    :return:
    """

    print ("before_first_request")
@app.before_request
def demo02():
    ### 获取用户的信息
    ###  获取用户的session   cookie
    ### 校验用户的身份
    print("before_request")
    userid = request.args.get("id")
    if not userid:
        return "缺少请求信息"


@app.after_request
def demo03(response):
    print ("after_request")
    ## 返回结构
    # result = {
    #     "code":response.get("code"),
    #     "data":response.get("data"),
    #     "version":"v1"
    # }

    ##  构建返回的结构
    return "hello"
@app.teardown_request
def demo04(response):
    print (response)
    print("teardown_request")
    ### 写log日志






@app.route("/index/")
def index():
    ####
    # params = {code data msg}
    1 /0
    return "index"

if __name__ == '__main__':
    app.run()

