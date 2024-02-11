import streamlit as st
import sqlite3
import subprocess

# Gitのユーザー情報
GIT_USER_EMAIL = "s709776801.55yotsuya@gmail.com"
GIT_USER_NAME = "Noi0113"

# Gitの認証情報をキャッシュする関数
def cache_git_credentials():
    try:
        subprocess.run(["git", "config", "--global", "credential.helper", "cache"], check=True)
        st.success('Gitの認証情報をキャッシュしました')
    except subprocess.CalledProcessError as e:
        st.error(f'エラーが発生しました: {e}')

# SQLiteデータベースに接続
conn = sqlite3.connect('test-monketsu.db')
c = conn.cursor()

# テーブルが存在しない場合は作成
c.execute('''CREATE TABLE IF NOT EXISTS your_table_name (
             column1 datatype,
             column2 datatype
             )''')

# Streamlitアプリケーション
def main():
    st.title('データ入力!!!!')

    # データ入力フォーム
    input_data1 = st.text_input('データ1')
    input_data2 = st.text_input('データ2')

    # 入力されたデータをデータベースに挿入
    if st.button('データを保存'):
        c.execute("INSERT INTO your_table_name (column1, column2) VALUES (?, ?)", (input_data1, input_data2))
        conn.commit()
        st.success('データを保存しました')

        # Gitコマンドを実行して変更をプッシュ
        try:
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "Update data", "--author", f"{GIT_USER_NAME} <{GIT_USER_EMAIL}>"], check=True)
            subprocess.run(["git", "push"], check=True)
            st.success('データを保存し、GitHubにプッシュしました')
        except subprocess.CalledProcessError as e:
            st.error(f'エラーが発生しました: {e}')

if __name__ == '__main__':
    cache_git_credentials()  # Gitの認証情報をキャッシュ
    main()
