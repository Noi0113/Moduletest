import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets認証情報の読み込み
credentials = ServiceAccountCredentials.from_json_keyfile_name('your-credentials.json', ['https://spreadsheets.google.com/feeds'])
gc = gspread.authorize(credentials)

# Google Sheetsのシートを開く
sheet = gc.open('Your Google Sheet Name').sheet1

# Streamlitアプリケーション
st.title('Streamlit Google Sheets Connection')

# Streamlitでの入力
user_input = st.text_input('Enter your information:')

# ボタンがクリックされたらGoogle Sheetsに書き込み
if st.button('Submit'):
    sheet.append_row([user_input])
    st.success('Data has been written to Google Sheets!')
