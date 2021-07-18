﻿import re
import codecs


m1 = codecs.open("1_cont.html", "r", encoding="utf-8")
m3 = codecs.open("3_cont.html", "r", encoding="utf-8")
m1r = m1.read()
m3r = m3.read()

fl = codecs.open("file_list.txt", "r")
flr = fl.read()
flr = flr.replace(".tif",".html")
flr = flr.replace(".TIF",".html")
flr = flr.replace(".gif",".html")
flr = flr.replace("S0","s0")
flr = flr.replace("L0","l0")
flr = flr.split("\n")
del flr[-1]
nmb = 0

lnth = len(flr)

flr.append(flr[0])

while nmb < lnth:
 nmp = nmb - 1
 nma = nmb + 1
 m2r = "uppage = \"../000/l001-l002.html\";" + "\r\n" + "previouspage = \"" + flr[nmp] + "\";" + "\r\n" + "nextpage = \"" + flr[nma] + "\";" + "\n"
 main_content = m1r + m2r + m3r
 print(main_content)
 print(flr[nmb])
 fl2 = codecs.open(flr[nmb], "w", encoding="utf-8")
 fl2.write(main_content)
 fl2.close()
 nmb += 1

print("Big Finish")
fl.close()