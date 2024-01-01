import csv
import os
from dotenv import load_dotenv

# .envファイルの内容を読み込む
load_dotenv()

# csvファイルを定義
file = './csv/' + os.environ['CSV_FILE'] + os.environ['EXTENSION']

f = open(file, 'r')
rows = csv.reader(f) # ファイルからデータを読み込み

print(rows)
for row in rows:
    print(row)
f.close
