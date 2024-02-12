import streamlit as st
import sqlite3
import subprocess

# Gitのユーザー情報を設定する
GIT_USER_EMAIL = "s709776801.55yotsuya@gmail.com"
GIT_USER_NAME = "Noi0113"

# GitHubのアクセストークン
GITHUB_ACCESS_TOKEN = "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"

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
    st.title('データ入力、アクセストークンをどうにかした版?')

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
            # Gitのユーザー情報を直接指定してコミットを作成
            subprocess.run(["git", "config", "--global", "user.email", GIT_USER_EMAIL])
            subprocess.run(["git", "config", "--global", "user.name", GIT_USER_NAME])
            
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "Update data"], check=True)
            
            # GitHubのアクセストークンを使用してプッシュ
            subprocess.run(["git", "push", f"https://{GIT_USER_NAME}:{GITHUB_ACCESS_TOKEN}@github.com/{GIT_USER_NAME}/Moduletest.git"], check=True)

            
            st.success('データを保存し、GitHubにプッシュしました')
        except subprocess.CalledProcessError as e:
            st.error(f'エラーが発生しました: {e}')

if __name__ == '__main__':
    cache_git_credentials()  # Gitの認証情報をキャッシュ
    main()
