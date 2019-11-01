import os
import shutil
import datetime

if "index.html" in os.listdir():
    shutil.copy("index.html","history/"+str(datetime.datetime.now())+".html")
    print("File copied!")

for i in os.listdir():
    if "travis_wait" in i:
        os.remove(i)
print("Clean up complete!")