import random
strTags=open('file.txt','r+',encoding='utf8')
listTag=strTags.readlines()
leng=len(listTag)
names=" "
for i in range(0,10):
    z=random.randrange(0,leng-1,1)
    names=names+" "+"@"+str(listTag[z])[:-2]

print(names)