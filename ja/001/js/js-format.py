import re
import codecs

fl = codecs.open("file_list.txt", "r")
flr = fl.read()
filelist = flr.split("\n")
del filelist[-1]

for i in filelist:
 f = codecs.open(i, "r", encoding="utf-8")
 inside = f.read()
 inside = inside.replace("'","\\'")
 inside = inside.replace("翻刻","原本")
 inside = inside.replace("原本 | Original","翻刻")
 inside = re.sub(r'http://biblevi.minibird.jp/sekiguchi/wp-content/uploads/[0-9]{4}/[0-9]{2}/S', "../../img/001/s", inside)
 inside = re.sub(r' id="exifviewer-img-[0-9]{1}" class="alignnone size-large wp-image-[0-9]{3}', "", inside)
 inside = re.sub(r'-[0-9]{3}x[0-9]{4}.gif', ".gif", inside)
 inside = re.sub(r' alt="" width="[0-9]{3}" height="[0-9]{4}"', "", inside)
 inside = inside.replace('<p><a href="../../img/','<a href="../../img/')
 inside = inside.replace("\r\n","');\r\ndocument.write('")
 inside = "document.write('<div class=\"container\">');\r\ndocument.write('" + inside + "\r\ndocument.write('</div>');"
 print(inside)
 print("Finish!")
 f.close()
 f = codecs.open(i, "w", encoding="utf-8")
 f.write(inside)
 f.close()

print("Big Finish")