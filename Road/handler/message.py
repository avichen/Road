# -*- coding: UTF-8 -*-
'''
Created on 2013/9/16

@author: Chen
'''
from lib.logger import LOGGER
from Base import *
import time
from json import _default_encoder

class messageUserUnreadHandler(BaseHandler):
    def get(self):
        user_info = self.get_current_user()
        id = 41
        strSql = "select id, send_id, rcv_id, message_title, message_txt, type, date_format(post_time, '%%Y %%m %%d %%H:%%i:%%s') post_time, status from message_info where rcv_id = "+bytes(id)+" and TO_DAYS(now()) - TO_DAYS(post_time) <= 30 and status = 0"
        message_info = self.db.query(strSql)
        LOGGER.debug(message_info)
        if message_info:
            self.write(tornado.escape.json_encode(message_info))
        return None
    
class messageUserUnreadCountHandler(BaseHandler):
    def get(self):
        user_info = self.get_current_user()
        id = 41
        strSql = "select count(*) count from message_info where rcv_id = "+bytes(id)+" and TO_DAYS(now()) - TO_DAYS(post_time) <= 30 and status = 0"
        count = self.db.query(strSql)
        LOGGER.debug(count)
        if count:
            self.write(tornado.escape.json_encode(count))
        return None


        
        