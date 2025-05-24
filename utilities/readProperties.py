import configparser
import os
#creating to read the config file
config = configparser.RawConfigParser() #this will create a configparser object
config.read(os.path.abspath(os.curdir) + "\\configurations\\config.ini") # this will read the config file from the configurations folder

class ReadConfig:
    @staticmethod # no need to create an instance of the class
    def getApplicationURL():
        url = config.get('commoninfo', 'baseURL') # this will get the baseURL from the config file, format is [section_name] [key_name]
        return url