# -*- coding: UTF-8 -*-
'''
Created on 2013/9/25

@author: Chen
'''
from lib.logger import LOGGER
from Base import *

class MyVacationListHandler(BaseHandler):
    def get(self):
        menu_code = self.get_argument("m")
        user_info = self.get_current_user()
        id = str(user_info['id'])

        strSql = "select date_format(est_begin,'%%Y-%%m-%%d') est_begin, date_format(est_end,'%%Y-%%m-%%d') est_end, est_hours, est_days from vacation_master where employee_id = " + id
        my_vacation = self.db.query(strSql)

        self.render("vacation/myvacationlist.html", menu_code = menu_code, my_vacation = my_vacation)
        
class MyVacationAddHandler(BaseHandler):
    def get(self):
        menu_code = self.get_arguments("m")
        user_info = self.get_current_user()
        id = str(user_info['id'])
        
        self.render("vacation/myvacationadd.html", menu_code = menu_code)