# -*- coding: UTF-8 -*-
'''
Created on 2013/9/5

@author: Chen
'''
import os
import logging
import logging.handlers

LOG_FILE_PATH = "log/out.log"

dir = os.path.dirname(LOG_FILE_PATH)

if not os.path.isdir(dir):
    os.mkdir(dir)

FILE_LOG_LEVEL="DEBUG"
CONSOLE_LOG_LEVEL="INFO"


class logger(object):

    def __init__(self,logFile,file_level,console_level):
        
        self.config(logFile,file_level,console_level)
        
    def config(self,logFile,file_level,console_level):
        self.logger = logging.getLogger("crawler")
        self.logger.setLevel(file_level)
        
        formatter = logging.Formatter("%(asctime)s *%(levelname)s* : %(message)s",'%Y-%m-%d %H:%M:%S') 
        
        self.fh = logging.handlers.RotatingFileHandler(logFile,mode='a', maxBytes=1024*1024*10, backupCount=100, encoding="utf-8")
        self.fh.setLevel(file_level)
        self.fh.setFormatter(formatter)
        
        self.ch = logging.StreamHandler()
        self.ch.setLevel(console_level)
        self.ch.setFormatter(formatter)
        
        #把所有的handler添加到root logger中  
        self.logger.addHandler(self.ch)    
        self.logger.addHandler(self.fh)
        
    def debug(self,msg):  
        if msg is not None:  
            self.logger.debug(msg)  
    def info(self,msg):  
        if msg is not None:  
            self.logger.info(msg)  
    def warning(self,msg):  
        if msg is not None:  
            self.logger.warning(msg)  
    def error(self,msg):  
        if msg is not None:  
            self.logger.error(msg)  
    def critical(self,msg):  
        if msg is not None:  
            self.logger.critical(msg)
            
            

LOGGER = logger(LOG_FILE_PATH, FILE_LOG_LEVEL, CONSOLE_LOG_LEVEL)