import streamlit as st
import paramiko

# 秘密鍵のパス
PRIVATE_KEY_PATH = r"C:\Users\81907\.ssh\id_rsa"


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
    st.title('SSH接続テスト！？')
    
    # SSH接続を試みるボタン
    if st.button('SSH接続をテストする'):
        test_ssh_connection('github.com', 'Kno0113', PRIVATE_KEY_PATH)

if __name__ == '__main__':
    main()
