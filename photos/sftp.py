import pysftp
import os
import glob

def upload_file(filepath_list):

    private_key = "/home/soumya/ubuntuNew.pem"  # can use password keyword in Connection instead
    srv = pysftp.Connection(host="3.16.108.210", username="ubuntu", private_key=private_key)
    srv.chdir('/home/ubuntu/bot_psu')  # change directory on remote server
    for each_Filepath in filepath_list:
        srv.put(each_Filepath)
        print(each_Filepath)  # To download a file, replace put with get
    srv.close() 

source_path=r'/home/soumya/Desktop/Python_Insta_botting/photos'
os.chdir(source_path)
myjpgFiles=glob.glob('*.jpg')
filepath_list=[]
for jpegs in myjpgFiles:
    filepath_list.append(jpegs)

filepath_list.append("captions.json")

upload_file(filepath_list)