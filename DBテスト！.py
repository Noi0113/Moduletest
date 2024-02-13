import streamlit as st
import sqlite3
import subprocess

# SQLite3データベースファイルのパス
DATABASE_PATH = 'test-monketsu.db'

# Gitのユーザー情報を設定する
GIT_USER_EMAIL = 's2110524@u.tsukuba.ac.jp'
GIT_USER_NAME = 'Noi0113'

# SQLite3データベースに接続
conn = sqlite3.connect(DATABASE_PATH)
c = conn.cursor()

# テーブルが存在しない場合は作成
c.execute('''CREATE TABLE IF NOT EXISTS your_table_name (
             column1 TEXT,
             column2 TEXT
             )''')

# Streamlitアプリケーション
def main():
    st.title('SSHでの認証を試してみる')

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
            subprocess.run(["git", "add", DATABASE_PATH], check=True)
            subprocess.run(["git", "commit", "-m", "Update test-monketsu.db"], check=True)
            subprocess.run(["git", "push"], check=True)

            st.success('データを保存し、GitHubにプッシュしました')
        except subprocess.CalledProcessError as e:
            st.error(f'エラーが発生しました: {e}')

if __name__ == '__main__':
    main()
