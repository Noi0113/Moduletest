import streamlit as st
import sqlite3

# Streamlitアプリの作成
def app():
    st.title('データベース実験')
    # データベース接続の作成
    conn = sqlite3.connect('test-monketsu.db')
    c = conn.cursor()

    # Streamlitのテキスト入力フィールド
    user_input1 = st.text_input("テキストを入力してください")
    user_input2 = st.text_input("テキストを入力してください2")
    # ユーザーが何かを入力した場合、それをデータベースに挿入
    if user_input1:
        c.execute('''
            INSERT INTO TestTable (taikai_name) VALUES (?)
        ''', (user_input1,))
        conn.commit()  # 変更を保存
    if user_input2:
        c.execute('''
            INSERT INTO TestTable (taikai_password) VALUES (?)
        ''', (user_input2,))
        conn.commit()  # 変更を保存

    # データベースからデータを取得して表示
    c.execute('SELECT * FROM TestTable')
    data = c.fetchall()
    st.write(data)

# Streamlitアプリを実行
if __name__ == "__main__":
    app()
