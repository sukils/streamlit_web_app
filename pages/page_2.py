import streamlit as st
from PIL import Image
import pandas as pd
import datetime
import matplotlib.pyplot as plt

with st.form(key='profile_form'):
    name = st.text_input('名前')
    address = st.text_input('住所')

    age_category = st.selectbox(
        '年齢層',
        ('18歳未満', '18歳以上')
    )

    hobby = st.multiselect(
        '趣味',
        ('競馬', '競輪', '麻雀物語', '風俗', '読書', 'プログラム',
         'アニメ', '映画', '釣り', '料理', '全店', '腸捻転', 'NISMO')
    )

    start_date = st.date_input(
        '開始日',
        datetime.date(2022, 2, 2)
    )

    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'ようこそ！{name}さん！{address}に書籍を送りました！！')
        st.text(f'年齢層：{age_category}')
        st.text(f'趣味：{",".join(hobby)}')
