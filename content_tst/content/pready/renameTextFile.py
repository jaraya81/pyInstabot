import os
import datetime
import glob

#date_front=datetime.date.today() + datetime.timedelta(days=1)


os.chdir(r'/home/soumya/Desktop/Python_Insta_botting/content_tst/content')
mytxtFiles=glob.glob('*.txt')
mytxtFiles.sort()
for count,filename in enumerate(mytxtFiles):
   #date=date_front.strftime(r"%m%d")
   print(filename)
   date="PSU"
   if count<10:
       dest=date+"_0"+str(count)+".txt"
   else:
       dest=date+"_"+str(count)+".txt"
    
   src=filename
   os.rename(src, dest) 
    

#print(dateTomorrow)