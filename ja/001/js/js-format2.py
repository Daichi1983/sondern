import re
import codecs

fl = codecs.open("file_list.txt", "r")
flr = fl.read()
filelist = flr.split("\n")
del filelist[-1]

for i in filelist:
 f = codecs.open(i, "r", encoding="utf-8")
 inside = f.read()
 inside = inside.replace('<figure class="wp-block-image is-resized">','')
 inside = inside.replace('<figure class="wp-block-image">','')
 inside = re.sub(r'class="wp-image-[0-9]{3}"', 'class="mw-100"', inside)
 inside = re.sub(r' width="[0-9]{3}" height="[0-9]{4}"', '', inside)
 inside = inside.replace('</figure>','')
 inside = re.sub(r'.gif"><img src', '.gif" class="luminous"><img src', inside)
 print(inside)
 print("Finish!")
 f.close()
 f = codecs.open(i, "w", encoding="utf-8")
 f.write(inside)
 f.close()

print("Big Finish")