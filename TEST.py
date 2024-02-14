import streamlit as st
import paramiko

import os


# ユーザーのホームディレクトリからの相対パスを絶対パスに変換
#private_key_path = os.path.expanduser(r'C:\Users\81907\.ssh\id_rsa')
private_key_path = r'C:\Users\81907\.ssh\id_rsa'

# 秘密鍵ファイルが存在するか確認
if os.path.exists(private_key_path):
    st.write("秘密鍵ファイルが見つかりました:", private_key_path)
else:
    st.write("秘密鍵ファイルが見つかりませんでした。")


# 秘密鍵ファイルの相対パス
relative_path = '.ssh/id_rsa'

# 秘密鍵ファイルの絶対パスを取得
absolute_path = os.path.abspath(relative_path)

st.write("絶対パス:", absolute_path)


# 秘密鍵のパス
PRIVATE_KEY_PATH = "/mount/src/moduletest/.ssh/id_rsa"


# SSH接続を試みる関数
def test_ssh_connection(hostname, username, private_key_path):
    try:
        # SSHクライアントの作成
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # SSH秘密鍵の設定
        ssh.connect(hostname, username=username, key_filename=private_key_path, timeout=5)
        
        # 接続が成功したことを出力
        st.success('SSH接続に成功しました')
        
        # SSHセッションを閉じる
        ssh.close()
    except Exception as e:
        # 接続が失敗したことを出力
        st.error(f'SSH接続に失敗しました: {e}')

# Streamlitアプリケーション
def main():
    st.title('SSH接続テスト？')
    
    # SSH接続を試みるボタン
    if st.button('SSH接続をテストする'):
        test_ssh_connection('github.com', 'Noi0113', PRIVATE_KEY_PATH)

if __name__ == '__main__':
    main()
