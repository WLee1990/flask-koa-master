#!/usr/bin/env python
# encoding: utf-8
import sys
from flask import Flask,Blueprint,render_template,request,url_for,redirect,abort,jsonify
from werkzeug import secure_filename
import json

ad=Blueprint('ad',__name__,template_folder='template')

'''
@ad.route('/test',methods=['GET','POST'])
def Test():
    if request.method=='GET':
        return render_template('test.html')
    else:
        #recv_data=request.get_data()
        recv_data=json.loads(request.get_data(as_text=True))
        print (recv_data)
        testOption=recv_data['test_type']
        print testOption
        test1=TEST()
        dataRes=test1.testDescription(testOption)
        result={'result':'success','data':dataRes}
        return json.dumps(result)
        #return json.dumps(testOption)

'''

#!/usr/bin/env python
# encoding: utf-8
import sys
from flask import Flask,Blueprint,render_template,request,url_for,redirect,abort,jsonify
from werkzeug import secure_filename
import json
from tool.script.attack_defense import AttackDefense
from scapy.all import *
ad=Blueprint('ad',__name__,template_folder='template')


@ad.route('/ping_of_death',methods=['GET','POST'])
def ping_of_death():
    if request.method =='GET':
        return render_template('ping_of_death.html')
    else:
	dst_ip = request.form['dst_ip']
        pfd = AttackDefense()
        ip_check = pfd.ip_check(dst_ip)
        if ip_check == 0:
            return render_template('ping_of_death.html', result="Bad dst_ip", ip=dst_ip)
        else:
            send_pkt = pfd.ping_of_death(dst_ip)	
            return render_template('ping_of_death.html', result=send_pkt, ip=dst_ip)

@ad.route('/land_dos',methods=['GET','POST'])
def land_dos():
    if request.method=='GET':
        return render_template('land_dos.html')
    else:
        dst_ip = request.form['dst_ip']
        land = AttackDefense()
        ip_check = land.ip_check(dst_ip)
        if ip_check == 0:
            return render_template('ping_of_death.html', result="Bad dst_ip", ip=dst_ip)
        else:
            send_pkt = land.land_dos(dst_ip)
            #pkt = IP(src=dst_ip,dst=dst_ip)/TCP(sport=135,dport=135)
            #sr1(pkt,iface="eth1",timeout=1)
            return render_template('land_dos.html', result=send_pkt, ip=dst_ip, )	

@ad.route('/port_scan',methods=['GET','POST'])
def port_scan():
    if request.method=='GET':
        return render_template('port_scan.html')
    else:
        dst_ip = request.form['dst_ip']
        start_port = request.form['start_port']
        end_port = request.form['end_port']
        portscan = AttackDefense()
        ip_check = portscan.ip_check(dst_ip)
        port_check = portscan.port_check(start_port,end_port)
        if ip_check == 0:
            return render_template('port_scan.html', result="Bad dst_ip", dst_ip=dst_ip)
        elif port_check == 0:
            return render_template('port_scan.html', result="Bad Port", dst_ip=dst_ip)
        else:
            send_pkt = portscan.port_scan(dst_ip, start_port, end_port)
            # pkt = IP(src=dst_ip,dst=dst_ip)/TCP(sport=135,dport=135)
            # sr1(pkt,iface="eth1",timeout=1)
            return render_template('port_scan.html', result=send_pkt)

