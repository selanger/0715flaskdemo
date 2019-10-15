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
@app.route("/leave_list/",methods=["get","post"])
@LoginVaild
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
        return redirect("/leave_all_list/")
    return render_template("leave_list.html")

@app.route("/leave_all_list/",methods=["get","post"])
@LoginVaild
def leave_all_list():
    leave = Leave.query.filter(Leave.request_id == request.cookies.get("user_id")).all()
    return render_template("leave_all_list.html",**locals())


