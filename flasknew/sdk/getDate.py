import calendar
import datetime
class MyDate(object):
    def __init__(self):
        now_time= datetime.datetime.now()   ## 当前时间
        year = now_time.year   ### 当前年
        month = now_time.month    ## 当前月
        self.result = []   ## 返回结果
        ## 当月总天数  最后一天
        total_day = calendar.monthrange(year, month)[1]
        ## 第一天
        first_day = datetime.date(year,month,1)
        ## 获取第一天是周几
        first_week = first_day.weekday()  ## 从0开始到6    0 代表周一  6 代表周日   1
        last_week = datetime.date(year,month,total_day).weekday()   ## 当月最后一天星期几

        all_day = [x for x in range(1,total_day+1)]   ### 当月总共的天数列表

        ## 前面补充empty
        lines = []
        for i in range(first_week):
            lines.append("empty")
        for j in range(7-first_week):
            lines.append(all_day.pop(0))
        self.result.append(lines)   ##### 结果列表中增加了第一行的数据

        while all_day:
            line = []  ### 临时列表，存储每一行的数据
            for i in range(7):
                if len(line)< 7 and all_day:
                    line.append(all_day.pop(0))
                else:
                    line.append("empty")   ## 最后一行 数字没有数字的时候 添加empty
            self.result.append(line)   ### 最终的结果列表
    def get_date(self):
        ## 返回结果
        return self.result
    def print_date(self):
        ## 将结果打印出来
        print (self.result)














