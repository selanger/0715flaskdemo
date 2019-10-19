from greenlet import greenlet
import time
def work1():
    while True:
        print ("work1")
        w2.switch()
        time.sleep(1)
def work2():
    while True:
        print ("work2")
        w1.switch()
        time.sleep(10)

if __name__ == '__main__':
    w1 = greenlet(work1)   ### 创建了一个greenlet 对象
    w2 = greenlet(work2)  ### 创建了一个greenlet 对象
    w1.switch()





