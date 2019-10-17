# Paginator(data,10)     将data数据进行分页，  每页10条
class Pager:
    """
    flask通过limit   offset 对数据进行分页

    切片
    提供的功能
    """
    #### params = User.query
    ###  data =  列表
    def __init__(self,data,page_size):
        """

        :param data:   数据
        :param page_size:     每页的条数
        """
        self.data = data   ### 数据
        self.page_size = page_size    ### 每页条数
        self.is_start = False
        self.is_end = False
        self.page_count = len(data)    ##  总条数
        self.previous_page = 0     ####上一页
        self.next_page = 0    ##### 下一页
        self.page_number = self.page_count / self.page_size  ### 总共的页数    len(data) / page_size
        if self.page_number == int(self.page_number):
            self.page_number = int(self.page_number)
        else:
            self.page_number = int(self.page_number) + 1
        self.page_range =( x for x in range(1,self.page_number + 1))  ## 迭代器   1 2 3 4 5 6 7 8 9 10

    def page_data(self,page):
        """
        page   offset   limit   每页10条
        1         0       10
        2        10       10
        切片      start     end
        1         0        10         (page-1)* 10
        2         10        20
        3         20        30
        :return:  返回分页的数据
        """
        # result = self.data.offset().limit().all()
        page_start = (page -1) * self.page_size### 切片开始的位置
        page_end = page * self.page_size    ## 切片结束的位置
        result = self.data[page_start:page_end]
        print (page)
        if page == 1:
            print ("--------------")
            self.is_start = True
        if page == self.page_number:
            self.is_end = True
        self.next_page = page + 1  ## 下一页
        self.previous_page = page - 1  ##上一页
        return result

from models import User,Leave

def add_data():
    for x in range(100):
        leave = Leave()
        leave.request_id = 1
        leave.request_name = "老王"
        leave.request_type = "事假"
        leave.request_start = "2019-07-01"
        leave.request_end = "2019-08-01"
        leave.request_description = "假期happy"
        leave.request_phone = "15201010101"
        leave.request_status = 0
        leave.save()


if __name__ == '__main__':
    while True:
        page = int(input(">>>>"))
        params = Leave.query.all()   ## 列表
        pager = Pager(params,10)
        result = pager.page_data(page)
        print (result)
        print(pager.page_size)     ### 每页的条数
        # print(pager.data)   ### 全部数据
        print(pager.page_number)   ### 最大页数
        print(list(pager.page_range))   ## 页数范围
        print(pager.page_count)   ## 数据总条数
        print(pager.is_end)       ### 是否是尾页
        print(pager.is_start)      ### 是否首页
        print(pager.next_page)     ### 下一页
        print(pager.previous_page)     ### 上一页



    # add_data()












