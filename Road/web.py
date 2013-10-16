# -*- coding: UTF-8 -*-
'''
Created on 2013/09/04

@author: Chen
'''


import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from lib.logger import LOGGER
import torndb
from handler import index, user, menu, staff, message, vacation


define("port", default=8888, help="run on the given port", type=int)
# define("mysql_host", default="11.11.11.15:3306", help="database host")
define("mysql_host", default="192.168.169.4:3306", help="database host")
define("mysql_database", default="Catch", help="database name")
define("mysql_user", default="root", help="database user")
define("mysql_password", default="jiangyin", help="database password")

class Application(tornado.web.Application):
    def __init__(self):
        
        handlers = [(r"/", index.LoginHandler),
                    (r"/index/", index.MainHandler),
                    (r"/menu/all", menu.MenuHandler),
                    (r"/message/unread/title", message.MessageUserUnreadHandler),
                    (r"/message/unread/count", message.MessageUserUnreadCountHandler),
                    (r"/message/list/", message.MessageListHandler),
                    (r"/user/list/", user.UserListHandler),
                    (r"/user/add/", user.UserAddHandler),
                    (r"/user/del/([0-9]+)/", user.UserDelHandler),
                    (r"/staff/list/", staff.StaffListHandler),
                    (r"/staff/add/", staff.StaffAddHandler),
                    (r"/vocation/mylist/", vocation.MyVacationListHandler)
                    
                ]

        settings = dict(
            site_name=u"路赛",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "common"),
            autoescape=None,
            login_url = '/',
            debug=True
        )
        tornado.web.Application.__init__(self, handlers, **settings)
#        self.db = mysqlconnector.Connection(
#                host=options.mysql_host,
#                database = options.mysql_database,
#                user = options.mysql_user,
#                password = options.mysql_password)
# 
        self.db = torndb.Connection(options.mysql_host, 
                                    options.mysql_database, 
                                    options.mysql_user, 
                                    options.mysql_password
                )

        

def main():
    LOGGER.info("Start....")
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':

    main()