import instabot
import time
import os
import glob


#os.chdir(r'C:\\Users\\Administrator\\Desktop\\insta poster\\punnysideup')
os.chdir(r'/home/soumya/Desktop/Python Insta botting/photos')

myjpgFiles=glob.glob('*.jpg')

#os.chdir(r'C:\\Users\\Administrator\\Desktop\\insta poster\\bot_PSU')
#path=r'C:\\Users\\Administrator\\Desktop\\insta poster\\punnysideup\\'
path=r'/home/soumya/Desktop/Python Insta botting/photos'
trackerpath=path+"Tracker.txt"
captiontext='''
Get your Punny Side up: 👈

#punnysideup
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Follow us @punny.sideup for more

•
•
•
•
•
#LaughSpreadLove
#love
#instagood
#photooftheday
#like4like
#followme
#style
#follow
#instadaily
#fun
#amazing
#likeforlike
#instalike
#smile
#follow4follow
#friends
#Repost
#followforfollow
#igers
#TagsForLikes
#funny
#blogger
#f4f
#nofilter
#happiness
'''
tracking=open(trackerpath,'r+',encoding='utf8')
str_track=tracking.read()
for i in myjpgFiles:
    str_track=tracking.read()
    photopath=path+str(i)
    if str(i) not in str_track:
        bot = instabot.Bot(filter_private_users=False)
        bot.login(username = "punny.sideup", password = "a_password")
        print(captiontext)
        bot.upload_photo(photopath,caption=captiontext)
        tracking.write(str(i)+"\n")
    time.sleep(1000)
tracking.close()
