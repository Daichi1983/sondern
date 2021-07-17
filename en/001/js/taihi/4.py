import re
import codecs

fl = codecs.open("file_list.txt", "r")
flr = fl.read()
filelist = flr.split("\n")
del filelist[-1]
temp = codecs.open("1.txt", "r", encoding="utf-8")
tmp = temp.read()
print(tmp)
temp.close()

for i in filelist:
 f = codecs.open(i, "r", encoding="utf-8")
 inside = f.read()
 inside = inside.replace('document.write(\'    </div>\');document','document.write(\'    </div>\');\r\ndocument.write(\'    <div id="tab2" class="tab-pane">\');\r\ndocument')
 f.close()
 f = codecs.open(i, "w", encoding="utf-8")
 f.write(inside)
 f.close()
 print(inside)
 print("Finish")

print("big finish")