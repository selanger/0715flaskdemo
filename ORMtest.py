from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

## 学习sqlalchemy
## 链接数据库
BASE_DIR = os.path.abspath(os.path.dirname(__file__))##当前文件  项目所在的根目录
print (BASE_DIR)
# "sqlite:////tmp/test.db"   ###链接sqllit3 配置
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR,"test.db")  ##链接sqllit3 配置
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123123@localhost/flask"  ##链接mysql 配置
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True  ### 请求结束之后自动提交
app.config["SQLALCHEMY_RTACK_MODIFICATIONS"] = True ## 跟踪修改  flask 1.x 之后增加的配置项
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True ## 跟踪修改  flask 1.x 之后增加的配置项
app.config["DEBUG"] = True

db = SQLAlchemy(app)    ### 绑定 flask项目
# from datetime import datetime
import datetime
## 创建模型

class BaseModel(db.Model):
    ##
    __abstract__ = True    ###  声明当前类为抽象类，被继承 调用不会被创建
    id = db.Column(db.Integer,primary_key=True)
    def save(self):
        db.session.add(self)
        db.session.commit()
    def merge(self):
        db.session.merge(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()



class UserInfo(BaseModel):
    __tablename__ = 'userinfo'     ## 表名
    # id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32))
    age = db.Column(db.Integer)
    time = db.Column(db.DATETIME,default=datetime.datetime.now())  ## auto_now = True
class User(BaseModel):
    __tablename__ = "user"
    name = db.Column(db.String(32))
    phone = db.Column(db.String(11))


userinfo = UserInfo(name="awu",age=19)
#  增加数据
userinfo.save()


### 更新数据
# userinfo = UserInfo.query.get(8)
# userinfo.name="aliu"
# userinfo.merge()

## 删除数据
# userinfo = UserInfo.query.get(8)
# userinfo.delete()







## 数据迁移
db.create_all()  ## 同步表结构

## 增加数据
#当条增加   add
# userinfo = UserInfo(name='laowang',age=19)
# db.session.add(userinfo)
# db.session.commit()
# 多条增加  add_all
# db.session.add_all([
#     UserInfo(name='laowang',age=19),
#     UserInfo(name='laowang',age=19),
#     UserInfo(name='laowang',age=19),
#     UserInfo(name='laowang',age=19),
#     UserInfo(name='laowang',age=19)
# ])
# db.session.commit()
# userinfo1 = UserInfo(name='laowang',age=19)
# userinfo2 = UserInfo(name='laowang',age=19)
# userinfo3 = UserInfo(name='laowang',age=19)
# userinfo4 = UserInfo(name='laowang',age=19)
# db.session.add_all([userinfo1,userinfo2,userinfo3,userinfo4])
# db.session.commit()
## 查询
## all
# data = UserInfo.query.all()
# print (data)
# for one in data:
#     print (one.name)
# get
# data = UserInfo.query.get(ident=16)
# print (data)
# print (data.name)

## filter
# data = UserInfo.query.filter_by(name="laowang").all()
# print (data)
# data = UserInfo.query.filter(UserInfo.name == "laowang").all()
# print (data)
## first
# data = UserInfo.query.filter(UserInfo.name == "lisi").first()
# print (data)
##

## order_by 排 序
# 升序
# data = UserInfo.query.order_by(UserInfo.id).all()
# print (data)
# data =UserInfo.query.order_by("id").all()
# print (data)
# 降序
# data = UserInfo.query.order_by(UserInfo.id.desc()).all()
# print (data)
# data =UserInfo.query.order_by(db.desc("id")).all()
# print (data)


## 分页
## sql  select * from userinfo limit 2,3;  2代表从哪里开始   3 取多少条
# data = UserInfo.query.offset(2).limit(2).all()
# ## limit(2)  取2条数据
# ## offset(2) 偏移2
# print (data)

## 修改
# data = UserInfo.query.filter(UserInfo.id==1).first()
# data.name = "lisi"
# db.session.merge(data)
# db.session.commit()
## 删除
#delete
# data = UserInfo.query.filter().first()
# print(data.id)
# db.session.delete(data)
# db.session.commit()

# data = UserInfo.query.filter(UserInfo.id == 2).delete()
# db.session.commit()
















@app.route("/")
def index():
    return "ORM测试"

if __name__ == '__main__':
    app.run()

