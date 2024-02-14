import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# Streamlitアプリケーション
st.title('Streamlit Google Sheets Connection！')

# スコープの設定
scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

# Google Sheets認証情報の読み込み
credentials = ServiceAccountCredentials.from_json_keyfile_name('monketsu2-2b83cfd57ed6.json', ['https://spreadsheets.google.com/feeds'])
gc = gspread.authorize(credentials)

# Google Sheetsのシートを開く
sheet = gc.open('monketsu-for-test').sheet1



# Streamlitでの入力
user_input = st.text_input('Enter your information:')

# ボタンがクリックされたらGoogle Sheetsに書き込み
if st.button('Submit'):
    sheet.append_row([user_input])
    st.success('Data has been written to Google Sheets!')
