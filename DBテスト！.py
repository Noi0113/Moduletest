import streamlit as st
import sqlite3
import subprocess
# SSHの設定を表示
result = subprocess.run(["ssh", "-G", "github.com"], capture_output=True, text=True)
ssh_config = result.stdout

# ~/.ssh/configファイルが読み込まれているかを確認
if "Host github.com" in ssh_config:
    print("SSH config file is being loaded by Python process.")
else:
    print("SSH config file is NOT being loaded by Python process.")


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
    st.title('SSHでの認証を試してみる!')

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
            # SSHエージェントにSSHキーを追加
            subprocess.run(["ssh-add", "C:\\Users\\81907\\.ssh\\id_rsa"])
            subprocess.run(["git", "add", DATABASE_PATH], check=True)
            subprocess.run(["git", "commit", "-m", "Update test-monketsu.db"], check=True)
            subprocess.run(["git", "push","git@github.com:Noi0113/Moduletest.git"], check=True)

            st.success('データを保存し、GitHubにプッシュしました')
        except subprocess.CalledProcessError as e:
            st.error(f'エラーが発生しました: {e}')

if __name__ == '__main__':
    main()
