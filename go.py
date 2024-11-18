import streamlit as st
import pandas as pd
import time

# 제목과 이미지
st.title("통합 데이터 분석 웹 서비스")
st.image('image.jpg')

# 데이터 불러오기
data = pd.read_csv("members.csv")
data["PW"] = data["PW"].astype(str)
data

# 로그인 폼
with st.form("login_form"):
    ID = st.text_input("ID", placeholder="아이디를 입력하세요")
    PW = st.text_input("Password", type="password", placeholder="비밀번호를 입력하세요")
    submit_button = st.form_submit_button("로그인")

if submit_button:
    if not ID or not PW:
        st.warning("ID와 비밀번호를 모두 입력해주세요.")
    else:
        # 사용자 확인
        user = data[(data["ID"] == ID) & (data["PW"] == str(PW))]
        
        if not user.empty:
            st.success(f"{ID}님 환영합니다!")
            st.session_state["ID"] = ID

            progress_text = "로그인 중입니다."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(1)
            my_bar.empty()

            # 페이지 전환
            st.query_params(page="bike")  # 1. 페이지 전환을 위한 쿼리 파라미터 설정
            st.experimental_user(page="go")  # 2. 앱을 리로드하여 새로운 쿼리 파라미터를 적용

        else:
            st.error("아이디 또는 비밀번호가 일치하지 않습니다.")