import sqlite3
import subprocess
import streamlit as st

st.title('DBテスト！')
# ユーザーからの入力を収集
user_input = st.text_input("何か入力してください")

if st.button("送信"):
    # データをデータベースに保存
    conn = sqlite3.connect('test-monketsu.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS user_inputs (input TEXT)")
    c.execute("INSERT INTO user_inputs VALUES (?)", (user_input,))
    conn.commit()
    conn.close()
    st.write(f"あなたが入力したテキスト: {user_input}")

    # Gitコマンドを実行
    try:
        subprocess.check_call(['git', 'add', 'test-monketsu.db'])
        subprocess.check_call(['git', 'commit', '-m', 'Update database'])
        subprocess.check_call(['git', 'push'])
        st.write("データベースがGitHubリポジトリにプッシュされました。")
    except subprocess.CalledProcessError as e:
        st.write("エラーが発生しました：", e)
