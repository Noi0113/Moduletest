import streamlit as st
import paramiko
import os

# SSH接続を試みる関数
def test_ssh_connection(hostname, username):
    try:
        # SSHクライアントの作成
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # SSH接続
        ssh.connect(hostname, username=username)
        
        # 接続が成功したことを出力
        st.success('SSH接続に成功しました')
        
        # SSHセッションを閉じる
        ssh.close()
    except Exception as e:
        # 接続が失敗したことを出力
        st.error(f'SSH接続に失敗しました: {e}')

# Streamlitアプリケーション
def main():
    st.title('SSH接続テスト！！！！')

    # SSH接続を試みるボタン
    if st.button('SSH接続をテストする'):
        # ローカルのSSHエージェントを利用してSSH接続を試みる
        try:
            os.system('ssh-add')  # SSHエージェントに鍵を追加
            test_ssh_connection('example.com', 'your_username')
        except Exception as e:
            st.error(f'SSH接続に失敗しました: {e}')

if __name__ == '__main__':
    main()
