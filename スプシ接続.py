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

# Google Sheetsのシート2を開く
sheet = gc.open('monketsu-karuta').get_worksheet(1)

absent_options = ['第1試合','第2試合','第3試合','第4試合']

# Streamlitでの入力
user_input = st.text_input('Enter your information:')
input_level = st.selectbox('級を入力してください(必須)',options=['A','B','C','D','E'])
absent_matches = st.multiselect('欠席する試合を入力してください(複数選択可)', absent_options)

#休む試合は複数選択のため、リスト化
st.write(absent_matches)

#提出ボタンを押してデータを格納
if st.button('Submit'):
    column_number = 1
    column_number2 = 2  # 例として2列目に書き込む
    last_row = len(sheet.col_values(column_number2)) + 1
    sheet.update_cell(last_row, column_number, user_input)
    sheet.update_cell(last_row, column_number2, input_level)
    #sheet.update_cell(last_row, 3, absent_list[0])
    #sheet.update_cell(last_row, 4, absent_list[0])
    
    st.success('Data has been written to Google Sheets!')


data = sheet.get_all_values()
headers = data.pop(0)  # ヘッダーを取得し、データから削除
df = pd.DataFrame(data, columns=headers)

st.write(df)
