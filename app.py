from termcolor import colored
import os
from os import listdir
from os.path import isfile,isdir,join,getsize,basename
import json

os.system("color")

def rec(mypath,obj={}):
	sum=0
	for f in listdir(mypath):
		fp = join(mypath,f)
		if isfile(fp):
			print( colored(f,"green"), colored(getsize(fp),"red"))
			sum+=getsize(fp)
			obj[f]=getsize(fp)
		elif isdir(fp):
			obj[f]={}
			sum+=rec(fp,obj[f])[0]
	return [sum,obj]

root = basename("C:\\Users\\Miguel\\Desktop\\b")

print(json.dumps(rec("C:\\Users\\Miguel\\Desktop\\b")[1],indent=4))

# print(json.dumps(obj))
