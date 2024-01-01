# pythonでcsvを編集

## 初期環境構築

コンテナの起動
```
# build
docker compose build

# コンテナの起動、作成
docker compose up
```

hello worldの表示
```
# コンテナに入る
docker-compose exec python3 bash

# sample.pyを実行
python opt/sample.py

実行結果に[Hello, world!]が表示されることを確認
```

`.env-copy`から`.env`を作成。

## CSVを閲覧する

1. `opt/csv`配下に読み込みたいCSVを設置
2. `.env`に読み取りたいCSVファイルを定義
3. `read-csv.py`を実行
4. コンソール画面でCSVが確認できること

## CSVを編集する

1. `opt/csv`配下に編集したいCSVを設置
2. `.env`に編集したいCSVファイルを定義
3. `edit-csv.py`を実行
4. `opt/csv`配下に`編集したいCSV名-updated.csv`があることが確認できること