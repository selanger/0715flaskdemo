## 项目的管理文件
##  python manage.py runserver
## python manage.py migrate
import sys
from main import app,db
from views import *
from models import *
from flask_script import Manager
manager = Manager(app)
from flask_migrate import MigrateCommand

### migrate  python manage.py migrtate
# @manager.command
# def migrate():
#     db.create_all()
manager.add_command("db",MigrateCommand)
if __name__ == '__main__':
    manager.run()     ### runserver 方法







# command = sys.argv[1]
# ### 从终端获取输入的参数
# if command == "runserver":     ### python manage.py runserver
#     app.run()
# elif command == "migrate":     ## python manage.py migrate
#     db.create_all()
# ##  python manage.py runserver 0.0.0.0:8000








