import re
import codecs

fl = codecs.open("file_list.txt", "r")
flr = fl.read()
flr = flr.split("\n")
fl.close()


for i in flr:
 fli = codecs.open(i, "r", encoding="utf-8")
 main_content = fli.read()
 print(main_content)
 main_content = main_content.replace('袋番号','Number')
 main_content = main_content.replace('タイトル','Category Title')
 main_content = main_content.replace('ページ','Page')
 fli.close()
 fl2 = codecs.open(i, "w", encoding="utf-8")
 fl2.write(main_content)
 fl2.close()

print("Big Finish")
fl.close()