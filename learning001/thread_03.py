import threading
import time

max_goods_num = 10
min_goods_num = 5
con = threading.Condition()
num = 0


class Producer(threading.Thread):

    def __init__(self, con):
        self.con = con
        super().__init__()

    def run(self):
        global num
        self.con.acquire()
        print('*' * 50)
        print('Coming in Producer\n', time.ctime())
        for _ in range(max_goods_num):
            print('开始循环生产')
            num = num + 1
            print('开始生成产品{}个'.format(num))
            time.sleep(2)
            if num == min_goods_num:
                print('已经生成5个，停止')
                self.con.notify()
                self.con.wait()
        self.con.release()
        print('Producer scripts exit')


class Customer(threading.Thread):

    def __init__(self, con):
        self.con = con
        super().__init__()

    def run(self):
        global num
        self.con.acquire()
        print('*' * 50)
        print('Coming in Customer\n', time.ctime())
        while num:
            print('开始循环消费')
            num = num - 1
            print('现在产品还有{}个'.format(num))
            time.sleep(2)
            if num < min_goods_num:
                print('产品已经小于5个，等待补货')
                self.con.notify()
                self.con.wait(3)
        self.con.release()
        print('Customer scripts exit')


if __name__ == '__main__':
    p = Producer(con).start()
    c = Customer(con).start()



