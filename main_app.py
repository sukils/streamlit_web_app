import streamlit as st
from PIL import Image

st.title('すごいアプリにこれからなるやつ')
st.caption('これはこれからすごいことになるはずのテストアプリです。')

image = Image.open('/Users/sunsuki/MEGAsync/業務用/VSCODE/Python/streamlit/test/IMG_1899.jpg')
st.image(image, width=600)