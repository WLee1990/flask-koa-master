#! /usr/bin/env python

import os
from flask_script import Manager
#from app import creat_app
from  tool.main import app

#app=creat_app(os.getenv('FLASK_CONFIG') or 'default')
#manager=Manager(app)

if __name__=='__main__':
    app.run(debug = True,threaded = True ,host= '0.0.0.0',port = 5000)
