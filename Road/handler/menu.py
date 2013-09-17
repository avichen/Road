# -*- coding: UTF-8 -*-
'''
Created on 2013年9月7日

@author: Chen
'''
from Base import BaseHandler
import tornado
from lib.logger import LOGGER

class MenuHandler(BaseHandler):
    @tornado.web.authenticated
    @tornado.web.asynchronous
    def get(self):
#         menu_list = self.db.query("select id,menu_code,memu_name_cn,menu_name_eng,menu_url,menu_parent,icon_flag from menus order by order_by")
        user_info = self.get_current_user()
        
        menu_list = self.db.query("select b.* from group_menu a left join menus b on a.menu_code=b.menu_code where a.group_code = '"+bytes(user_info['type'])+"' order by b.menu_code", )
#         LOGGER.info(user_info['type'])
        if not menu_list: raise tornado.web.HTTPError(404)
        self.db.close()
        self.write(tornado.escape.json_encode(menu_list))
        self.finish()