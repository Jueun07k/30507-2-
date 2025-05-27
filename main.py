# streamlit_app.py

import streamlit as st
import pandas as pd

# Google Sheets CSV export URL (공개 문서일 경우)
sheet_url = "https://docs.google.com/spreadsheets/d/1TD9qzcDZI4fYc56v2ze_6oEcv7j9Ho0J3sH5_J_FILo/export?format=csv&gid=316915650"

@st.cache_data
def load_data(url):
    return pd.read_csv(url)

df = load_data(sheet_url)

st.title("📊 구글 시트 기반 데이터 대시보드")
st.dataframe(df)
