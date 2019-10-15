from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))##当前文件  项目所在的根目录

# "sqlite:////tmp/test.db"   ###链接sqllit3 配置
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR,"test.db")  ##链接sqllit3 配置
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123123@localhost/flask"  ##链接mysql 配置
# app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True  ### 请求结束之后自动提交
# app.config["SQLALCHEMY_RTACK_MODIFICATIONS"] = True ## 跟踪修改  flask 1.x 之后增加的配置项
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True ## 跟踪修改  flask 1.x 之后增加的配置项
# app.config["DEBUG"] = True

app.config.from_pyfile("settings.py")  ## 使用python文件做配置文件
app.config.from_object("settings.TestConfig")
app.secret_key = "dsfdsfdsfdsfs"
# app.config.from_envvar()   ### 环境变量中加载
# app.config.from_json()   ##从json串中加载
# app.config.from_mapping()   ## mapping ---》 字典类型
db = SQLAlchemy(app)






