#!/usr/bin/env python
# encoding: utf-8
import sys,os
from flask import Flask,Blueprint,render_template,request,url_for,redirect,abort,jsonify
from werkzeug import secure_filename
import json
sys.path.append('../')
from tool.script.botnet  import BotnetSignature

more=Blueprint('more',__name__,template_folder='templates')



@more.route('/signature',methods=['GET','POST'])
def BotnetSig():
    if request.method =='GET':
        return render_template('signature.html')
    else:
	recv_data=json.loads(request.get_data(as_text=True))
	sigType = recv_data['botnet_type']
	sigNum =int(recv_data['number'])
	botSig=BotnetSignature()
        if (sigType == 'IP'):
	    botSig.Get_ip(sigNum,'1.1.1.1','ip_list')
	else:
	    print 'get domain'
	    botSig.Get_domain(sigNum,'domain_list')
	dataRes=botSig.Printtxt()
	result={'result':'success','msg':'Get Signature success!','data':dataRes}
	#return dataRes
	return json.dumps(result)

@more.route('/md5',methods=['GET','POST'])
def ChangeFilenameToMd5():
    if request.method =='POST':
        f=request.files['file']
  	f.save(secure_filename(f.filename))
	return ('upload successfully')
    
    else:
        return render_template('md5.html')

