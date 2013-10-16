# -*- coding: UTF-8 -*-
'''
Created on 2013/9/16

@author: Chen
'''
from lib.logger import LOGGER
from Base import *
import time
from json import _default_encoder

class MessageUserUnreadHandler(BaseHandler):
    def get(self):
        user_info = self.get_current_user()
        id = str(user_info['id'])
        strSql = "select id, send_id, rcv_id, message_title, message_txt, type, date_format(post_time, '%%Y %%m %%d %%H:%%i:%%s') post_time, status from message_info where rcv_id = "+id+" and TO_DAYS(now()) - TO_DAYS(post_time) <= 30 and status = 0"
        message_info = self.db.query(strSql)
        LOGGER.debug(message_info)
        if message_info:
            self.write(tornado.escape.json_encode(message_info))
        return None
    
class MessageUserUnreadCountHandler(BaseHandler):
    def get(self):
        user_info = self.get_current_user()
        id = str(user_info['id'])
        strSql = "select count(*) count from message_info where rcv_id = "+id+" and TO_DAYS(now()) - TO_DAYS(post_time) <= 30 and status = 0"
        count = self.db.query(strSql)

#         LOGGER.debug(count)
        if not count:
            self.write(tornado.escape.json_encode(count))
        return None

class MessageListHandler(BaseHandler):
    def get(self):
        menu_code = self.get_argument("m")
        user_info = self.get_current_user()
        strSql = "select * from message_info where rcv_id = %s" % str(user_info["id"])
        message_list = self.db.query(strSql)

        self.render("message/messagelist.html", message_list = message_list, menu_code = menu_code)
        
        