from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_restful import Api
from flask_migrate import Migrate
from flask_wtf import CSRFProtect  ## 导入csrf保护
pymysql.install_as_MySQLdb()

csrf = CSRFProtect()
db = SQLAlchemy()
api = Api()
migrate =Migrate()


def Create(config):
    """
    生成flask 配置文件
    """
    app = Flask(__name__)
    ##
    import sys
    # print(sys.path)
    import os
    app.config.from_pyfile(os.path.join(sys.path[0],"settings.py"))  ## 从配置文件中加载配置
    app.config.from_object(config)  # 从类中加载配置
    db.init_app(app)   ### db = Sqlalchemy(app)
    migrate.init_app(app,db)
    api.init_app(app)
    csrf.init_app(app)
    from app.main import main
    app.register_blueprint(main)
    return app







