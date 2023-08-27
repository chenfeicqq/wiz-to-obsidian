import os.path
import time
from datetime import datetime

mtime_string = "2020-11-11 21:38:29"
atime_string = "2020-11-12 22:38:29"
format_string = "%Y-%m-%d %H:%M:%S"

datetime_obj = datetime.strptime(atime_string, format_string)
print(datetime_obj.timestamp())
print(datetime_obj.ctime())


file = "/Users/chenfei/Downloads/笔记/任务/13年/12.06～12.19.md"

os.utime(file, (datetime.strptime(atime_string, format_string).timestamp(), datetime.strptime(mtime_string, format_string).timestamp()))

ctime = time.ctime(os.stat(file).st_ctime)
mtime = time.ctime(os.stat(file).st_mtime)
atime = time.ctime(os.stat(file).st_atime)

print(ctime)
print(mtime)
print(atime)
