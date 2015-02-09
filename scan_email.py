#!/usr/bin/env python
#coding:utf-8

from smtplib import SMTP as smtp
import optparse
from time import sleep
import imaplib
import poplib

def scan_smtp(server_name,uname,upass):
    host='smtp.'+server_name+'.com'
    port=25
    try:
        s = smtp(host,port)
        s.login(uname,upass)
        print "[+]sucess: %s: %s" %(uname,upass)
        return True
    except Exception :
        print "[-]failed: %s %s" %(uname,upass)
    return False
def scan_imap(server_name,uname,upass):
    host='imap.'+server_name+'.com'
    try:
        mail=imaplib.IMAP4_SSL(host)
        mail.login(uname,upass)
        print "[+]sucess: %s: %s" %(uname,upass)
        return True
    except Exception:
        print "[-]failed: %s %s" %(uname,upass)
    return False

def scan_pop3(server_name,uname,upass):
    host='pop.'+server_name+'.com'
    port=995
    try:
        mail=poplib.POP3_SSL(host,port)
        mail.user(uname)
        mail.pass_(upass)
        print "[+]sucess: %s: %s" %(uname,upass)
        return True
    except Exception:
        print "[-]failed: %s %s" %(uname,upass)
    return False

def scanemail(server_name,uname,upass):
    if(scan_imap(server_name,uname,upass)):
        return True
    elif(scan_smtp(server_name,uname,upass)):
        return True
    elif(scan_pop3(server_name,uname,upass)):
        return True
    else:
        return False

def main():
    scanemail('163','beyondkmp@163.com','XXXXXXXXXX')
if __name__=='__main__':
    main()
