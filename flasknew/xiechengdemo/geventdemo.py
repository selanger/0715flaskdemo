import gevent
from gevent import monkey
monkey.patch_all()   ## 识别耗时操作，并转化
import time
def work1():
    for i in range(10):
        print ("work1 %d" %i)
        time.sleep(1)    ### 模拟耗时操作
        ###   IO密集型   耗时操作
        # gevent.sleep(1)

def work2():
    for i in range (10):
        print ("work2 %d " %i)
        time.sleep(1)
        # gevent.sleep(1)


# w1 = gevent.spawn(work1)   ##  创建一个 gevent对象  （参数：要执行的方法）
# w2 = gevent.spawn(work2)
#
# w1.join()  ## 等待  w1  执行结束
# w2.join()  ## 等待  w2 执行结束
gevent.joinall([
gevent.spawn(work1),
gevent.spawn(work2)
])













