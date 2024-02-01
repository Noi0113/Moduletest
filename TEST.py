import sqlite3
import streamlit as st

st.title('SQLのテスト')
# データベースに接続
conn = sqlite3.connect('test-monketsu.db')

# カーソルオブジェクトを作成
c = conn.cursor()

# テーブル作成のクエリを実行
c.execute('''
    CREATE TABLE my_table(
        id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

# 変更を保存
conn.commit()

# データベース接続を閉じる
conn.close()
