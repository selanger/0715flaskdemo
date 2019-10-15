from main import db
import datetime
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
    email = db.Column(db.String(32))
    password = db.Column(db.TEXT)
    age = db.Column(db.Integer)
    sex = db.Column(db.Integer)
    identity = db.Column(db.String(32))
    subject = db.Column(db.String(32))
    level= db.Column(db.String(64))
    photo = db.Column(db.String(64))


class Leave(BaseModel):
    __tablename__ = "leave"
    #   审核中   0
    #   通过    1
    #   驳回     2
    #   销假     3
    request_id = db.Column(db.Integer)  ## 请假人id
    request_name = db.Column(db.String(32))  ## 请假人姓名
    request_type = db.Column(db.String(32))    ### 假期类型
    request_start = db.Column(db.DATE)    ## 请假的开始时间
    request_end = db.Column(db.DATE)     ## 请假的结束时间
    request_description = db.Column(db.TEXT)   ## 请假描述
    request_phone = db.Column(db.String(11))    ###联系人手机号
    request_status = db.Column(db.Integer)    ## 请假状态







