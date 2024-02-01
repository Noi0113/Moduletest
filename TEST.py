import streamlit as st
import sqlite3

# Streamlitアプリの作成
def app():
    st.title('データベース実験変更版')
    # データベース接続の作成
    conn = sqlite3.connect('test-monketsu.db')
    c = conn.cursor()

    # Streamlitのテキスト入力フィールド
    user_input1 = st.text_input("テキストを入力してください")
    user_input2 = st.text_input("テキストを入力してください2")
    # ユーザーが何かを入力した場合、それをデータベースに挿入

    if st.button('送信'):
        c.execute('''
            INSERT INTO TestTable (taikai_name,taikai_password) VALUES (?,?)
        ''', (user_input1,user_input2))
        conn.commit()
        st.success("回答を送信しました！")
    
    # データベースからデータを取得して表示
    c.execute('SELECT * FROM TestTable')
    data = c.fetchall()
    st.write(data)

    st.subheader("これまでの回答")
    c.execute("SELECT * FROM TestTable")
    rows = c.fetchall()
    for row in rows:
        st.write(f"大会名: {row[0]}, 大会パスワード: {row[1]}")
# Streamlitアプリを実行
if __name__ == "__main__":
    app()
