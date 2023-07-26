# sondern
ここは大正から昭和にかけて活躍したドイツ語学者、[関口存男](https://ja.wikipedia.org/wiki/%E9%96%A2%E5%8F%A3%E5%AD%98%E7%94%B7)（せきぐち つぎお、1894-1958）が収集していた語学の用例集であるノート（関口存男文例集）を公開する準備の場です。

私はたまたま、2万5千頁におよぶ関口存男の文例集全データを手に入れたこと、関口の死後50年が過ぎて著作権法上の権利が切れたこともあり、公開準備を進めています。

実はこれまでも[無料ホームページスペース](http://sondern.starfree.jp/)で公開してきましたが、2018年で更新が止まっていました。「気長にお待ちください」と言いつつ、待たせすぎていました。

その間に技術は進歩し、CMSの時代からSSG（静的サイトジェネレーター）時代へと変わり、大規模なサイトでも早く見せる方法が出てきました。

そこで、現在、すべてのノートをSSGで公開すべく、ここにデータを置き、SSGに作成していくことにしました。技術的にはまだよくわかっていないところも多々あるので、成功するかは分かりませんが、一つの試みとしてやってみます。

## それぞれのファイルの作り方

### 基本となるファイルの作り方

いくつかのファイルを用いて自動で作成していきます。まずはそれぞれの画像フォルダに行って画像ファイルのリストを作成します。

```
dir /b *.TIF > file_list.txt
```

簡単ですね。できたfile_list.txtはそれぞれ/ja/以下のフォルダに入れていきます。

### HTMLファイルの作り方

/ja/001に入っているファイルを参照に、以下のファイルを準備します。

* 1_cont.html
* 2_cont.html
* 3_cont.html
* breadcrumb.js
* file_list.txt
* html-format.py

HTMLファイルは合体させて完成後のファイルの一部とするものです。単体ではあまり意味がありません。

breadcrumb.jsはその名の通りパンくずリスト作成用JavaScriptファイルです。これも完成後のファイルの一部とするものです。

肝心なのはpythonファイルです。へたくそなファイルですが、中身は以下の通りです。

```python:html-format.py

import re
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

```

HTMLファイル配下ではfile_list.txtの中身の.TIFや.GIFといった拡張子を.htmlに変換する必要があります。

変換後、html-format.pyを動かせば自動的にファイルが完成します。

### JSファイルの作り方

以下のファイルを用意します。

* file_list.txt
* js-format.py
* sample.js

まず、file_list.txtの中の画像の拡張子、.TIFや.gifを.jsに置換します。

その後、js-format.pyを動かせば完成です。

```python:js-format.py

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

```

これでひとまずファイルはできあがるはずです。

ただ、JavaScriptの変数の宣言にconstやletじゃなくてvarを使っていたりと少し古い書き方をしているので、将来的には見せ方を考えないといけません。

JavaScriptファイルはリンクを修正しないといけませんので、以下のようなやぼったいファイルで一ファイルずつリンクを付けて手で修正していきました。プログラムを書く前は1ファイル10分以上かけていました。やっぱりプログラムで書くとチェックを含めて一瞬で済むので便利ですね。

```python
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
```

余談ですが、以下の書き方でディレクトリ名を得られるのはJavaScript側に特徴があるからです。

```
# ディレクトリ名を得る
fr_split = fr.split("\n")
directory = fr_split[2][52:54] #ディレクトリ名を得た
```

JavaScript側は以下のようになっています。

``` JavaScript
document.write('<div class="container">');
document.write('<div class="row"><div class="col-2">袋番号</div><div class="col-8">タイトル</div><div class="col-2">ページ</div></div>');
```

本来なら上の通りパスを使うのがスマートですね。

そのあとはコマンドプロンプトで拡張子を書き換えました。これは簡単ですね。

```
ren *.txt *.js
```

ネットにはこうした写真集、画像集を効率的に見せるノウハウがあまり転がっていないので、手探りでやっています。

個人で2万5千ファイルの画像を公開しようとする人は少ないでしょうから、仕方ないですね。

## Netlifyの設定

以下のように設定しないとエラー続出でした。

| Repository | github.com/Daichi1983/sondern |
|:---|:---|
|Base directory |Not set |
|Build command |Not set |
|Publish directory |Not set |
|Deploy log |visibility Logs are public |
|Builds |Active |

## XMLファイル構築の手続き

XMLファイルでText Encoding Initiativeに準拠したデータベースを検討しています。まずは文例集のディレクトリごとに分けていたファイルを整理します。

```python
import glob

# ファイルの一覧を取得する
file_list = glob.glob("*.js")

# ファイルを一つにまとめる
with open("088all.txt", "w", encoding="utf-8") as outfile:
    for file_name in file_list:
        with open(file_name, "r", encoding="utf-8") as infile:
            outfile.write(infile.read())
```

出来上がったテキストファイルは同じディレクトリに入れます。次に全体を一覧できる目次ファイルを作ります。

```python
import glob

# ファイルの一覧を取得する
file_list = glob.glob("*.txt")

# ファイルを一つにまとめる
with open("all.txt", "w", encoding="utf-8") as outfile:
    for file_name in file_list:
        with open(file_name, "r", encoding="utf-8") as infile:
            outfile.write(infile.read())
```

そうしてExcelで成形すると表が出来上がりました。

|分類番号 | 分類題目 | 総目次ページ |
|:---|:---|:---|
|1 | 名詞 Substantiv | 1 |
|2 | 名詞の型 Substantivtypen | 3 |
|3 | 性と数 Genus und Numerus | 4 |
|4 | 格支配 Rektion | 7 |
|5 | 1格 Nominativ | 8 |

## XMLファイルの構造決定

XMLファイルでデータベースを作るにあたっては、構造設計をしないといけません。関口の文例集の場合は大きな分冊があって、その中に小項目が書かれていくという書き方がされているので、それに従ってクラス分けをしていきます。

なぜか最初に入っていたのでこれだけは入れておきます。

```HTML
<?xml version="1.0" encoding="UTF-8"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0" xml:lang="ja">
    <teiHeader xml:lang="ja">
        <fileDesc>
            <titleStmt>
                <title>
                    Sekiguchi Manuscript
                </title>
                <author>
                    Tsugio Sekiguchi
                </author>
                <respStmt>
                    <resp>
                        reprinter and editor
                    </resp>
                    <name>
                        Daichi Uchibori
                    </name>
                </respStmt>
            </titleStmt>
            <publicationStmt>
                <p>
                    for use by whoever wants it
                </p>
                <authority> Tsugio Sekiguchi </authority> 
                <pubPlace> Tokyo </pubPlace> 
                <date> 1930-1958 </date> 
            </publicationStmt>
            <notesStmt> 
                <note>大阪大学所蔵の関口存在男文例集のスキャンデータ</note> 
                <note>Scan data of Sekiguhi Manuscript from Osaka University</note> 
            </notesStmt>
            <sourceDesc>
                <p>
                    created on Wwednesday 19th July 2023 08:44:00 PM
                </p>
            </sourceDesc>
        </fileDesc>
    </teiHeader>
    <text>
        <body>
            <head>
                Manuscripts written and collected by Tsugio Sekiguchi<lb/>
                Handschriften, geschrieben und gesammelt von Tsugio Sekiguchi<lb/>
            </head>
            <schemaSpec ident="sekiguchi_manuscript" docLang="ja" prefix="tei_" xml:lang="en">
                <moduleRef key="core" except=""/>
                <moduleRef key="tei" except=""/>
                <moduleRef key="header" except=""/>
                <moduleRef key="textstructure" except=""/>
            </schemaSpec>
```

エクセル等表計算ソフトでちょっと整形して、数時間でそこそこのものができました。

```HTML

<TEI xmlns="http://www.tei-c.org/ns/1.0" xml:lang="ja">
<teiHeader xml:lang="ja">
<fileDesc>
<titleStmt>
<title> Sekiguchi Manuscript </title>
<author> Tsugio Sekiguchi </author>
<respStmt>
<resp> reprinter and editor </resp>
<name> Daichi Uchibori </name>
</respStmt>
</titleStmt>
<publicationStmt>
<p> for use by whoever wants it </p>
<authority> Tsugio Sekiguchi </authority>
<pubPlace> Tokyo </pubPlace>
<date> 1930-1958 </date>
</publicationStmt>
<notesStmt>
<note>大阪大学所蔵の関口存在男文例集のスキャンデータ</note>
<note>Scan data of Sekiguhi Manuscript from Osaka University</note>
</notesStmt>
<sourceDesc>
<p> created on Wwednesday 19th July 2023 08:44:00 PM </p>
</sourceDesc>
</fileDesc>
</teiHeader>
<text>
<body>
<head>
Manuscripts written and collected by Tsugio Sekiguchi
<lb/>
Handschriften, geschrieben und gesammelt von Tsugio Sekiguchi
<lb/>
</head>
<schemaSpec ident="sekiguchi_manuscript" docLang="ja" prefix="tei_" xml:lang="en">
<moduleRef key="core" except=""/>
<moduleRef key="tei" except=""/>
<moduleRef key="header" except=""/>
<moduleRef key="textstructure" except=""/>
</schemaSpec>
<msItem n="1">
<locus from="1" to="2">SS.1-2</locus>
<title type="main">名詞 Substantiv</title>
<div1 n="01-1B">
<title type="sub">固有名詞でもあり普通名詞でもあり</title>
<locus from="1" to="1">S1</locus>
<graphic url="https://sondern.netlify.app/img/001/S0001.gif"/>
</div1>
<div1 n="01-2B">
<title type="sub">固有名詞</title>
<locus from="2" to="49">SS2-49</locus>
<graphic url="https://sondern.netlify.app/img/001/S0002.gif"/>
</div1>
```
