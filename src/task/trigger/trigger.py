# coding=utf-8

'''
触发器

@author: Huiyugeng
'''
import datetime
import time

class Trigger(object):

    def __init__(self, repeat_count=0, repeat_interval=1):
        self.repeat_count = repeat_count
        self.repeat_interval = repeat_interval
        
        self.start_delay = 0
        self.end_delay = 0
        
        self.start_date = None
        self.end_date = None
        
        self.execute_count = 0
    
    def set_delay(self, start_delay=0, end_delay=0):
        self.start_delay = start_delay
        self.end_delay = end_delay
    
    def set_date(self, start_date=None, end_date=None):
        if start_date != None and isinstance(start_date, datetime.datetime):
            self.start_date = time.mktime(start_date.timetuple())
        if end_date != None and isinstance(end_date, datetime.datetime):
            self.end_date = time.mktime(start_date.timetuple())
        
    def _get_repeat_interval(self):
        return self.repeat_interval
    
    def _get_start_delay(self):
        now = time.time()
        if self.start_delay == 0 and self.start_date != None:
            self.start_delay = self.start_date - now
        return self.start_delay
        
    def _inc_execute_count(self):
        self.execute_count = self.execute_count + 1
    
    def _is_finish(self):
        # 判断是否执行次数是否完成
        if self.repeat_count != 0 and self.repeat_count <= self.execute_count:
            return True
        
        # 判断是否到底结束时间
        now = time.time()
        if self.end_date != None and now >= self.end_date:
            return True
        
        return False
