def f_outer(func):
    def inner(*args,**kwargs):
        return "i" + func(*args,**kwargs)
    return inner

def s_outer(func):
    def inner(*args,**kwargs):
        return "am" + func(*args,**kwargs)
    return inner


@f_outer
@s_outer
def test():
    return "gutianle"
print (test())

