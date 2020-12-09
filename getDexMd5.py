#!/usr/bin/python
import sys 
import zipfile
import hashlib
import base64
import os 
import re 
file_name=""

if __name__ == "__main__":
	file_name = sys.argv[1]



f_zip = zipfile.ZipFile(file_name,'r')
classesDexFile = f_zip.read('classes.dex')
hash = hashlib.md5()
hash.update(classesDexFile)

with open('classes.dex','wb') as f:
	f.write(classesDexFile)


version = classesDexFile.decode("utf-8",errors='ignore').partition('App: ')[-1].partition('.')[0]

all_apk_info = os.popen("aapt dump badging %s " % file_name).read()
package_name = re.compile(r"package: name='(\S+)'").findall(all_apk_info)[0]
app_version  = re.compile(r"versionName='(\S+)'").findall(all_apk_info)[0]
print("App PackageName:" + package_name)
print("App Version:" + app_version)
print("App Dex MD5:" + base64.b64encode(hash.digest()).decode("utf-8"));