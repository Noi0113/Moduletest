import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Streamlitアプリケーション
st.title('Streamlit Google Sheets Connection!')

# スコープの設定（Google Sheets API および Google Drive API のスコープを追加）
scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

# Google Sheets認証情報の読み込み
credentials = ServiceAccountCredentials.from_json_keyfile_name('monketsu2-2b83cfd57ed6.json', scopes)
gc = gspread.authorize(credentials)

# Google Sheetsのシートを開く
sheet = gc.open('monketsu-for-test').sheet1

# Streamlitでの入力
user_input = st.text_input('Enter your information:')

if st.button('Submit'):
    # ここで特定の列にデータを書き込む
    column_number = 5  # 例として2列目に書き込む
    row_index = 3  # 例として2行目に書き込む
    sheet.update_cell(column_number, user_input)
    st.success('Data has been written to Google Sheets!')
