import streamlit as st
from PIL import Image

st.title('すごいアプリにこれからなるやつ')
st.caption('これはこれからすごいことになるはずのテストアプリです。')

image = Image.open('sapu_app/data/名称未設定のアートワーク.jpg')
st.image(image, width=600)
