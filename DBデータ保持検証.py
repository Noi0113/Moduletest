import streamlit as st
import sqlite3
import pandas as pd

# データベース名
db_name = 'test-monketsu.db'

# 全てのデータを選択するSQL文
select_all_sql = 'select * from tips'

# SQLiteデータベースに接続し、データを読み込む
with sqlite3.connect(db_name) as conn:
    df_from_sql = pd.read_sql(select_all_sql, conn)

# 列名を取り出す
df_from_sql_columns = df_from_sql.columns

# Streamlitのセレクトボックスで列を選択
option = st.selectbox('どの列がはいっているデータを抽出しますか？', (df_from_sql_columns))

# ユーザーからの入力を受け取る
num = st.text_input('数字を半角で入力してください :例 0.04')

# 列と入力値両方が入力されるまで待つためのif文
if not option or not num:
    st.title("列と数字が入力されるまで待ちます")
else:
    st.title("選択されました")

    # SQL文を作成
    def sql1(columns, num2):
        sql = 'select * from tips where ' + columns + ' > ' + num2
        return sql

    sql2 = sql1(option, num)

    # SQL文を実行し、結果を取得
    with sqlite3.connect(db_name) as conn:
        df_from_sql2 = pd.read_sql(sql2, conn)

    # 結果を表示
    st.dataframe(df_from_sql2)
