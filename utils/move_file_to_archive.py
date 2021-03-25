import os
import shutil
import datetime as dt
from datetime import datetime, date, time

# print now #2013-05-23 04:07:40.951726    
def moveFilesToArchive(src:str, dest:str, destFile:str):
    src_files = os.listdir(src)
    previousDate = dt.datetime.today() - dt.timedelta(days=1)
    previousDateFormatted = previousDate.strftime ('%d-%m-%Y') # format the date to ddmmyyyy
    # print(previousDateFormatted)
    destFileName = destFile+previousDateFormatted+".xlsx"
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.move(full_file_name, os.path.join(dest, destFileName))
    # print("move successful!!!")
    return True