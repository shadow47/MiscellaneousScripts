# coding: utf-8
# this script changes the terminal prompt
# It reduces the length of the command prompt trimming all folders in the path except the last one.
# eg if path is  x@y: abc/def/ghi  changed to x@y: a/d/ghi 
# also replaces $ with λ (looks cool)
# set this script in .bashr by replacing the value of PS1 with this     PS1='$(python ~/.short.pwd.py)' 
import os
from commands import getoutput
from socket import gethostname
hostname = gethostname()
username = os.environ['USER']
pwd = os.getcwd()
homedir = os.path.expanduser('~')
pwd = pwd.replace(homedir, '~', 1)
dirs = pwd.split("/");
dirs.pop(0);
y = ""
last = len(dirs)-1;
for index, x in enumerate(dirs):
   if(index < last): 
       y = y +'/'+ x[0];
   else:
       y = y +'/'+ x; #show last element as full string
#if len(pwd) > 30:
#    pwd = pwd[:10]+'...'+pwd[-20:] # first 10 chars+last 20 chars
print '\033[01;32m%s@%s:\033[01;33m%s \033[01;32mλ \033[00m' % (username, hostname, y)  
