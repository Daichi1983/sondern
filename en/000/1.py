import re
import codecs

nmb = 1

m1 = codecs.open("1_cont.html", "r", encoding="utf-8")
m3 = codecs.open("3_cont.html", "r", encoding="utf-8")
m1r = m1.read()
m3r = m3.read()

fl = codecs.open("file_list.txt", "r")
flr = fl.read()
flr = flr.split("\n")
del flr[-1]
fl.close()

lnth = len(flr)

for i in flr:
 fli = codecs.open(i, "r", encoding="utf-8")
 main_content = fli.read()
 print(main_content)
 main_content = main_content.replace('lang="ja"','lang="en"')
 main_content = main_content.replace('拡張子無しで','without kakuchoshi')
 main_content = main_content.replace('キー押下時に関数pageMove()を呼び出す','call pageMove() when a key is typed')
 main_content = main_content.replace('」が押されたか確認','')
 main_content = main_content.replace('「','')
 fli.close()
 fl2 = codecs.open(i, "w", encoding="utf-8")
 fl2.write(main_content)
 fl2.close()

print("Big Finish")
fl.close()