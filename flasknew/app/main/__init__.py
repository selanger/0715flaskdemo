### 使用蓝图
from flask import Blueprint
from flask_restful import Api
main = Blueprint("main",__name__)
from .views import *


main_api = Api(main)
## 收集路由
main_api.add_resource(LeaveApi,"/Api/v1/leave/")
main_api.add_resource(Demo,"/Api/v1/demo/")




