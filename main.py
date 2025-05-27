import streamlit as st
import pandas as pd

st.set_page_config(page_title="📊 구글 시트 대시보드", layout="wide")
st.title("📊 구글 스프레드시트 기반 대시보드")

# 🔗 Google Sheets - CSV 형식 링크
sheet_csv_url = "https://docs.google.com/spreadsheets/d/1TD9qzcDZI4fYc56v2ze_6oEcv7j9Ho0J3sH5_J_FILo/export?format=csv&gid=316915650"

# ✅ 데이터 불러오기 함수
@st.cache_data
def load_data(url):
    try:
        df = pd.read_csv(url)
        return df, None
    except Exception as e:
        return None, e

# ✅ 데이터 불러오기
with st.spinner("데이터 불러오는 중..."):
    df, error = load_data(sheet_csv_url)

# ✅ 결과 출력
if error:
    st.error(f"❌ 데이터를 불러오는 데 실패했습니다:\n\n{error}")
    st.info("⚠️ 시트를 '공개'로 설정했는지 확인해주세요.\n\n👉 공유 > '링크가 있는 모든 사용자에게 보기 권한 부여'")
else:
    st.success("✅ 데이터가 성공적으로 불러와졌습니다!")
    st.dataframe(df, use_container_width=True)
