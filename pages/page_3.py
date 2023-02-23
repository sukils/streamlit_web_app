import streamlit as st
from PIL import Image
import pandas as pd
import datetime
import matplotlib.pyplot as plt

df = pd.read_csv(
    'Python/streamlit/sapu_app/data/quantity.csv', encoding='shift_jis')
st.dataframe(df)
#st.table(df)
st.bar_chart(df, y='quantity')

fig, ax = plt.subplots()
ax.plot(df.index, df['quantity'])

st.pyplot(fig)
