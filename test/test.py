def test(**kwargs):
    print (kwargs)


def newfunc(*args,**kwargs):
    # print(kwargs)
    test(kwargs)

if __name__ == '__main__':
    newfunc(name="zhangsan",age=19)






