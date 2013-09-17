# -*- coding: UTF-8 -*-
'''
Created on 2013年9月11日

@author: Chen
'''
from lib.logger import LOGGER
from Base import *
from Tix import Select

class StaffListHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        menu_code = self.get_argument("m")
        strSql = "select * from staff_info order by id desc"
        staff_list = self.db.query(strSql)
        if not staff_list:
            raise tornado.web.HTTPError(404)
            return None
        self.render("staff/stafflist.html", staff_list = staff_list, menu_code = menu_code)
        
class StaffAddHandler(BaseHandler):
    def get(self):
        menu_code = self.get_argument("m")
        strSql = "select * from user_info a left join staff_info b on a.id=b.user_id where b.user_id is null and a.type=1 order by a.id desc"
        user_list = self.db.query(strSql)
        self.db.close()
        if not user_list: 
            raise tornado.web.HTTPError(404)
            return None

        self.render("staff/staffadd.html", user_list = user_list, menu_code = menu_code)
        
    def post(self):
        menu_code = self.get_argument("m")
        user_code = self.get_argument("user_code")
        user_name = self.get_argument("user_name")
        age = self.get_argument("age")
        marriage = self.get_argument("marriage")
        edu = self.get_argument("edu")
        join_date = self.get_argument("join_date")
        position = self.get_argument("position")
        dept = self.get_argument("dept")
        begin_year = self.get_argument("begin_year")
        loc_address = self.get_argument("loc_address")
        home_town = self.get_argument("home_town")
        home_address = self.get_argument("home_address")
        status = self.get_argument("status")
        emc_person = self.get_argument("emc_person")
        emc_phone = self.get_argument("emc_phone")
        
        strSql = "insert into staff_info(user_id, name, age, marriage, educational, join_date, position, department, begin_work_year, local_address, home_town, home_address, status, emergency_person, emergency_phone) values('"+user_code+"', '"+user_name+"', '"+age+"', '"+marriage+"', '"+edu+"', '"+join_date+"', '"+position+"', '"+dept+"', '"+begin_year+"', '"+loc_address+"', '"+home_town+"', '"+home_address+"', '"+status+"', '"+emc_person+"', '"+emc_phone+"')"
        LOGGER.debug(strSql)
        last_rowid = self.db.execute_lastrowid(strSql)
        LOGGER.debug(last_rowid)
        self.redirect("/staff/list/?m="+menu_code)
        
class StaffViewHandler(BaseHandler):
    def get(self):
        menu_code = self.get_argument("m")
        self.render("staff/staffview.html", menu_code = menu_code)