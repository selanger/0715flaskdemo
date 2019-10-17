from flask import render_template
from main import app
from getDate import MyDate
from models import *
from flask import request,redirect
from settings import STATIC_PATH
import hashlib
import functools
from flask import session

def set_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result


def LoginVaild(func):
    @functools.wraps(func)  ## 保留原来的函数名字
    def inner(*args,**kwargs):
        user_id = request.cookies.get("user_id")
        email = request.cookies.get("email")
        session_email = session.get("email")
        print (session_email)
        if user_id and email and email == session_email:
            ##
            user = User.query.filter(User.email == email,User.id==user_id).first()
            if user:
                return func(*args,**kwargs)
            else:
                return redirect("/login/")
        else:
            return redirect("/login/")
    return inner


@app.route("/index/")
@LoginVaild
def index():
    ## userinfo 数据
    # userinfo = UserInfo(name="python",age=19)
    # userinfo.save()
    data = UserInfo.query.get(7)
    return render_template("index.html",data=data)
@app.route("/userinfo/")
@LoginVaild
def userinfo():
    obj = MyDate()
    result = obj.get_date()

    return render_template("userinfo.html",**locals())


@app.route("/register1/",methods=["get","post"])
def register1():
    if request.method == "POST":
        ## 注册
        email = request.form.get("email")
        password= request.form.get("password")
        data = User.query.filter(User.email == email).first()
        if data:
            ## 存在
            return redirect("http://www.baidu.com")
        user = User(email = email,password = password)
        user.save()

    return "注册成功"
    # return render_template("register.html")


@app.route("/perfect/information/",methods=["get","post"])
def perfect_information():
    if request.method == "POST":
        ## 注册
        user_id = request.form.get("id")
        ### 获取图片  图片的名字   获取图片的内容   保存图片
        ### 数据中存 图片路径
        photo = request.files.get("photo")

        user = User.query.filter(User.id == user_id).first()
        if user:
            ##  保存图片
            import os
            file_name = photo.filename
            photo_path = os.path.join("img",file_name)   ##img/xxx.jpg
            path = os.path.join(STATIC_PATH,photo_path)
            photo.save(path)
            ## 将图片路径存在数据库中
            user.photo = photo_path
            user.merge()
        else:
            return "用户不存在"
    # return "增加信息成功"
    user = User.query.filter(User.id ==1).first()
    photo = user.photo
    return render_template("photo.html",**locals())

## 登录
@app.route("/login/",methods=["get","post"])
def login():
    error = ""
    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")
        if email and password:
            user = User.query.filter_by(email = email,password=set_password(password)).first()
            if user is not None:
                # return redirect("/index/")
                response = redirect("/index/")
                response.set_cookie("email",user.email)
                response.set_cookie("user_id",str(user.id))
                session["email"] = user.email
                return response
            else:
                error = "邮箱或者密码错误"

        else:
            error = "参数不能为空"
    return render_template("login.html",error = error)

@app.route("/register/",methods=["get","post"])
def register():
    error = ""
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if email and password:
            user = User.query.filter(User.email == email).first()
            if user:
                error = "邮箱已存在"
            else:
                user = User()
                user.email = email
                user.password = set_password(password)
                user.save()
                return redirect("/login/")
        else:
            error = "参数不能为空"
    return render_template("register.html",error = error)

@app.route("/logout/",methods=["get","post"])
def logout():
    rep = redirect("/login/")
    rep.delete_cookie("email")
    rep.delete_cookie("user_id")
    session.pop("email")
    del session["email"]
    return rep

@app.route("/testget/")
def testget():
    # name = request.args.get("name",None)
    name = request.form.get("name",None)
    print (name)
    return render_template("testget.html")
import time
from main import csrf
@app.route("/leave_list/",methods=["get","post"])
@LoginVaild
@csrf.exempt
def leave_list():
    if request.method == "POST":
        user_id = request.cookies.get("user_id")
        data = request.form
        print (type(request.form.get("start_time")))
        start_time = data.get("start_time")
        end_time = data.get("end_time")
        ## 保存数据
        leave = Leave()
        leave.request_id = int(user_id)  ## 请假人id
        leave.request_name = data.get("username")  ## 请假人姓名
        leave.request_type = data.get("type")  ### 假期类型
        leave.request_start = start_time  ## 请假的开始时间
        leave.request_end = end_time ## 请假的结束时间
        leave.request_description = data.get("dec")  ## 请假描述
        leave.request_phone = data.get("phone")  ###联系人手机号
        leave.request_status = 0 ## 请假状态
        leave.save()
        return redirect("/leave_all_list/1/")
    return render_template("leave_list.html")


from sdk.pager import Pager
@app.route("/leave_all_list/<int:page>/",methods=["get","post"])
@LoginVaild
def leave_all_list(page):
    leave = Leave.query.filter(Leave.request_id == request.cookies.get("user_id")).all()
    pager = Pager(leave,10)
    page_data = pager.page_data(page)
    return render_template("leave_all_list.html",**locals())

