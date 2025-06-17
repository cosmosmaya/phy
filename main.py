# philosophy_data.py

philosophy_db = {
    "플라톤": {
        "사상가": "플라톤",
        "시대": "기원전 427년 ~ 기원전 347년",
        "지역": "고대 그리스",
        "개념": "이데아론, 이상국가, 영혼의 삼분설",
        "관련 서적": ["국가", "향연", "파이돈"],
        "설명": "플라톤은 소크라테스의 제자이며 이데아 이론과 이상 국가론으로 유명하다."
    },
    "이데아론": {
        "사상가": "플라톤",
        "시대": "기원전 4세기",
        "지역": "고대 그리스",
        "개념": "이데아는 감각적 세계 너머에 존재하는 참된 실재이다.",
        "관련 서적": ["국가", "파이돈"],
        "설명": "플라톤의 중심 개념 중 하나로, 이데아는 모든 사물의 본질적인 원형이다."
    },
    "실존주의": {
        "사상가": "키르케고르, 하이데거, 사르트르",
        "시대": "19세기 ~ 20세기",
        "지역": "유럽",
        "개념": "실존, 자유, 책임, 불안",
        "관련 서적": ["존재와 시간", "구토", "죽음에 이르는 병"],
        "설명": "실존주의는 인간의 주체적 존재와 자유, 책임을 강조하는 철학 사조이다."
    },
    # 여기에 더 많은 사상가나 이론을 추가할 수 있음
}
# app.py

import streamlit as st
from philosophy_data import philosophy_db

st.set_page_config(page_title="철학 백과", layout="centered")

st.title("🔍 철학 정보 검색 앱")
st.markdown("**사상가, 이론, 개념, 서적 제목 등을 입력하세요.**")

query = st.text_input("검색어를 입력하세요:", "")

if query:
    result = philosophy_db.get(query)
    
    if result:
        st.success(f"🔎 '{query}'에 대한 정보입니다:")
        st.markdown(f"**사상가:** {result['사상가']}")
        st.markdown(f"**시대:** {result['시대']}")
        st.markdown(f"**지역:** {result['지역']}")
        st.markdown(f"**개념:** {result['개념']}")
        st.markdown(f"**관련 서적:** {', '.join(result['관련 서적'])}")
        st.markdown(f"**설명:** {result['설명']}")
    else:
        st.warning(f"'{query}'에 대한 정보를 찾을 수 없습니다. 데이터베이스를 확인해주세요.")

st.markdown("---")
st.caption("© 2025 철학 백과 앱")
