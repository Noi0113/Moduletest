import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

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
input_level = st.selectbox('級を入力してください(必須)',options=['A','B','C','D','E'])

if st.button('Submit'):
    column_number = 1
    column_number2 = 2  # 例として2列目に書き込む
    last_row = len(sheet.col_values(column_number2)) + 1
    sheet.update_cell(last_row, column_number, user_input)
    sheet.update_cell(last_row, column_number2, input_level)
    st.success('Data has been written to Google Sheets!')


data = sheet.get_all_values()
headers = data.pop(0)  # ヘッダーを取得し、データから削除
df = pd.DataFrame(data, columns=headers)

st.write(df)