from flask import jsonify
@app.route("/chexiao/",methods=["get","post"])
def chexiao():
    ## 获取请假条 leave_id
    id = request.form.get("id")
    # print (id)
    ## delete操作
    leave = Leave.query.filter(Leave.id == id).first()
    leave.delete()
    ##return "删除成功"
    result = {"code":10000,"msg":"删除成功"}
    return jsonify(result)    ## 返回json 串


from form import TaskForm
@app.route("/add_task/",methods=["get","post"])
def add_task():
    task = TaskForm()
    # print(dir(task))
    # print ("csrf_token%s" % task.csrf_token)   ### csrf_token
    # print ("errors %s" % task.errors)      ###错误
    # print (task.validate())      ###  判断是否是一个合法的请求
    # print (task.validate_on_submit())     ### 判断是否是一个有效post、请求
    # print (task.data)    ### 请求的数据
    #
    error = {}
    if request.method == "POST":
        if task.validate_on_submit():    ## 校验
            ## 获取数据数据
            FormData = task.data
            ## 保存数据   数据库当中 建立模型
        else:
            ##
            error = task.errors
    return render_template("add_task.html",**locals())


from main import api
from flask_restful import Resource

@api.resource("/Api/v1/leave/")
class LeaveApi(Resource):
    def __init__(self):
        super(LeaveApi, self).__init__()
        self.result = {
            "method": "get",
            "version": "v1",
            "data":""
        }
    def create_data(self,leave):
        """
            定义返回的数据
        :return:
        """
        result_data = {
            "request_id": leave.request_id,
            "request_name": leave.request_name,
            "request_type": leave.request_type,
            "request_start": str(leave.request_start),
            "request_end": str(leave.request_end),
            "request_description": leave.request_description,
            "request_phone": leave.request_phone,
            "request_status": leave.request_status
        }
        return result_data

    method_decorators = {
        "get":[LoginVaild]
    }
    def get(self):
        """
        处理get请求
        获取资源
        :return:
        """
        data = request.args
        id = data.get("id")
        result_data = {}
        if id:
            leave = Leave.query.get(int(id))
            if leave is not None:
                result_data = self.create_data(leave)
        else:
            leaves = Leave.query.all()  ### 所有数据
            result_data = []
            for leave in leaves:
                info = self.create_data(leave)
                result_data.append(info)

        self.result["data"] = result_data

        return jsonify(self.result)

        # return "get 请求 %s" % data
    def post(self):
        """
        处理post请求  增加数据的功能
        :return:
        """
        data = request.form
        leave = Leave()
        leave.request_id = data.get("request_id") ## 请假人id
        leave.request_name = data.get("request_name")  ## 请假人姓名
        leave.request_type = data.get("request_type")  ### 假期类型
        leave.request_start = data.get("request_start") ## 请假的开始时间
        leave.request_end = data.get("request_end")  ## 请假的结束时间
        leave.request_description = data.get("request_description")  ## 请假描述
        leave.request_phone = data.get("request_phone")  ###联系人手机号
        leave.request_status = data.get("request_status")  ## 请假状态
        leave.save()
        self.result["method"] = "post"
        self.result["data"] = self.create_data(leave)
        return jsonify(self.result)
    def put(self):
        """
        处理put请求 更新数据
        可以支持更改部分数据
        根据id查询的  -》  对象
        修改的是  对象中属性
        对象属性中  ——》  setattr

        :return:
        """
        data = request.form   ## 字典
        id = data.get("id")   ##假条id
        leave = Leave.query.get(id)  ## 找到被修改的数据   leave是一个对象
        for key,value in data.items():
            ## 传过来的 key  和 value
            if key != "id":
                if hasattr(leave,key):
                    setattr(leave,key,value)
        leave.merge()
        self.result["method"] = "put"
        self.result["data"] = self.create_data(leave)
        return jsonify(self.result)


    def delete(self):
        """
        处理delete方法   删除数据
        :return:
        """
        data = request.form
        id = data.get("id")
        leave = Leave.query.get(id)
        leave.delete()
        self.result["method"] = "delete"
        self.result["msg"] = "删除成功"
        return jsonify(self.result)



@app.route('/apidemo/')
def apidemo():
    return render_template("apidemo.html")



def func1(func):
    def inner():
        print ("func1 装饰器")
        func()
    return inner

def func2(func):
    def inner():
        print ("func2 装饰器")
        func()
    return inner


# @api.resource("/Demo/")
class Demo(Resource):
    method_decorators = {
        "get":[func1,func2],
        "post":[func2]
    }

    def get(self):
        """

        :return:
        """
        return "get请求"
    def post(self):
        """

        :return:
        """
        return "post 请求"

api.add_resource(Demo,"/Demo/")  ##


