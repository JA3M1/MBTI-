import time
import streamlit as st

# 1. 페이지 설정 (와이드 모드)
st.set_page_config(
    page_title="🌟 MBTI 찰떡 진로 대탐험! 🚀",
    page_icon="🦄",
    layout="wide",
)

# 2. 화려한 CSS 스타일링 적용 (글로우 효과, 형색빛깔 배경 등)
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .stButton>button {
        background: linear-gradient(45deg, #FF4B2B, #FF416C);
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 30px;
        padding: 15px 30px;
        border: none;
        box-shadow: 0px 5px 15px rgba(255, 75, 43, 0.4);
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0px 8px 20px rgba(255, 65, 108, 0.6);
    }
    .card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 3. MBTI별 진로 데이터베이스 (이모지 폭탄 💥)
mbti_data = {
    "INTJ": {
        "title": "🧠 용의주도한 전략가",
        "emoji": "👑🔭",
        "jobs": [
            "데이터 과학자 📊",
            "전략 컨설턴트 ♟️",
            "소프트웨어 아키텍트 💻",
            "교수/연구원 🔬",
        ],
        "advice": "당신의 철저한 계획력과 통찰력은 세상을 바꿀 거대한 프로젝트를 성공으로 이끌 거예요! 힘내세요! ✨",
    },
    "ENFP": {
        "title": "🌟 재기발랄한 활동가",
        "emoji": "🎉🦄",
        "jobs": [
            "크리에이터/유튜버 🎥",
            "마케터/홍보 전문가 📢",
            "이벤트 플래너 🎈",
            "상담사/심리학자 💖",
        ],
        "advice": "무한한 아이디어와 에너지는 사람들을 매료시키는 최고의 무기랍니다! 세상을 더 즐겁게 만들어주세요! 🌈",
    },
    "ISTP": {
        "title": "🔧 만능 재주꾼",
        "emoji": "🛠️🏎️",
        "jobs": [
            "엔지니어/기술자 ⚙️",
            "파일럿/항해사 ✈️",
            "응급구조사 🚑",
            "금융 분석가 📈",
        ],
        "advice": "문제 상황이 닥쳤을 때 가장 냉정하게 해결책을 찾아내는 멋진 실력가예요! 당신의 손끝에서 혁신이 일어납니다! 💡",
    },
    "ENFJ": {
        "title": "🔥 정의로운 사회운동가",
        "emoji": "🏆🤝",
        "jobs": [
            "교사/교육 전문가 📚",
            "외교관/인권 운동가 🌍",
            "인사(HR) 매니저 👥",
            "아나운서/방송인 🎤",
        ],
        "advice": "따뜻한 공감 능력과 리더십으로 주변 사람들을 환하게 빛내주는 천상의 리더예요! 🌟",
    },
    # 다른 MBTI들도 이와 같은 형식으로 확장 가능합니다! (기본 예시용으로 대표 4가지 수록)
}

# 4. 사이드바 - MBTI 선택 구역
st.sidebar.markdown("# 🎨 진로 탐색 메뉴")
st.sidebar.markdown("---")
selected_mbti = st.sidebar.selectbox(
    "👇 당신의 MBTI를 선택해주세요!", list(mbti_data.keys())
)
st.sidebar.markdown("---")
st.sidebar.info("💡 팁: 나뿐만 아니라 친구나 가족의 MBTI도 검색해 보세요! 🎁")

# 5. 메인 화면 구성
st.markdown(
    "<h1 style='text-align: center; color: #FF4B2B;'>🌈✨ 반짝반짝 MBTI 맞춤형 진로 대탐험 🚀💎</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h4 style='text-align: center; color: #555;'>나의 타고난 성향을 알고, 세상에 단 하나뿐인 꿈을 찾아 떠나요! 🗺️💖</h4>",
    unsafe_allow_html=True,
)
st.markdown("---")

# 6. 결과 출력 버튼 및 인터랙션
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    analyze_button = st.button("🔮 찰떡 직업 대공개 버튼 팡팡! 🎉")

if analyze_button:
    # 로딩 바 효과 (화려함 극대화)
    with st.spinner("✨ 우주 에너지를 모아서 맞춤형 직업을 분석 중입니다... ⏳"):
        time.sleep(1.2)

    # 폭죽 애니메이션 터트리기! 🎇
    st.balloons()

    # 선택된 MBTI 정보 가져오기 (만약 데이터에 없는 경우 기본값 처리)
    info = mbti_data.get(
        selected_mbti,
        {
            "title": "✨ 멋진 탐험가",
            "emoji": "🌟🚀",
            "jobs": ["전문가 💼", "기획자 📋", "리더 👑", "예술가 🎨"],
            "advice": "당신만의 독특한 매력으로 세상에서 빛나는 별이 될 거예요! 화이팅! 💖",
        },
    )

    # 결과 카드 출력
    st.markdown(
        f"""
        <div class="card">
            <h2 style='text-align: center; color: #333;'>{info['emoji']} 선택된 MBTI: <span style='color: #FF416C;'>{selected_mbti}</span></h2>
            <h3 style='text-align: center; color: #666;'>({info['title']})</h3>
            <hr>
            <h4 style='color: #FF4B2B;'>💼 추천 찰떡 직업 TOP 4</h4>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # 직업 목록을 예쁘게 컬럼으로 배치
    job_cols = st.columns(2)
    for idx, job in enumerate(info["jobs"]):
        with job_cols[idx % 2]:
            st.success(f"**{idx+1}. {job}**")

    # 조언 박스
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div style='background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%); padding: 25px; border-radius: 15px; text-align: center;'>
            <h3 style='color: #fff; text-shadow: 1px 1px 2px rgba(0,0,0,0.2);'>💌 진로 코칭 마법의 메시지</h3>
            <p style='font-size: 18px; color: #fff; font-weight: bold;'>{info['advice']}</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

else:
    # 초기 안내 화면
    st.markdown(
        """
        <div style='text-align: center; padding: 50px;'>
            <h3>👈 왼쪽 사이드바에서 본인의 <b>MBTI</b>를 고르고 버튼을 눌러보세요!</h3>
            <p style='font-size: 50px;'>👇🦄🔮✨💖</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

# 7. 푸터 장식
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #888;'>✨ Made with ❤️ for Dreamers & Explorers 🚀</p>",
    unsafe_allow_html=True,
)
