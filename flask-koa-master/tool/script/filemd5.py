#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import hashlib
import os
import sys
 
def get_md5(file_path):
    f = open(file_path,'rb')  
    md5_obj = hashlib.md5()
    while True:
        d = f.read(8096)
        if not d:
          break
        md5_obj.update(d)
    hash_code = md5_obj.hexdigest()
    f.close()
    md5 = str(hash_code).lower()
    return md5
 
if __name__ == "__main__":
    filepath='/home/hilltone/ftp'
    print (filepath)
    for dirpath,dirnames,filelist in os.walk('.'):
        print (dirpath) 
        for files in filelist:
            print (files)
            olddir= os.path.join(dirpath,files)
            filename = os.path.splitext(files)[0]
            filetype = os.path.splitext(files)[1]
            md5 = get_md5(olddir)
            print (md5)
            newdir = os.path.join(dirpath,md5+filetype)
            os.rename(olddir,newdir)
            print (olddir+'---'+newdir)
    
    
