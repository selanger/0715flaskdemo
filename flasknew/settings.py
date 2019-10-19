import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_PATH = os.path.join(BASE_DIR,"static")

class Product:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  ### 请求结束之后自动提交
    SQLALCHEMY_RTACK_MODIFICATIONS = True  ## 跟踪修改  flask 1.x 之后增加的配置项
    SQLALCHEMY_TRACK_MODIFICATIONS = True  ## 跟踪修改  flask 1.x 之后增加的配置项

class Config(Product):
    ## 正式环境的 配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:123123@localhost/flask"  ##链接mysql 配置
    SECRET_KEY = "fdshfkjdsjfheofhihfkfjl"

class TestConfig(Product):
    ## 测试环境的配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:123123@localhost/flask"  ##链接mysql 配置
    DEBUG = True
    SECRET_KEY = "fdshfkjdsjfheofhihfkfjl"






