import streamlit as st
import pandas as pd

if "ID" not in st.session_state:
    st.session_state["ID"] = "Noname"

ID = st.session_state["ID"]
with st.sidebar:
    st.caption(f'{ID}님 접속 중 입니다.')

st.title('공공자전거 위치를 알아봅시다.')

data = pd.read_csv("공공자전거.csv")

data = data.copy().fillna(0)
data['total']=4*(data["LCD"]+data["QR"])+5

color = {'QR':'#37e8eb',
         'LCD':'#ebd637'}
data['color'] = data.copy()['운영방식'].map(color)
data

st.map(data,
       latitude="위도",
       longitude="경도",
       size="total",
       color="color")
