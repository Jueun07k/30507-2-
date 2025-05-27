import streamlit as st
import pandas as pd

st.set_page_config(page_title="📊 구글 시트 대시보드", layout="wide")
st.title("📊 구글 스프레드시트 기반 대시보드")

# 🔗 Google Sheets - CSV 형식 링크
sheet_csv_url = "https://docs.google.com/spreadsheets/d/1TD9qzcDZI4fYc56v2ze_6oEcv7j9Ho0J3sH5_J_FILo/export?format=csv&gid=316915650"

# ✅ 데이터 불러오기 함수 - 캐시 가능하도록 DataFrame만 반환
@st.cache_data
def load_data(url: str) -> pd.DataFrame:
    return pd.read_csv(url)

# ✅ Streamlit 앱 실행
try:
    with st.spinner("데이터 불러오는 중..."):
        df = load_data(sheet_csv_url)

    st.success("✅ 데이터가 성공적으로 불러와졌습니다!")
    st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error("❌ 데이터를 불러오는 데 실패했습니다.")
    st.exception(e)
    st.info("⚠️ 시트를 '공개'로 설정했는지 확인해주세요.\n👉 공유 > '링크가 있는 모든 사용자에게 보기 권한 부여'")
