# -*- coding: UTF-8 -*-
'''
Created on 2013/9/16

@author: Chen
'''
from lib.logger import LOGGER
import time

# class MessageCreateHandler(BaseHandler):
#     def post(self, send_id, message_title, message_text, type, status):
#         current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#         strSql = "insert into message_text (send_id, message_title, message_text, type, post_time, status) values('"+send_id+"', '"+message_title+"', '"+message_text+"', '"+type+"', '"+current_time+"', '"+status+"')"
#         last_rowid = self.db.execute_lastrowid(strSql)
#         if not last_rowid:
#             raise tornado.web.HTTPError(404)
#             return None
#         LOGGER.debug(last_rowid)
#         self.re
        
        
#         strSql = "insert into message_log (rcv_id, message_id, status, log_time) values()"




def create(db, send_id, rcv_id, message_title, message_txt, type, status):
    current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    LOGGER.debug("------------------"+str(current_time))
    strSql = "insert into message_info (send_id, rcv_id, message_title, message_txt, type, post_time, status) values(%s, %s, '%s', '%s', %s, '%s', %s)" % (send_id,rcv_id,message_title,message_txt,type,current_time,status)
    LOGGER.debug(strSql)
    last_rowid = db.execute_lastrowid(strSql)
    if not last_rowid:
        return "KO"
    LOGGER.debug(last_rowid)
    return "OK"
        
        