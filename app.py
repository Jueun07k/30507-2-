import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="📦 배송 데이터 시각화", layout="wide")
st.title("📦 Delivery 데이터 Plotly 대시보드")

# ✅ CSV 파일 읽기
@st.cache_data
def load_data():
    return pd.read_csv("Delivery.csv")

df = load_data()

# ✅ 데이터 미리보기
st.subheader("📋 데이터 미리보기")
st.dataframe(df, use_container_width=True)

# ✅ 컬럼 목록 추출
numeric_cols = df.select_dtypes(include='number').columns.tolist()
categorical_cols = df.select_dtypes(include='object').columns.tolist()

# ✅ 사용자 선택 시각화
st.subheader("📈 사용자 정의 Plotly 시각화")

x_axis = st.selectbox("X축 선택", numeric_cols)
y_axis = st.selectbox("Y축 선택", numeric_cols, index=1 if len(numeric_cols) > 1 else 0)
color = st.selectbox("색상 기준 컬럼 선택 (선택사항)", categorical_cols + ["(없음)"])

if x_axis and y_axis:
    fig = px.scatter(
        df,
        x=x_axis,
        y=y_axis,
        color=color if color != "(없음)" else None,
        title=f"{x_axis} vs {y_axis}",
        size=y_axis if y_axis != x_axis else None,
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)
