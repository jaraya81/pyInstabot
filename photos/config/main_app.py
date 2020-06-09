
import instabot
import time
import os
import glob
import random


#os.chdir(r'C:\\Users\\Administrator\\Desktop\\insta poster\\punnysideup')
os.chdir(r'/home/ubuntu/bot_psu')

myjpgFiles=glob.glob('*.jpg')

#os.chdir(r'C:\\Users\\Administrator\\Desktop\\insta poster\\bot_PSU')
#path=r'C:\\Users\\Administrator\\Desktop\\insta poster\\punnysideup\\'
path=r'/home/ubuntu/bot_psu/'
trackerpath=path+"Tracker.txt"
captiontext1='''Like it , Share it with your friends or tag them in the comments: 
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
#punnysideup
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Follow us @punny.sideup for more
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
•
•
•
•
•
#LaughSpreadLove #quotes #instagood #instadaily #fun #amazing #likeforlike #instalike #smile #follow4follow #friends
#Repost #followforfollow #igers #bollywood #kerala #fashion #maharashtra #likeforlikes #sarcastic #rajasthan #art #insta
#tiktok #pune

'''
captiontext2='''If you Like it , tag your friends in the comments: 
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

for more such content Follow us @punny.sideup and share your ideas with #punnysideup
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
•
•
•
•
•
#LaughSpreadLove #quotes #instagood #instadaily #fun #amazing #likeforlike #instalike #smile #follow4follow #friends
#Repost #followforfollow #igers #bollywood #laugh #india #maharashtra #likeforlikes #sarcastic #memes #art #insta
#tiktok #pune

'''
tracking=open(trackerpath,'r+',encoding='utf8')
str_track=tracking.read()
for i in myjpgFiles:
    str_track=tracking.read()
    photopath=path+str(i)
    if str(i) not in str_track:
        bot = instabot.Bot(filter_private_users=False)
        bot.login(username = "punny.sideup", password = "Mar@2020")
        strTags=open('/home/ubuntu/bot_psu/file.txt','r+',encoding='utf8')
        listTag=strTags.readlines()
        leng=len(listTag)
        names=" "
        num=random.randint(-20,20)
        print("Random number generated : ",num)
        for i in range(0,5):
            z=random.randrange(0,leng-1,1)
            names=names+" "+"@"+str(listTag[z])[:-1]
            
        if num<0:
            cap=captiontext1+names
        else:
            cap=captiontext2+names
        strTags.close()
        print(cap)
        bot.upload_photo(photopath,caption=cap)
        tracking.write(str(i)+"\n")
        break
    

tracking.close()
