# coding=utf-8
'''
Created on 2012-11-27

@author: Eric
'''



import tornado.web
from lib.logger import LOGGER

class BaseHandler(tornado.web.RequestHandler):
    
#     def write_error(self, status_code, **kwargs):
#         if status_code == 404:
#             self.render('templates/404.html')
#         elif status_code == 500:
#             self.render('templates/500.html')
#         else:
#             super(tornado.web.RequestHandler, self).write_error(status_code, **kwargs)
            
    @property
    def db(self):
        return self.application.db
    
    def get_current_user(self):
        user_code = self.get_cookie("userinfo")
#         LOGGER.debug("---------base get_current_user-----------")
        if not user_code: return None
        else: 
            userinfo = self.db.get("SELECT * FROM user_info WHERE user_code = %s", user_code)
#             LOGGER.debug("---------get_current_user-----------")
            self.db.close()
            return userinfo
      
    @property
    def check_menu(self,m):
        strSql = "select * from group_menu a left join user_info b on a.group_code = b.type where b.user_code='admin' and menu_code='"+m+"'"
        
        LOGGER.info("----------check_menu----------"+strSql)
        menus = self.db.get(strSql)
        self.db.close()
        if not menus:
            self.render("login.html", message="无权限访问")
            return None
        
        return "OK"
        