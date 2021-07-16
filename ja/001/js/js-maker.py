import re
import codecs

fl = codecs.open("file_list.txt", "r")
flr = fl.read()
filelist = flr.split("\n")
del filelist[-1]

for i in filelist:
 f = codecs.open("sample.js", "r", encoding="utf-8")
 inside = f.read()
 inside = inside.replace("置換", i[1:5])
 print(inside)
 print("Finish!")
 f.close()
 f = codecs.open(i, "w", encoding="utf-8")
 f.write(inside)
 f.close()

print("Big Finish")