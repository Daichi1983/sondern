import glob

# ファイルの一覧を取得する
file_list = glob.glob("*.js")

# ファイルを一つにまとめる
with open("072all.txt", "w", encoding="utf-8") as outfile:
    for file_name in file_list:
        with open(file_name, "r", encoding="utf-8") as infile:
            outfile.write(infile.read())