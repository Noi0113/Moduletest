import streamlit as st
import sqlite3

# Streamlitアプリの作成
def app():
    st.title('データベース実験変更版！！！！')
    # データベース接続の作成
    conn = sqlite3.connect('test-monketsu.db')
    c = conn.cursor()

    #c.execute('''
    #CREATE TABLE IF NOT EXISTS TestTable (
    #    user_1 TEXT,
    #    user_2 TEXT
    #    )
    #''')
    #conn.commit()

    # Streamlitのテキスト入力フィールド
    user_input1 = st.text_input("テキストを入力してください")
    user_input2 = st.text_input("テキストを入力してください2")
    # ユーザーが何かを入力した場合、それをデータベースに挿入

    if st.button('送信'):
        c.execute('''
            INSERT INTO TestTable(taikai_name,taikai_password) VALUES (?,?)
        ''', (user_input1,user_input2))
        conn.commit()
        st.success("回答を送信しました！")
    
    
    # データベースからデータを取得して表示
    #c.execute('SELECT taikai_name FROM TestTable WHERE taikai_password = "え"')
    #data = c.fetchall()
    #st.write(data)

    st.subheader("これまでの回答")
    c.execute("SELECT * FROM TestTable")
    rows = c.fetchall()
    for row in rows:
        st.write(f"大会名: {row[0]}, 大会パスワード: {row[1]}")



# Gitコマンドを実行
try:
    # Gitのユーザー情報を設定
    subprocess.check_call(['git', 'config', '--global', 'user.email', 's2110524@u.tsukuba.ac.jp'])
    subprocess.check_call(['git', 'config', '--global', 'user.name', 'KNo0113'])

    # 変更をステージング
    subprocess.check_call(['git', 'add', '--all'])

    # コミット
    subprocess.check_call(['git', 'commit', '-m', 'Update database'])

    # リモートのmainブランチを最新状態にリセット
    subprocess.check_call(['git', 'reset', '--hard', 'origin/main'])

    # 変更を再度ステージング
    subprocess.check_call(['git', 'add', 'test-monketsu.db'])

    # リモートリポジトリの最新情報を取得
    subprocess.check_call(['git', 'fetch', 'origin'])

    # 変更をコミット
    subprocess.check_call(['git', 'commit', '-m', 'Add SQLite database'])

    # リモートリポジトリにプッシュ
    subprocess.check_call(['git', 'push'])

    print("データベースの変更がGit上に反映され、リモートリポジトリにプッシュされました。")
except subprocess.CalledProcessError as e:
    print("エラーが発生しました：", e)


    conn.close()
# Streamlitアプリを実行
if __name__ == "__main__":
    app()


#コードを書き換えるとデータベースの中身失われる…？？っぽいんだけど、リロードだけなら中身保持されてる
