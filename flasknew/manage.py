from app import Create
from flask_script import Manager
from flask_migrate import MigrateCommand
from settings import TestConfig
from gevent import monkey
monkey.patch_all()
app = Create(TestConfig)
manager = Manager(app)

@manager.command
def ruserver_gevent():
    """
    当前代码中所有io频繁的flask项目，可以提高flask的效率
    :return:
    """
    from gevent import pywsgi   ### pywsgi 是gevent自带的一个 web uwsgi 服务器
    server = pywsgi.WSGIServer(("127.0.0.1",5000),app)   ###封装一个服务
    server.serve_forever()  ## 启动服务




manager.add_command("db",MigrateCommand)
if __name__ == '__main__':
    import sys
    print (sys.path)
    manager.run()
    app.run()













