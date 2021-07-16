import re
import codecs

fl = codecs.open("file_list.txt", "r")
flr = fl.read()
filelist = flr.split("\n")
del filelist[-1]

for i in filelist:
 f = codecs.open(i, "r", encoding="utf-8")
 inside = f.read()
 inside = inside.replace('../img','/img')
 print(inside)
 print("Finish!")
 f.close()
 f = codecs.open(i, "w", encoding="utf-8")
 f.write(inside)
 f.close()

print("Big Finish")