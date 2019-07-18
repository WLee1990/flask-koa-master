#!/usr/bin/env python
# encoding: utf-8
import sys
from flask import Flask,Blueprint,render_template,request,url_for,redirect,abort,jsonify
from werkzeug import secure_filename
import json

errors=Blueprint('errors',__name__,template_folder='template')




@errors.errorhandler(404)
def page_not_found(e):
    #response=dict(status=0,message="404 NOT Found")
    #return jsonify(response),404
    return render_template('404.html'),404

@errors.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

