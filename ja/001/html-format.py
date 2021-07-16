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

lnth = len(flr)

flr.append("s0001.html")

while nmb < lnth:
 nmp = nmb - 1
 nma = nmb + 1
 m2r = "uppage = \"../000/l001-l002.html\";" + "\n" + "previouspage = \"" + flr[nmp] + "\";" + "\n" + "nextpage = \"" + flr[nma] + "\";" + "\n"
 main_content = m1r + m2r + m3r
 print(main_content)
 print(flr[nmb])
 fl2 = codecs.open(flr[nmb], "w", encoding="utf-8")
 fl2.write(main_content)
 fl2.close()
 nmb += 1

print("Big Finish")
fl.close()