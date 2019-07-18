#!/usr/bin/python
#coding:utf-8
'''
Function:test
'''

import os
import sys

class TEST(object):
    def __init__(self):
        super(TEST, self).__init__()
    def testDescription(self,testType):
        return ('YOU SELECT %s'%testType)

'''
if __name__ == "__main__":
    usemessage = """
    ****************************************************
    test
    ****************************************************
    """
    print (usemessage)
    test1=Test()
    Res=test1.testDescription('test3')
    print Res
'''
