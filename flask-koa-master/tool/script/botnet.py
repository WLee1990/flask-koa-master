#!/usr/bin/python
#coding:utf-8
'''
Function:快速按序产生大量ip
'''

import os
import sys
import random
import string
class BotnetSignature(object):
    def __init__(self):
        super(BotnetSignature, self).__init__()
        self.signature_list=[]
    def Get_ip(self,number,start,file):
	self.number=number
	self.start=start
	self.file_name=file
        file = open(self.file_name, 'a')
        starts = self.start.split('.')
        A = int(starts[0])
        B = int(starts[1])
        C = int(starts[2])
        D = int(starts[3])
        i = 1
        for A in range(A, 1000):
            for B in range(B, 1000):
                for C in range(C, 1000):
                     for D in range(D, 1000):
                        ip = "%d.%d.%d.%d" % (A, B, C, D)
                        stringip = '01 '+str(i)+' '+ip
                        i= i+1
                        if self.number > 1:
                            file.write(stringip + '\n')
			    self.signature_list.append(stringip)
                            self.number -= 1
                        elif self.number == 1:  # 解决最后多一行回车问题
                            file.write(stringip)
                            self.number -= 1
			    self.signature_list.append(stringip)
                        else:
                            file.close()
                            return
                     D = 0
                C = 0
            B = 0
    def Get_domain(self,count,domain_file):
        txt_list=[]
	src_digits = string.digits              #string_数字
	src_uppercase = string.ascii_uppercase  #string_大写字母
	src_lowercase = string.ascii_lowercase  #string_小写字母
	filename = open(domain_file,'a+')
	for i in range(count):
	#随机生成数字、大写字母、小写字母的组成个数（可根据实际需要进行更改）
	    TXTlength = 26
	    TXT_end = random.choice(('.com', '.org', '.cn', '.uk','.top','.cc','.net','.biz','.eu','.jp'))
	    digits_num = random.randint(1,9)
	    uppercase_num = random.randint(1,TXTlength-digits_num-1)
	    lowercase_num = TXTlength - (digits_num + uppercase_num)
	    #生成字符串
	    TXT = random.sample(src_digits,digits_num) + random.sample(src_uppercase,uppercase_num) + random.sample(src_lowercase,lowercase_num)
	    #打乱字符串
	    random.shuffle(TXT)
            #列表转字符串
	    i=i+1
            txt_string = '01 '+str(i)+' '+''.join(TXT)+TXT_end
            txt_list.append(txt_string)
	    filename.write(txt_string+'\n')
	filename.close()
        self.signature_list=txt_list
    def Printtxt(self):
        return self.signature_list

'''
if __name__ == "__main__":
    usemessage = """
    ****************************************************
    规格列表
    ****************************************************
    """
    print (usemessage)
    Botnet=BotnetSignature()
    Botnet.Get_domain(10,'domain_list.txt')
    Botnet.Get_ip(10,'2.2.2.2','ip_list.txt')
    Botnet.Printtxt()
'''
