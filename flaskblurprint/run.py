from flask import Flask
from goodsviews import g_views
from userviews import u_views

class Config:
    SECRET_KEY = "helloworld"


if __name__ == '__main__':
    app  = Flask(__name__)
    ### app中增加一个配制
    app.config.from_object(Config)
    ## 注册蓝图

    app.register_blueprint(g_views,url_prefix = "/goods")
    app.register_blueprint(u_views,url_prefix="/user")
    print (app.config)

    app.run(debug=True)