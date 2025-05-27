import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="📦 배송 데이터 시각화", layout="wide")
st.title("📦 Delivery 데이터 Plotly 대시보드")

# ✅ 데이터 로드 함수
@st.cache_data
def load_data():
    try:
        # 1. 로컬 파일이 있으면 그것 사용
        return pd.read_csv("Delivery.csv"), "로컬 파일로부터 불러옴"
    except FileNotFoundError:
        # 2. 없으면 Google Drive에서 다운로드 링크로 불러오기
        url = "https://drive.google.com/uc?id=1yq6aIqR3sUd1MLrWCTwPDpS6pBFlxpPl"
        try:
            df = pd.read_csv(url)
            return df, "Google Drive로부터 불러옴"
        except Exception as e:
            return None, f"데이터 불러오기 실패: {e}"

# ✅ 데이터 불러오기 시도
df, source_info = load_data()

# ✅ 오류 처리
if df is None:
    st.error("❌ 데이터를 불러올 수 없습니다. 파일 경로나 공유 링크를 확인하세요.")
else:
    st.success(f"✅ 데이터 로드 성공: {source_info}")
    
    # 📋 데이터 미리보기
    st.subheader("📋 데이터 미리보기")
    st.dataframe(df, use_container_width=True)

    # 📊 시각화 섹션
    st.subheader("📈 사용자 정의 Plotly 시각화")

    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    categorical_cols = df.select_dtypes(include='object').columns.tolist()

    x_axis = st.selectbox("X축 선택", numeric_cols)
    y_axis = st.selectbox("Y축 선택", numeric_cols, index=1 if len(numeric_cols) > 1 else 0)
    color = st.selectbox("색상 기준 컬럼 (선택)", categorical_cols + ["(없음)"])

    if x_axis and y_axis:
        fig = px.scatter(
            df,
            x=x_axis,
            y=y_axis,
            color=color if color != "(없음)" else None,
            title=f"{x_axis} vs {y_axis}",
            template="plotly_white"
        )
        st.plotly_chart(fig, use_container_width=True)
