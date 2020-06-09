import json
import glob
#reading
with open('captions.json', 'r+') as f:
     jsonload= json.load(f)
     myjpgFiles=glob.glob('*.jpg')
     myjpgFiles.sort()
     for jpgs in myjpgFiles:
          temp_dict={jpgs:""}
          jsonload.update(temp_dict)
          f.seek(0)
          json.dump(jsonload,f)