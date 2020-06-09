import instabot
import time
import os
import glob
import random

def getCaption(captionpath):
    
    strTags=open('/home/ubuntu/bot_photostockin/file.txt','r+',encoding='utf8')
    listTag=strTags.readlines()
    leng=len(listTag)
    names=" "
    for i in range(0,5):
        z=random.randrange(0,leng-1,1)
        names=names+" "+"@"+str(listTag[z])[:-1]
    strCaption=open(captionpath,'r+',encoding='utf8')
    strCaptiontxt=strCaption.read()
    strCaption.close()
    finalCaptiontxt=strCaptiontxt+names
    return finalCaptiontxt

#os.chdir(r'C:\\Users\\Administrator\\Desktop\\insta poster\\punnysideup')
path=r'/home/ubuntu/bot_photostockin'
os.chdir(path)

myjpgFiles=glob.glob('*.jpg')

#os.chdir(r'C:\\Users\\Administrator\\Desktop\\insta poster\\bot_PSU')
#path=r'C:\\Users\\Administrator\\Desktop\\insta poster\\punnysideup\\'
#path=r'/home/soumya/Desktop/Python_Insta_botting/bot/profiles/travelsticlife/prod_ready/'
trackerpath=path+"/"+"Tracker.txt"
count=0
tracking=open(trackerpath,'r+',encoding='utf8')
str_track=tracking.read()
for i in myjpgFiles:
    str_track=tracking.read()
    
    photopath=path+"/"+str(i)
    captionpath=path+"/"+str(i)[:-3]+"txt"
    print("-----------------------------------------------------------")
    print(photopath)
    print("-----------------------------------------------------------")
    print(captionpath)
    print("-----------------------------------------------------------")
    if str(i) not in str_track:
        bot = instabot.Bot(filter_private_users=False)
        bot.login(username = "photostockin", password = "Jan@2020")
        captiontext=getCaption(captionpath)
        print(captiontext)
        bot.upload_photo(photopath,caption=captiontext)
        tracking.write(str(i)+"\n")
        count=count+1
        break
    print("-----------------------------------------------------------")
    
tracking.close()
