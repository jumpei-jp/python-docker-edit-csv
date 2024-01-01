import csv
import os
from dotenv import load_dotenv

# 0埋めする
def filled_with_zero(day_arg):
    # 1桁の場合は0埋めをする
    if len(str(day_arg)) == 1:
        # print(day_arg)
        return '0' + day_arg
    else:
        return day_arg

# .envファイルの内容を読み込む
load_dotenv()

# 編集元となるファイルを定義
base_file = './csv/' + os.environ['CSV_FILE'] + os.environ['EXTENSION']
f1 = open(base_file, 'r')
rows = csv.reader(f1) # ファイルからデータを読み込み

# 加工した新規ファイルを定義
updated_file = './csv/' + os.environ['CSV_FILE'] + '-updated' + os.environ['EXTENSION']
f2 = open(updated_file, 'w')
csv_writer = csv.writer(f2)

# ベースデータを読み込んで必要カラムを更新して新しいCSVを作成
# 配列番号とそれに紐づくヘッダー名を変数に定義
company_name = 1
day = 4

for row in rows:
    row[company_name] = '検証株式会社'
    row[day] = filled_with_zero(row[day])
    csv_writer.writerow(row)
f2.close()
f1.close()
