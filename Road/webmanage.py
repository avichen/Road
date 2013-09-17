# coding=utf-8
'''
Created on 2012-11-27

@author: Eric
'''



import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db