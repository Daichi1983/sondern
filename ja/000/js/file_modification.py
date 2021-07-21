fname = "s0131-s0135"

# 上記のファイル名をそれぞれのjsファイルの拡張子より前のものに変える。

import re
num = 1
frs_len = 1

# ファイルを開く


with open(fname + '.js','r', encoding="utf-8") as f:
  fr=f.read()

# ディレクトリ名を得る
fr_split = fr.split("\n")
directory = fr_split[2][52:54] #ディレクトリ名を得た


# それぞれのファイル番号を得る
for frs in fr_split:
 frs = re.sub('タイトル</a>', 'タイトル', frs)
 frss = frs.split("<div class=\"col-2\">")
 frs_len=len(frss)
 frsss = frss[frs_len-1].split("</div></div>")
 file_number = frsss[0]
 if len(file_number) > 3:
  file_number = file_number[0:3]
 if len(file_number) == 2:
  file_number = "0" + file_number
 if len(file_number) == 1:
  file_number = "00" + file_number
 frs = re.sub('class="col-8\">','class=\"col-8\"><a href=\"../0' + directory + '/s0' + file_number + '.html\">', frs)
 with open(fname + '.txt','a', encoding="utf-8") as f:
  f.write(frs + "\n")
  print(frs)

#--- 確定 ---


