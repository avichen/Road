# -*- coding: UTF-8 -*-
'''
Created on 2013/09/04

@author: Chen
'''

from lib.logger import LOGGER
import lib.message
from Base import *


class UserListHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        menu_code = self.get_argument("m")
        user_list = self.db.query("select * from user_info order by id desc")
        self.db.close()
#         LOGGER.debug(user_list)
        self.render("user/userlist.html", user_list = user_list, menu_code = menu_code)
        
class UserAddHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        menu_code = self.get_argument("m")
        self.render("user/useradd.html", menu_code=menu_code)
        
    @tornado.web.authenticated
    def post(self):
        menu_code = self.get_argument("m")
        user_code = self.get_argument("user_code")
        password = self.get_argument("password")
        gender = self.get_argument("gender")
        email = self.get_argument("email")
        phone = self.get_argument("phone")
        type = self.get_argument("type")
        status = self.get_argument("status")
        db = self.db
        strSql = "insert into user_info(user_code, pass_word, gender, email, phone, type, status) values('"+user_code+"', md5('"+password+"'), '"+gender+"', '"+email+"', '"+phone+"', "+type+", "+status+")"
#         LOGGER.debug(strSql)
        last_rowid = db.execute_lastrowid(strSql)
        status = lib.message.create(db = db, send_id = 0, rcv_id = last_rowid, message_title = u'请填写您的个人信息', message_txt = u'请填写您的个人信息!!!', type = 1, status = 0)
        if status == "KO":
            raise tornado.web.HTTPError(404)
            return None
        
#         LOGGER.debug(last_rowid)
        self.redirect("/user/list/?m="+menu_code)

        
class UserDelHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, id):
        menu_code = self.get_argument("m")
        strSql = "delete from user_info where id = %s" % id
        LOGGER.debug(strSql)
        last_rowid = self.db.execute_lastrowid(strSql)
        self.redirect("/user/list/?m="+menu_code)
        
        
# class CleanHandler(BaseHandler):
#     
#     def get(self):
#         self.clear_cookie("userinfo")
#         user_list = self.db.query("select * from user_info order by id desc")
#         self.db.close()
# #         LOGGER.info(user_list)
#         self.render("user/userlist.html", user_list = user_list)
        
# class JsonHandler(BaseHandler):
#     
#     def post(self):
#         #特别要注意，因为是响应的ajax的请求，返回数据类型需指定为json
#         self.set_header("Content-Type", "application/json")
#         LOGGER.info("---------------JsonHandler--------------------")
#         user_list = self.db.query("select * from user_info order by id desc")
#         self.db.close()
#         self.write(tornado.escape.json_encode(user_list))