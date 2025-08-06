# Aug.6.2025
# AUTHOR: TY
# R0286 P4ラインで PJの中身をチェックする必要性があったため作成

# cd内にinifileを置き、サーチする文字列を指定する

# Aug.6.2025    create

import os
import configparser

# iniファイルを読み込む
config = configparser.ConfigParser()
config.read("search_strings.ini", encoding="utf-8")


# 検索文字列リストを取得
search_strings = [s.strip() for s in config["SearchStrings"]["strings"].split(",")]

# 文字列を確認
print("検索する文字列リスト:")
for s in search_strings:
    print(f"- {s}")

# チェックするフォルダのパス
folder_path = "./search"

# 結果を出力するファイル
output_file = "search_results.txt"

# 合計カウンター
total_count = 0

with open(output_file, "w", encoding="utf-8") as out:
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith((".txt", ".PJ")):
            file_path = os.path.join(folder_path, filename)
            out.write(f"--- {filename} ---\n")
            
            # with open(file_path, "r", encoding="utf-8") as f:
            with open(file_path, "r", encoding="cp932") as f:  # Shift_JIS対応
                for lineno, line in enumerate(f, start=1):
                    for string in search_strings:
                        count = line.count(string)
                        if count > 0:
                            total_count += count
                            out.write(f"行 {lineno}: '{string}' が {count} 回含まれています\n")

    print(f"検索結果を '{output_file}' に出力しました。")
    print(f"検索文字列の合計出現回数: {total_count}")

