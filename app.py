import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="📦 배송 데이터 군집화", layout="wide")
st.title("📦 Delivery 데이터 분석 대시보드")

# ✅ 데이터 로드 함수
@st.cache_data
def load_data():
    try:
        return pd.read_csv("Delivery.csv"), "로컬 파일로부터 불러옴"
    except FileNotFoundError:
        url = "https://drive.google.com/uc?id=1yq6aIqR3sUd1MLrWCTwPDpS6pBFlxpPl"
        try:
            df = pd.read_csv(url)
            return df, "Google Drive로부터 불러옴"
        except Exception as e:
            return None, f"데이터 불러오기 실패: {e}"

# ✅ 데이터 불러오기
df, source_info = load_data()

if df is None:
    st.error("❌ 데이터를 불러올 수 없습니다.")
    st.stop()

st.success(f"✅ 데이터 로드 성공: {source_info}")
st.subheader("📋 데이터 미리보기")
st.dataframe(df, use_container_width=True)

# 📊 군집화 섹션
st.subheader("🔍 KMeans 군집 분석")

# ✅ 수치형 변수 추출
numeric_cols = df.select_dtypes(include='number').columns.tolist()
selected_cols = st.multiselect("군집에 사용할 변수 선택", numeric_cols, default=numeric_cols[:2])

if len(selected_cols) < 2:
    st.warning("⚠️ 최소 2개의 변수는 선택해야 시각화할 수 있습니다.")
    st.stop()

# ✅ 군집 수 설정
k = st.slider("군집 수(K)", min_value=2, max_value=10, value=3)

# ✅ 군집화 수행
try:
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[selected_cols])

    kmeans = KMeans(n_clusters=k, n_init="auto", random_state=42)
    clusters = kmeans.fit_predict(X_scaled)
    df["Cluster"] = clusters

    # ✅ 시각화 (2D)
    fig = px.scatter(
        df,
        x=selected_cols[0],
        y=selected_cols[1],
        color=df["Cluster"].astype(str),
        title=f"KMeans 군집 결과 (K={k})",
        labels={"color": "Cluster"},
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)
except Exception as e:
    st.error(f"❌ 군집화 중 오류 발생: {e}")
