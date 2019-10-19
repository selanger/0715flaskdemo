from flask import Flask,Blueprint
# app = Flask(__name__)
### 1. 实例化一个蓝图对象    
##  参数： 第一个蓝图的名字
##         第二个：蓝图的路径
bp = Blueprint("goods",__name__)

# @app.route("/index/")
# def index():
#     return "index"
@bp.route("/index/")    ## 2. 由蓝图定义的路由和视图
def index():
    return "index"
if __name__ == '__main__':
    app = Flask(__name__)
    app.config["DEBUG"] = True
    ## 3. 注册蓝图
    app.register_blueprint(bp,url_prefix="/goods")
    app.run()