import streamlit as st
import sqlite3
import subprocess
import os


def parse_ssh_config():
    ssh_config = {}
    config_file_path = os.path.expanduser("~/.ssh/config")
    if os.path.exists(config_file_path):
        with open(config_file_path, "r") as f:
            lines = f.readlines()
            host = None
            for line in lines:
                line = line.strip()
                if line.startswith("Host "):
                    host = line.split()[1]
                    ssh_config[host] = {}
                elif line.startswith("  ") and host:
                    key, value = line.strip().split(maxsplit=1)
                    ssh_config[host][key] = value
    return ssh_config

# SSH設定を取得
ssh_config = parse_ssh_config()

# GitHubのホスト設定が存在するか確認
if "github.com" in ssh_config:
    st.write("GitHubのホスト設定が存在します。")
    st.write("設定内容:", ssh_config["github.com"])
else:
    st.write("GitHubのホスト設定は存在しません。")


# SSHコマンドでconfig情報を取得
result = subprocess.run(["ssh", "-G", "github.com"], capture_output=True, text=True)
ssh_config_output = result.stdout

# config情報を表示
st.write(ssh_config_output)


def parse_ssh_config():
    ssh_config = {}
    config_file_path = os.path.expanduser("~/.ssh/config")
    if os.path.exists(config_file_path):
        with open(config_file_path, "r") as f:
            lines = f.readlines()
            host = None
            for line in lines:
                line = line.strip()
                if line.startswith("Host "):
                    host = line.split()[1]
                    ssh_config[host] = {}
                elif line.startswith("  ") and host:
                    key, value = line.strip().split(maxsplit=1)
                    ssh_config[host][key] = value
    return ssh_config

# SSH設定を取得
ssh_config = parse_ssh_config()

# GitHubのホスト設定が存在するか確認
if "github.com" in ssh_config:
    st.write("SSH config file is being loaded by Python process.")
else:
    st.write("SSH config file is NOT being loaded by Python process.")


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
    st.title('SSHでの認証を試してみる!ディレクトリも')

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
            # ディレクトリパス
            env_directory = 'C:\Users\81907\Moduletest'
            
            # SSHエージェントにSSHキーを追加
            subprocess.run(["ssh-add", "C:\\Users\\81907\\.ssh\\id_rsa"])
            subprocess.run(["git", "add", DATABASE_PATH], check=True)
            subprocess.run(["git", "commit", "-m", "Update test-monketsu.db"], check=True)
            subprocess.run(["git", "push","git@github.com:Noi0113/Moduletest.git"], check=True,cwd=env_directory)

            st.success('データを保存し、GitHubにプッシュしました')
        except subprocess.CalledProcessError as e:
            st.error(f'エラーが発生しました: {e}')

if __name__ == '__main__':
    main()
