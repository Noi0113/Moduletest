import streamlit as st
import sqlite3
import subprocess
import os

# Gitのユーザー情報を設定する
GIT_USER_EMAIL = "s709776801.55yotsuya@gmail.com"
GIT_USER_NAME = "Noi0113"

# GitHubのアクセストークン
GITHUB_ACCESS_TOKEN = "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"

# Gitの認証情報をキャッシュする関数
def cache_git_credentials():
    try:
        # credential.helper を設定していない場合に wincred ヘルパーを設定する
        existing_helper = subprocess.run(["git", "config", "--global", "--get", "credential.helper"], capture_output=True, text=True)
        existing_helper_output = existing_helper.stdout.strip()

        # credential.helper が存在しない場合のみ wincred ヘルパーを設定する
        if "wincred" not in existing_helper_output:
            subprocess.run(["git", "config", "--global", "credential.helper", "store"], check=True, capture_output=True)
            print('Gitの認証情報をキャッシュしました')
        else:
            print('Gitの認証情報はすでにキャッシュされています')

    except subprocess.CalledProcessError as e:
        print(f'エラーが発生しました: {e}')

# 関数を実行して認証情報をキャッシュする
cache_git_credentials()




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
    st.title('データ入力、アクセストークンをどうにかした(パスワードをトークンに変更。キャッシ)')

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

            env = os.environ.copy()
            env["GIT_ASKPASS"] = "echo"
            env["GIT_USERNAME"] = GITHUB_ACCESS_TOKEN

            # GitHubのアクセストークンを使用してプッシュ
            subprocess.run(["git", "push", "https://Noi0113:" + GITHUB_ACCESS_TOKEN + "@github.com/Noi0113/Moduletest.git"], check=True)
            
            st.success('データを保存し、GitHubにプッシュしました')
        except subprocess.CalledProcessError as e:
            st.error(f'エラーが発生しました: {e}')
            
if __name__ == '__main__':
    cache_git_credentials()  # Gitの認証情報をキャッシュ
    main()
