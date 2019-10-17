from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql
from flask_restful import Api
from flask_migrate import Migrate
from flask_wtf import CSRFProtect  ## 导入csrf保护

pymysql.install_as_MySQLdb()
app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))##当前文件  项目所在的根目录
app.config.from_pyfile("settings.py")  ## 使用python文件做配置文件
app.config.from_object("settings.TestConfig")
app.secret_key = "dsfdsfdsfdsfs"
db = SQLAlchemy(app)
api = Api(app)  ## 负责收集路由 收集类视图的注册信息
migrate = Migrate(app,db)  ###  安装数据库管理插件
csrf = CSRFProtect(app)  ## 使用csrf保护







