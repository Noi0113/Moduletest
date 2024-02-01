import streamlit as st
import sqlite3

# Streamlitアプリの作成
def app():
    st.title('データベース実験')
    # データベース接続の作成
    conn = sqlite3.connect('test-monketsu.db')
    c = conn.cursor()

    # Streamlitのテキスト入力フィールド
    user_input = st.text_input("テキストを入力してください")

    # ユーザーが何かを入力した場合、それをデータベースに挿入
    if user_input:
        c.execute('''
            INSERT INTO TestTable (text) VALUES (?)
        , (user_input,))
        conn.commit()  # 変更を保存

    # データベースからデータを取得して表示
    c.execute('SELECT * FROM TestTable')
    data = c.fetchall()
    st.write(data)
