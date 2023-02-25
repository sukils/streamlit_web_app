import streamlit as st
from PIL import Image

st.title('すごいアプリにこれからなるやつ')
st.caption('これはこれからすごいことになるはずのテストアプリです。')

image = Image.open('/Users/sunsuki/python/streamlit/sapu_app/data/noname001.jpg')
st.image(image, width=600)
