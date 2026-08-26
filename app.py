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

# 3. 16가지 MBTI 전체 진로 데이터베이스 (이모지 폭탄 💥)
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
    "INTP": {
        "title": "💡 논리적인 사색가",
        "emoji": "🧪🔮",
        "jobs": [
            "인공지능(AI) 연구원 🤖",
            "보안 전문가 🔒",
            "철학자/작가 ✍️",
            "시스템 분석가 📊",
        ],
        "advice": "끝없는 호기심과 독창적인 논리로 세상의 비밀을 파헤치는 멋진 지식 탐험가입니다! 🌌",
    },
    "ENTJ": {
        "title": "🔥 대담한 통솔자",
        "emoji": "🏆🦁",
        "jobs": [
            "기업 CEO/창업가 💼",
            "경영 컨설턴트 📈",
            "변호사 ⚖️",
            "투자 뱅커 💰",
        ],
        "advice": "카리스마와 효율적인 리더십으로 목표를 향해 거침없이 질주하는 최고의 승부사예요! 🚀",
    },
    "ENTP": {
        "title": "⚡ 뜨거운 논쟁을 즐기는 변론가",
        "emoji": "🌪️🎤",
        "jobs": [
            "크리에이티브 디렉터 🎨",
            "스타트업 기획자 🚀",
            "마케터 📢",
            "방송 PD 🎬",
        ],
        "advice": "지루한 것은 1분도 못 참는 천재적인 아이디어 뱅크! 세상을 유쾌하게 뒤집어주세요! 🎈",
    },
    "INFJ": {
        "title": "✨ 통찰력 있는 선구자",
        "emoji": "🌙🦄",
        "jobs": [
            "상담심리사 💖",
            "작가/시인 📖",
            "사회운동가 🌍",
            "예술가/디자이너 🎨",
        ],
        "advice": "깊은 공감 능력과 이상향을 향한 열정으로 사람들의 마음을 치유하는 따뜻한 별이에요! 🌟",
    },
    "INFP": {
        "title": "🌸 열정적인 중재자",
        "emoji": "🧚‍♀️🎨",
        "jobs": [
            "동화작가 📚",
            "일러스트레이터 🖌️",
            "비영리단체(NGO) 활동가 🕊️",
            "심리 상담사 🌱",
        ],
        "advice": "내면의 아름다운 감성과 따뜻한 가치관으로 세상을 포근하게 물들이는 감성 천사! 💌",
    },
    "ENFJ": {
        "title": "🏆 정의로운 사회운동가",
        "emoji": "🤝🌟",
        "jobs": [
            "교사/교육 전문가 📚",
            "외교관/국제기구 종사자 🌐",
            "인사(HR) 매니저 👥",
            "아나운서 🎤",
        ],
        "advice": "따뜻한 공감 능력과 긍정적인 에너지로 모두를 이끄는 천상의 리더이자 비타민! 💖",
    },
    "ENFP": {
        "title": "🎉 재기발랄한 활동가",
        "emoji": "🌈🎈",
        "jobs": [
            "유튜버/크리에이터 🎥",
            "이벤트 플래너 🎉",
            "여행 작가 ✈️",
            "카피라이터 ✍️",
        ],
        "advice": "무한한 에너지와 창의력으로 어디를 가나 웃음꽃을 피우는 매력 만점 비타민이에요! 🦄",
    },
    "ISTJ": {
        "title": "🛡️ 청렴결백한 논리주의자",
        "emoji": "📋⚓",
        "jobs": [
            "회계사/세무사 💳",
            "법률가/공무원 🏛️",
            "데이터 관리자 🗂️",
            "의공학자 🩺",
        ],
        "advice": "철저한 책임감과 신뢰도로 조직의 든든한 기둥이 되어주는 믿음직한 멋쟁이! 💎",
    },
    "ISFJ": {
        "title": "🌿 임금님 뒷편의 권력자",
        "emoji": "🧸☕",
        "jobs": [
            "간호사/보건 의료인 🏥",
            "초등학교 교사 🍎",
            "사회복지사 🤝",
            "큐레이터/사서 🏛️",
        ],
        "advice": "세심한 배려와 헌신적인 사랑으로 주변을 안전하고 따뜻하게 감싸주는 천사 같은 수호자! 🌸",
    },
    "ESTJ": {
        "title": "📊 엄격한 관리자",
        "emoji": "👔📈",
        "jobs": [
            "기업 임원/CEO 🏢",
            "프로젝트 매니저(PM) 🗂️",
            "군인/경찰관 👮‍♂️",
            "재무 설계사 💰",
        ],
        "advice": "뛰어난 조직력과 결단력으로 무엇이든 확실하게 해내는 든든한 추진력의 대명사! ⚡",
    },
    "ESFJ": {
        "title": "💖 사교적인 외교관",
        "emoji": "🥳🍰",
        "jobs": [
            "승무원/호텔리어 ✈️",
            "이벤트/웨딩 플래너 💐",
            "홍보/마케팅 전문가 📢",
            "상담사 🗣️",
        ],
        "advice": "넘치는 친화력과 배려심으로 언제나 사람들을 웃게 만드는 무대의 분위기 메이커! 🌟",
    },
    "ISTP": {
        "title": "🔧 만능 재주꾼",
        "emoji": "🛠️🏎️",
        "jobs": [
            "기계/소프트웨어 엔지니어 💻",
            "파일럿/항해사 ✈️",
            "응급구조사 🚑",
            "금융 분석가 📈",
        ],
        "advice": "위기 상황에서도 당황하지 않고 냉철하게 해결책을 찾아내는 최고의 실력가! ⚙️",
    },
    "ISFP": {
        "title": "🎨 호기심 많은 예술가",
        "emoji": "🌸🎧",
        "jobs": [
            "패션 디자이너 👗",
            "인테리어 디자이너 🛋️",
            "음악가/프로듀서 🎵",
            "수의사/동물 조련사 🐾",
        ],
        "advice": "섬세한 감각과 따뜻한 마음으로 세상의 아름다움을 포착해 내는 감성 아티스트! 🎨",
    },
    "ESTP": {
        "title": "🏄‍♂️ 모험을 즐기는 사업가",
        "emoji": "🔥🛹",
        "jobs": [
            "스포츠 선수/지도자 ⚽",
            "영업/세일즈 전문가 💼",
            "소방관 🚒",
            "연예인/방송인 🎤",
        ],
        "advice": "도전을 두려워하지 않는 과감함과 특유의 재치로 세상을 흥미진진하게 만드는 개구쟁이! 🚀",
    },
    "ESFP": {
        "title": "💃 자유로운 영혼의 연예인",
        "emoji": "✨🎤",
        "jobs": [
            "배우/엔터테이너 🎭",
            "쇼호스트/인플루언서 📸",
            "안무가/댄서 💃",
            "여행 가이드 🗺️",
        ],
        "advice": "있는 그대로의 자신을 사랑하며 어디서나 환한 빛을 발하는 반짝반짝 스타! 🌟",
    },
}

# 4. 사이드바 - MBTI 선택 구역
st.sidebar.markdown("# 🎨 진로 탐색 메뉴")
st.sidebar.markdown("---")
selected_mbti = st.sidebar.selectbox(
    "👇 당신의 MBTI를 선택해주세요!", list(mbti_data.keys())
)
st.sidebar.markdown("---")
st.sidebar.info("💡 팁: 친구, 가족, 선생님의 MBTI도 검색해 보세요! 🎁")

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
        time.sleep(1.0)

    # 폭죽 애니메이션 터트리기! 🎇
    st.balloons()

    # 선택된 MBTI 정보 가져오기
    info = mbti_data[selected_mbti]

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
