def flask_url(func):
    print ("我是flask url装饰器")
    def inner(*args,**kwargs):
        print("url")
        func(*args,**kwargs)
    return inner
def loginouter(func):
    print("我是登录验证装饰器")
    def inner(*args,**kwargs):
        print("验证")
        func()
    return inner
@flask_url
@loginouter ###index = loginouter(index)
def index():
    print("index")
index()








