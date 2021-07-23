import re
import codecs
import os

place = os.getcwd()
place_s = place.split("\\")
folder = place_s[-2] #ディレクトリ名を得る

fl = codecs.open("file_list.txt", "r")
flr = fl.read()
flr = flr.replace(".tif",".js")
flr = flr.replace(".TIF",".js")
flr = flr.replace("L0","l0")
flr = flr.replace("S0","s0")
flr = flr.split("\n")
nmb = 0

lnth = len(flr)
del flr[-1]

for i in flr:
 nmp = nmb - 1
 nma = nmb + 1
 fl1 = codecs.open("sample.js", "r", encoding="utf-8")
 main_content = fl1.read()
 main_content = main_content.replace("番号",folder)
 main_content = main_content.replace("置換",i[1:5])
 print(main_content)
 print(i[1:5])
 fl2 = codecs.open(i, "w", encoding="utf-8")
 fl2.write(main_content)
 fl2.close()
 nmb += 1

print("Big Finish")
fl.close()