import os
import shutil
import datetime

if "index.html" in os.listdir():
    shutil.copy("index.html","history/"+str(datetime.datetime.now())+".html")
    print("File copied!")