import re
import codecs

fl = codecs.open("file_list.txt", "r")
flr = fl.read()
filelist = flr.split("\n")
del filelist[-1]

for i in filelist:
 f = codecs.open(i, "r", encoding="utf-8")
 inside = f.read()
 inside = inside.replace("\r\n","")
 inside = inside.replace("'","\\'")
 inside = inside.replace('<div class="bango">','<div class="row"><div class="col-2">')
 inside = inside.replace('</div><div class="row">','</div></div>\r\n<div class="row">')
 inside = inside.replace('"daimoku"','"col-8"')
 inside = inside.replace('"mpage"','"col-2"')
 inside = inside + "</div>"
 inside = inside.replace("</div></div>\r\n","</div></div>');\r\n")
 inside = inside.replace("</div></div></div>","</div></div></div>');")
 inside = inside.replace("<div class=\"row\">","document.write('<div class=\"row\">")
 inside = inside.replace("<div id=\"container\">","document.write('<div class=\"container\">');\r\ndocument.write('<div class=\"row\"><div class=\"col-2\">分類番号</div><div class=\"col-8\">分類題目</div><div class=\"col-2\">総目次ページ</div></div>');\r\n")
 print(inside)
 print("Finish!")
 f.close()
 f = codecs.open(i, "w", encoding="utf-8")
 f.write(inside)
 f.close()

print("Big Finish")