import re
import codecs

fl = codecs.open("file_list.txt", "r")
flr = fl.read()
filelist = flr.split("\n")
del filelist[-1]

temp = codecs.open("1.txt", "r")
tmp = fl.read()

for i in filelist:
 f = codecs.open(i, "r", encoding="utf-8")
 inside = f.read()
 inside = inside.replace("翻訳",i[1-5])
 inside = inside.replace("\r\n","');\r\ndocument.write('")
 inside = "document.write('" + inside + "document.write('    </div>');\r\ndocument.write('  </div>');\r\ndocument.write('</div>');"
 f.close()
 f = codecs.open(i, "w", encoding="utf-8")
 f.write(inside)
 f.close()
 print(inside)

print("big finish")