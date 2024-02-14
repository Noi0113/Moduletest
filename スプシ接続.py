import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets認証情報の読み込み
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret_990746109257-2e2kq4bo5vdfr1fe26v2f02v791jfmbl.apps.googleusercontent.com.json', ['https://spreadsheets.google.com/feeds'])
gc = gspread.authorize(credentials)

# Google Sheetsのシートを開く
sheet = gc.open('monketsu-for-test').sheet1

# Streamlitアプリケーション
st.title('Streamlit Google Sheets Connection')

# Streamlitでの入力
user_input = st.text_input('Enter your information:')

# ボタンがクリックされたらGoogle Sheetsに書き込み
if st.button('Submit'):
    sheet.append_row([user_input])
    st.success('Data has been written to Google Sheets!')
