from flask import Flask

app = Flask(__name__)   ## 实例app实例

@app.route("/")   ### 路由
def index():  ## 视图
    return "helloworld"   ## 返回值

@app.route("/hello1/<path:url>")
def hello1(url):
    print (url)

    return "hello1"

@app.route("/hello/<string:username>/<int:age>")
def hello(username,age):
    print (type(age))
    return "我的名字是%s,年龄%s" % (username,age)

@app.route("/hello2/<uuid:id>")
def hello2(id):
    print (id)
    return "hello2"

from flask import request
@app.route("/reqdemo/",methods=["post","get"])
def reqdemo():
    ## 获取get请求参数
    # data = request.args.get("name")
    # data = request.args.get("age")
    # print (data)
    ## post请求参数
    print (request.form)
    name = request.form.get("name")
    age = request.form.get("age")
    print (request.method)
    return "reqdemo name: %s age %s" %(name,age)

from flask import redirect,render_template
@app.route("/getindex")
def getindex():
    # return render_template("index.html",name="zhangsan",age=19)
    # name = "lisi"
    # age_new = 19
    # return render_template("index.html",name=name,age=age_new)
    name = "hello1"
    age = 20
    mydict = {"shuxue":100,"yuwen":50}
    return render_template("index.html",**locals())




if __name__ == '__main__':
    # app.run()   ## 项目启动
    app.run(host="0.0.0.0",port=8000,debug=True)
    ## 开启debug模式： 1.显示错误内容   2. 修改代码之后自动重启

