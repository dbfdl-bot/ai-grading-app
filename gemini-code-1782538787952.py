import streamlit as st
import re

# 페이지 기본 설정 및 스타일 정의
st.set_page_config(page_title="국어 서논술형 답안 작성 연습", layout="wide", page_icon="✏️")

# 커스텀 CSS를 통한 UI 디자인 개선
st.markdown("""
    <style>
    .main-title {
        font-size: 2.4rem !important;
        font-weight: 800 !important;
        color: #2C3E50;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        color: #7F8C8D;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #F8F9FA;
        border: 1px solid #E9ECEF;
        border-radius: 4px 4px 0px 0px;
        padding: 10px 20px;
        font-weight: 600;
        color: #495057;
    }
    .stTabs [aria-selected="true"] {
        background-color: #FFF !important;
        border-top: 3px solid #E74C3C !important;
        color: #E74C3C !important;
    }
    .criterion-box {
        background-color: #F1F2F6;
        padding: 15px;
        border-left: 5px solid #2F3542;
        border-radius: 4px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# 상단 헤더 UI
st.markdown('<div class="main-title">✏️ [국어] 서·논술형 답안 작성 연습</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">작성한 답안을 입력한 뒤 문제의 조건에 맞게 작성하였는지의 여부를 확인하세요. 수업 시간에 배운 내용을 복습할 때 참고용으로 활용하세요.</div>', unsafe_allow_html=True)

# 세션 상태 초기화 (진행 상황 체크용)
if "resolved" not in st.session_state:
    st.session_state.resolved = {1: False, 2: False, 3: False}

# 진행 상황바 및 상단 UI 배치
resolved_count = sum(st.session_state.resolved.values())
st.write(f"✅ **완료된 세트: {resolved_count} / 3**")
st.progress(resolved_count / 3)

# 처음부터 다시 풀기 버튼
if st.button("🔄 처음부터 다시 풀기", type="secondary"):
    st.session_state.resolved = {1: False, 2: False, 3: False}
    st.rerun()

st.markdown("---")

# 텍스트 정규화 함수
def normalize(text):
    return re.sub(r'\s+', '', text).strip()

# 이미지에 제시된 문항 전개 방식처럼 탭(Tab) 스타일로 화면 분할
tab1, tab2, tab3, tab4 = st.tabs(["문제 세트 1", "문제 세트 2", "문제 세트 3", "📚 복습할 내용"])

# ==============================================================================
# [탭 1] 세트 1 문항 공간
# ==============================================================================
with tab1:
    st.markdown("### 1️⃣ 경쟁도 없는데 왜 집중이 잘 됐을까? — 사회적 촉진과 억제 [cite: 14]")
    
    with st.expander("📖 [지문 보기 / 숨기기]", expanded=True):
        st.info("""
        **기자**: '사회적 촉진'과 '사회적 억제'를 일상 학습에 어떻게 적용할 수 있을까요? [cite: 15]
        **전문가**: 비교적 쉬운 취미 생활이나 큰 노력을 들일 필요가 없는 과제를 할 때는 커피숍이나 도서관이 더 효율적일 수 있습니다. 공부 모임을 만드는 것도 좋죠. [cite: 17, 19, 20]
        **기자**: 그렇다면 어렵고 복잡한 과제를 할 때는요? [cite: 21]
        **전문가**: 그럴 때는 반대입니다. 지나치게 어렵거나 도전이 필요한 과제는 충분히 연습하며 익숙해질 때까지 차분하게 혼자 집중하는 시간을 가지는 것이 좋습니다. [cite: 22]
        """)
        
    st.markdown("#### [서·논술형 1] 표 빈칸 채우기 [cite: 23]")
    c1, c2, c3 = st.columns(3)
    ans_1_1 = c1.text_input("(1) 어려운 과제와 대비되는 '과제의 특성' [cite: 24]", key="1_1")
    ans_1_2 = c2.text_input("(2) 어려운 과제 해결을 위한 '효율적인 환경 및 방법' [cite: 24]", key="1_2")
    ans_1_3 = c3.text_input("(3) 빈칸에 들어갈 올바른 '심리 현상' 용어 [cite: 24]", key="1_3")
    
    st.markdown("#### [서·논술형 2] 조건에 맞춰 설명문 완성하기 [cite: 29]")
    st.markdown('<div class="criterion-box"><b>[조건]</b> 서로 다른 설명 방법을 활용하여 문장 완성 후 끝에 명칭 표기 (예: (예시), (대조)) [cite: 33, 35]</div>', unsafe_allow_html=True)
    ans_2_1 = st.text_input("첫 번째 이어질 문장 (1) [cite: 36]", key="2_1")
    ans_2_2 = st.text_input("두 번째 이어질 문장 (2) [cite: 37]", key="2_2")
    
    st.markdown("#### [서·논술형 3] 영상 기획안 연출 및 효과 작성 [cite: 39, 40]")
    ans_3_v = st.text_area("시각 요소(Ⓐ) 연출 계획 및 기대 효과 서술 [cite: 55, 56]", key="3_1")
    ans_3_a = st.text_area("청각 요소(Ⓑ) 연출 계획 및 기대 효과 서술 [cite: 57, 58]", key="3_2")

    if st.button("세트 1 채점 및 피드백 받기", type="primary", key="btn_1"):
        score = 0
        st.markdown("#### 🎯 세트 1 채점결과")
        
        if ('쉬운' in ans_1_1 or '낮은' in ans_1_1) and ('과제' in ans_1_1 or '취미' in ans_1_1):
            st.success("✔️ [서·논술형 1-1] 정답! 과제의 특성을 정확히 찾았습니다.")
            score += 1
        else:
            st.error("❌ [서·논술형 1-1] 오답: 지문에서 '비교적 쉬운 취미 생활이나 과제' 부분을 확인하세요. [cite: 17]")
            
        if '혼자' in ans_1_2 and ('집중' in ans_1_2 or '차분' in ans_1_2):
            st.success("✔️ [서·논술형 1-2] 정답! 효율적인 환경 환경을 올바르게 제시했습니다.")
            score += 1
        else:
            st.error("❌ [서·논술형 1-2] 오답: '차분하게 혼자 집중하는 시간'의 의미가 들어가야 합니다. [cite: 22]")
            
        if normalize(ans_1_3) == "사회적억제":
            st.success("✔️ [서·논술형 1-3] 정답! 정확한 용어를 기술했습니다.")
            score += 1
        else:
            st.error("❌ [서·논술형 1-3] 오답: 올바른 심리 용어는 '사회적 억제'입니다. [cite: 15]")
            
        # 설명 방법 검증 부분
        m1 = re.search(r'\(([^)]+)\)', ans_2_1)
        m2 = re.search(r'\(([^)]+)\)', ans_2_2)
        if m1 and m2:
            st.success("✔️ [서·논술형 2] 조건 충족! 설명 방법의 명칭과 형태가 모두 적절합니다.")
            score += 2
        else:
            st.error("❌ [서·논술형 2] 감점: 문장 끝에 괄호를 사용하여 설명 방법 명칭을 적었는지 확인하세요. [cite: 35]")
            
        if ('혼자' in ans_3_v or '독립' in ans_3_v) and ('조용' in ans_3_a or '소음' in ans_3_a):
            st.success("✔️ [서·논술형 3] 정답! 복합양식성의 연출 의도가 훌륭합니다.")
            score += 2
        else:
            st.error("❌ [서·논술형 3] 감점: 어려운 과제 특성에 맞는 '혼자/조용함'의 성격이 시청각에 드러나야 합니다. [cite: 53]")

        if score >= 5:
            st.session_state.resolved[1] = True
            st.balloons()

# ==============================================================================
# [탭 2] 세트 2 문항 공간
# ==============================================================================
with tab2:
    st.markdown("### 2️⃣ 겨울철 불청객의 비밀 — 정전기의 특징 [cite: 60, 61]")
    
    with st.expander("📖 [지문 보기 / 숨기기]"):
        st.info("""
        **전문가**: 정전기란 전하가 정지 상태로 있어 그 분포가 시간적으로 변화하지 않는 전기를 말합니다. 쉽게 말해 흐르지 않고 머물러 있는 전기입니다. [cite: 62, 63]
        실생활에서 쓰는 전기가 '흐르는 물'이라면, 정전기는 '높은 곳에 고여 있는 물'과 같습니다. 전하가 이동하지 않고 머물러 있어 높은 전압에도 위험하지는 않습니다. [cite: 65, 67]
        """)
        
    st.markdown("#### [서·논술형 1] 표 빈칸 채우기 [cite: 69]")
    c1, c2, c3 = st.columns(3)
    ans_2_1_1 = c1.text_input("(1) 정전기의 '물의 상태 비유' [cite: 70]", key="2_1_1")
    ans_2_1_2 = c2.text_input("(2) 정전기의 '전하의 상태' [cite: 70]", key="2_1_2")
    ans_2_1_3 = c3.text_input("(3) 정전기의 '위험성' 여부 [cite: 70]", key="2_1_3")

    st.markdown("#### [서·논술형 2] 논리적 흐름에 따른 설명문 작성 [cite: 74]")
    ans_2_2_1 = st.text_input("이어지는 문장 (1) [cite: 82]", key="2_2_1")
    ans_2_2_2 = st.text_input("이어지는 문장 (2) [cite: 83]", key="2_2_2")

    st.markdown("#### [서·논술형 3] 복합양식성 고려 영상 연출 [cite: 85, 99]")
    ans_2_3_v = st.text_area("시각 요소(Ⓐ) 연출 계획 및 지문 근거 효과 서술 [cite: 102, 103]", key="2_3_v")
    ans_2_3_a = st.text_area("청각 요소(Ⓑ) 연출 계획 및 지문 근거 효과 서술 [cite: 104, 105]", key="2_3_a")

    if st.button("세트 2 채점 및 피드백 받기", type="primary", key="btn_2"):
        score2 = 0
        if '고여' in ans_2_1_1 or '멈춘' in ans_2_1_1:
            st.success("✔️ [서·논술형 1-1] 정답! 정지된 물의 속성을 잘 포착했습니다.")
            score2 += 1
        else:
            st.error("❌ [서·논술형 1-1] 오답: 지문에 제시된 비유인 '고여 있는 물'을 확인하세요. [cite: 65]")
            
        if '이동하지' in ans_2_1_2 or '머물' in ans_2_1_2 or '정지' in ans_2_1_2:
            st.success("✔️ [서·논술형 1-2] 정답! 전하의 상태를 정확하게 작성했습니다.")
            score2 += 1
        else:
            st.error("❌ [서·논술형 1-2] 오답: 전하가 '이동하지 않고 머물러 있음'이 명시되어야 합니다. [cite: 67]")
            
        if '위험하지' in ans_2_1_3 or '안전' in ans_2_1_3:
            st.success("✔️ [서·논술형 1-3] 정답! 위험성에 대한 올바른 결론입니다.")
            score2 += 1
        else:
            st.error("❌ [서·논술형 1-3] 오답: 높은 전압에도 불구하고 '위험하지 않다'가 정답입니다. [cite: 67]")
            
        if '란' in ans_2_2_1 or '말한다' in ans_2_2_1 or '물' in ans_2_2_2:
            st.success("✔️ [서·논술형 2] 정답! 정의와 비교/대조의 설명 방법 특성이 잘 드러납니다.")
            score2 += 2
        else:
            st.error("❌ [서·논술형 2] 감점: 지문의 내용(개념 정의 및 물 비유)을 논리적으로 연결해 주세요. [cite: 62, 65]")

        if ('댐' in ans_2_3_v or '호수' in ans_2_3_v or '고여' in ans_2_3_v) and ('고요' in ans_2_3_a or '침묵' in ans_2_3_a):
            st.success("✔️ [서·논술형 3] 정답! 지문의 내용을 시청각적으로 완벽하게 치환했습니다.")
            score2 += 2
        else:
            st.error("❌ [서·논술형 3] 감점: 실생활 전기의 거센 물소리와 반대되는 정적인 연출이 필요합니다. [cite: 92]")

        if score2 >= 5:
            st.session_state.resolved[2] = True
            st.balloons()

# ==============================================================================
# [탭 3] 세트 3 문항 공간
# ==============================================================================
with tab3:
    st.markdown("### 3️⃣ 알고리즘 초상화와 가치 — 인공지능 그림과 예술 [cite: 107, 108]")
    
    with st.expander("📖 [지문 보기 / 숨기기]"):
        st.info("""
        **전문가**: 인간의 작품에는 작가의 고유한 감정, 철학, 삶의 경험, 세상을 바라보는 관점 등 내외부적인 요소가 종합적으로 담겨 있어 예술입니다. [cite: 114]
        반면 인공 지능은 감정도 느끼지 못하고 독자적인 철학이나 이야기가 없기 때문에 이를 예술로 보기는 어렵습니다. [cite: 115]
        그러나 기존 미술계에 큰 변화를 가져왔고 예술의 범주를 확장할 수 있다는 점에서 상징적인 가치를 지닙니다. [cite: 117, 118]
        """)
        
    st.markdown("#### [서·논술형 1] 표 빈칸 채우기 [cite: 119]")
    c1, c2, c3 = st.columns(3)
    ans_3_1_1 = c1.text_input("(1) 인공지능 그림의 올림픽 경기 비유 [cite: 120]", key="3_1_1")
    ans_3_1_2 = c2.text_input("(2) 인공지능 작품을 예술로 볼 수 있는가(근거 포함) [cite: 120]", key="3_1_2")
    ans_3_1_3 = c3.text_input("(3) 인공지능 예술로서의 상징적 가치 [cite: 120]", key="3_1_3")

    st.markdown("#### [서·논술형 2] 조건에 따른 설명문 작성 [cite: 125]")
    ans_3_2_1 = st.text_input("이어지는 문장 (1) [cite: 130]", key="3_2_1")
    ans_3_2_2 = st.text_input("이어지는 문장 (2) [cite: 131]", key="3_2_2")

    st.markdown("#### [서·논술형 3] 마음에 울림을 주는 진정한 예술 연출 [cite: 137, 146]")
    ans_3_3_v = st.text_area("시각 요소(Ⓐ) 연출 계획 및 지문 근거 효과 서술 [cite: 155, 156]", key="3_3_v")
    ans_3_3_a = st.text_area("청각 요소(Ⓑ) 연출 계획 및 지문 근거 효과 서술 [cite: 157, 158]", key="3_3_a")

    if st.button("세트 3 채점 및 피드백 받기", type="primary", key="btn_3"):
        score3 = 0
        if '로봇' in ans_3_1_1 and '피겨' in ans_3_1_1:
            st.success("✔️ [서·논술형 1-1] 정답! 올림픽 비유 대상을 정확하게 짚어냈습니다.")
            score3 += 1
        else:
            st.error("❌ [서·논술형 1-1] 오답: 지문에 서술된 '로봇의 피겨 스케이팅 연기' 내용을 확인하세요. [cite: 113]")
            
        if ('아니다' in ans_3_1_2 or '어렵다' in ans_3_1_2) and ('감정' in ans_3_1_2 or '철학' in ans_3_1_2):
            st.success("✔️ [서·논술형 1-2] 정답! 예술 판단의 방향성과 핵심 근거를 충족했습니다.")
            score3 += 1
        else:
            st.error("❌ [서·논술형 1-2] 오답: '예술로 보기 어렵다'는 결론과 '감정/철학 부재'라는 지문 속 근거가 들어가야 합니다. [cite: 115]")
            
        if '변화' in ans_3_1_3 or '확장' in ans_3_1_3 or '상징' in ans_3_1_3:
            st.success("✔️ [서·논술형 1-3] 정답! 인공지능 작품의 미술사적 의의를 명확히 기술했습니다.")
            score3 += 1
        else:
            st.error("❌ [서·논술형 1-3] 오답: 지문 후반부의 '미술계 변화' 혹은 '예술 범주 확장' 내용을 참고하세요. [cite: 117, 118]")

        if '감정' in ans_3_2_1 or '철학' in ans_3_2_1 or '반면' in ans_3_2_2:
            st.success("✔️ [서·논술형 2] 정답! 분석과 대조의 설명 방법 구조를 잘 구현했습니다.")
            score3 += 2
        else:
            st.error("❌ [서·논술형 2] 감점: 인간 예술의 다각적 요소(분석)와 AI와의 차이점(대조)이 녹아나야 합니다. [cite: 114, 115]")

        if ('인간' in ans_3_3_v or '선수' in ans_3_3_v) and ('음악' in ans_3_3_a or '환호' in ans_3_3_a):
            st.success("✔️ [서·논술형 3] 정답! 인간 예술의 본질적인 따뜻함과 감동을 효과적으로 나타냈습니다.")
            score3 += 2
        else:
            st.error("❌ [서·논술형 3] 감점: 로봇의 차가운 기계음과 선명한 대조를 이룰 수 있는 인간미 있는 사운드와 역동적 연출이 필요합니다. [cite: 145]")

        if score3 >= 5:
            st.session_state.resolved[3] = True
            st.balloons()

# ==============================================================================
# [탭 4] 복습할 내용 (학습 가이드 요약본)
# ==============================================================================
with tab4:
    st.markdown("### 📚 대단원 핵심 개념 및 학습 가이드 요약")
    st.markdown("서논술형 평가에서 높은 점수를 받기 위해 반드시 숙지해야 할 핵심 설명 방법 개념 요약표입니다. [cite: 3]")
    
    # 핵심 개념 테이블 시각화
    st.table([
        {"설명 방법": "정의", "주요 특징": "대상의 뜻, 개념, 본질을 밝힐 때 주로 사용 [cite: 4]"},
        {"설명 방법": "예시", "주요 특징": "구체적인 사례를 바탕으로 이해를 도울 때 사용 [cite: 4]"},
        {"설명 방법": "분석", "주요 특징": "대상을 구성하는 여러 요소나 부분으로 나누어 설명할 때 사용 [cite: 4]"},
        {"설명 방법": "비교와 대조", "주요 특징": "둘 이상의 대상 간의 공통점과 차이점을 선명하게 드러낼 때 사용 [cite: 4]"},
        {"설명 방법": "분류와 구분", "주요 특징": "일정한 기준에 따라 종류를 묶거나 나눌 때 사용 [cite: 4]"}
    ])
    
    st.markdown("""
    > 💡 **서논술형 감점 예방 Tip!**
    > 1. 문제 조건에서 **'윗글의 내용을 근거로'** 하라고 요구하는 경우, 자신만의 임의적인 상식이나 느낌을 적으면 점수를 받을 수 없습니다. [cite: 34]
    > 2. 영상 기획안과 같은 **복합양식성** 문항은 시각 요소와 청각 요소가 글의 주제를 전달하는 데 유기적으로 어울려야 합니다. [cite: 9, 54]
    """)
