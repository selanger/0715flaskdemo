

class Demo:
    name = "张三"
    age = 19
d = Demo
print(d.name)
print(d.age)
setattr(d,"name","laoli")
setattr(d,"age",20)
print(d.name)
print(d.age)
setattr(d,"sex","nan")
print (d.sex)
a = getattr(d,"name")
print (a)
flag = hasattr(d,"namenew")  ##判断是否包含某一个属性
print (flag)

##  类中的变量
        #  类属性
        #  局部变量
        #  成员变量
## 类中的方法
        ##  静态方法
            ###  没有明确的逻辑关系
            ###  类对象和实例对象调用
            ### 访问变量： 不能使用任何实例和对象的方法和属性
         ##  类方法
            ## 接收cls  类 当前类对象
            ## 类对象和实例对象调用
            ### 访问变量： 类的属性和方法
        ##  方法
            ## 可被实例对象对象
            ### 访问变量：  可以使用属性和方法





