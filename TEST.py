import streamlit as st
import paramiko

st.title('sshtest')
def ssh_and_push():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect('hostname', username='username', password='password')
        st.write("SSH接続成功")
    except paramiko.AuthenticationException:
        st.write("認証エラー: SSH接続失敗")
        return
    except:
        st.write("接続エラー: SSH接続失敗")
        return

    try:
        stdin, stdout, stderr = ssh.exec_command('cd /path/to/your/repo && git add . && git commit -m "your commit message" && git push origin master')
        st.write("gitコマンド実行成功")
    except:
        st.write("gitコマンド実行エラー")

st.button("Push to Git", on_click=ssh_and_push)
