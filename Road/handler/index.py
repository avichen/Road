# -*- coding: UTF-8 -*-
'''
Created on 2013/09/04

@author: Chen
'''
from lib.logger import LOGGER
from Base import *
import hashlib

class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html", message="")
        
    def post(self):
#         msg = {msg="", next=""}
        user_code = self.get_argument("user_code")
        pass_word = self.get_argument("pass_word")
        m_password = hashlib.md5(pass_word)
        strSql = "select * from user_info where user_code='"+user_code+"' and pass_word=md5('"+pass_word+"')"
        user_info = self.db.get(strSql)
        self.db.close()
        if not user_info:
            message = "用户名或密码错误"
            self.render("login.html", message=message)

        else:
            self.clear_cookie("userinfo")
            self.set_cookie("userinfo", user_info['user_code'])
            self.redirect("/index/?m=000", user_info)

class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        menu_code = self.get_argument("m")
        if not self.get_current_user():
            message = "请重新登录"
            self.render("login.html", message=message)
        else:
#             menu_code = '000'
            self.render('main.html', menu_code = menu_code)
#             
#     def post(self):
#         user_code = self.get_argument("user_code")
#         pass_word = self.get_argument("pass_word")
#         LOGGER.info(user_code)
#         LOGGER.info(pass_word)
#         user_info = self.db.get("select * from user_info where user_code='"+user_code+"' and pass_word='"+pass_word+"'")
# #         LOGGER.info(user_info)
#         self.db.close()
#         if not user_info:
#             self.render("login.html")
#         else:
#             self.clear_cookie("userinfo")
#             self.set_cookie("userinfo", user_info['user_code'])
#             self.render("main.html", user_info=user_info)
        