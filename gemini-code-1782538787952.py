import streamlit as st
import re

# 페이지 기본 설정 및 스타일 정의
st.set_page_config(page_title="국어 서논술형 답안 작성 연습", layout="wide", page_icon="✏️")

# 커스텀 CSS: image_5630fe.png 스타일 재현 및 UI 개선
st.markdown("""
    <style>
    /* 제목 및 본문 스타일 */
    .main-title {
        font-size: 2.3rem !important;
        font-weight: 800 !important;
        color: #2C3E50;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        color: #5A626A;
        font-size: 1.05rem;
        line-height: 1.6;
        margin-bottom: 1.8rem;
    }
    
    /* 탭 스타일 조정 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #F8F9FA;
        border: 1px solid #E9ECEF;
        border-radius: 4px 4px 0px 0px;
        padding: 8px 16px;
        font-weight: 600;
        color: #495057;
    }
    .stTabs [aria-selected="true"] {
        background-color: #FFF !important;
        border-top: 3px solid #E74C3C !important;
        color: #E74C3C !important;
    }
    
    /* 지문 박스 스타일 */
    .passage-box {
        background-color: #EBF3FC;
        padding: 18px;
        border-radius: 8px;
        color: #1E3A5F;
        font-size: 1.05rem;
        line-height: 1.6;
        margin-top: 10px;
        margin-bottom: 15px;
    }
    .passage-title {
        font-weight: bold;
        color: #0056B3;
    }
    
    /* <조건> 박스 스타일 */
    .condition-container {
        background-color: #F1F3F5;
        padding: 20px;
        border-radius: 8px;
        margin-top: 15px;
        margin-bottom: 15px;
        border: 1px solid #E2E8F0;
    }
    .condition-title {
        font-weight: bold;
        font-size: 1.05rem;
        color: #212529;
        margin-bottom: 10px;
    }
    .condition-list {
        margin: 0;
        padding-left: 20px;
        line-height: 1.7;
        color: #343A40;
    }
    
    /* 입력 안내 라벨 스타일 */
    .input-label {
        font-size: 1rem;
        font-weight: bold;
        color: #212529;
        margin-top: 15px;
        margin-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# 상단 헤더 UI
st.markdown('<div class="main-title">✏️ [국어] 서·논술형 답안 작성 연습</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">작성한 답안을 입력한 뒤 문제의 조건에 맞게 작성하였는지의 여부를 확인하세요. 수업시간에 배운 내용을 복습할 때 마음이 막막할까봐 만든 자료이므로, 참고로만 활용하세요. 선생님과 수업 시간에 공부한 내용이 답안 작성의 초점이에요 😉</div>', unsafe_allow_html=True)

# 세션 상태 초기화
if "resolved" not in st.session_state:
    st.session_state.resolved = {1: False, 2: False, 3: False}

# 진행 상황바 및 상단 UI 배치
resolved_count = sum(st.session_state.resolved.values())
st.write(f"✅ **완료된 문제: {resolved_count} / 3**")
st.progress(resolved_count / 3)

# 처음부터 다시 풀기 버튼
if st.button("🔄 처음부터 다시 풀기", type="secondary"):
    st.session_state.resolved = {1: False, 2: False, 3: False}
    st.rerun()

st.markdown("---")

# 텍스트 정규화 함수
def normalize(text):
    return re.sub(r'\s+', '', text).strip()

# 문제 탭 레이아웃 설정
tab1, tab2, tab3, tab4 = st.tabs(["문제 1", "문제 2", "문제 3", "📚 복습할 내용"])

# ==============================================================================
# [문제 1] 사회적 촉진과 억제
# ==============================================================================
with tab1:
    st.markdown("## 1️⃣ 상황에 맞는 학습 공간 선택법 — 사회적 촉진과 억제")
    
    st.markdown("""
    <div class="passage-box">
        <span class="passage-title">[대담 지문]</span><br>
        <b>기자</b>: 심리학 용어인 '사회적 촉진'과 '사회적 억제'를 일상생활, 특히 우리의 학습에 어떻게 적용할 수 있을까요?<br>
        <b>전문가</b>: 이 두 가지 개념을 알면 상황에 맞춰 유용하게 활용할 수 있습니다. 예를 들어, 비교적 쉬운 취미 생활이나 큰 노력을 들일 필요가 없는 과제를 할 때는 어떨까요?<br>
        <b>기자</b>: 음, 그냥 집에서 편하게 혼자 하는 게 집중이 잘되지 않을까요?<br>
        <b>전문가</b>: 그렇지 않습니다. 오히려 집에서 혼자 하는 것보다는 커피숍이나 도서관에서 하는 것이 더 효율적일 수 있습니다. 평소 친숙하고 좋아하는 과목이라면 공부 모임을 만들어서 다른 사람들과 함께 공부하는 것도 좋은 방법이죠.<br>
        <b>기자</b>: 그렇다면 어렵고 복잡한 과제를 할 때는 어떻게 해야 하나요?<br>
        <b>전문가</b>: 그럴 때는 반대입니다. 지나치게 어렵거나 도전이 필요한 과제는 충분히 연습하며 익숙해질 때까지 차분하게 혼자 집중하는 시간을 가지는 것이 좋습니다.
    </div>
    """, unsafe_allow_html=True)
    
    # 1번 문항 세트 시작
    st.subheader("[서·논술형 1] 표 빈칸 채우기")
    st.markdown("윗글을 요약하여 정리한 표의 빈칸에 들어갈 내용을 알맞게 찾아 쓰시오.")
    c1, c2, c3 = st.columns(3)
    ans_1_1 = c1.text_input("(1) 어려운 과제와 대비되는 '과제의 특성'", key="1_1")
    ans_1_2 = c2.text_input("(2) 어려운 과제를 해결하기 위한 '효율적인 환경 및 방법'", key="1_2")
    ans_1_3 = c3.text_input("(3) 어려운 과제와 관련된 '심리 현상' 용어", key="1_3")
    
    st.subheader("[서·논술형 2] 조건에 맞춰 설명문 완성하기")
    st.markdown("윗글을 활용하여 '과제 난이도에 따른 효율적인 학습 전략'에 대한 설명문을 작성하려 한다. 주어진 첫 문장('과제의 특성과 난이도에 따라 우리의 학습 효율을 높이는 방법은 다르게 적용되어야 한다.')에 이어지는 내용을 완성하시오.")
    st.markdown("""
    <div class="condition-container">
        <div class="condition-title">〈조건〉</div>
        <ul class="condition-list">
            <li>🎯 서로 다른 2가지의 설명 방법을 사용하여 이어지는 문장을 (1), (2)에 각각 하나씩 작성할 것</li>
            <li>🎯 윗글에 제시된 내용만을 활용하여 문장을 구성할 것 (외부 배경지식 제외)</li>
            <li>🎯 각 문장의 끝에 자신이 사용한 설명 방법의 명칭을 괄호에 넣어 표기할 것 (예: (예시), (대조))</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    c_ans1 = st.text_input("(1) 첫 번째 이어질 문장", key="2_1")
    c_ans2 = st.text_input("(2) 두 번째 이어질 문장", key="2_2")
    
    st.subheader("[서·논술형 3] 영상 기획안 연출 및 효과 작성")
    st.markdown("윗글을 바탕으로 '상황에 맞는 학습 공간 선택법'을 설명하는 영상을 제작할 때, 어려운 과제를 할 때의 [장면 2] 기획안을 완성하시오.")
    st.markdown("""
    <div class="condition-container">
        <div class="condition-title">〈조건〉</div>
        <ul class="condition-list">
            <li>🎯 어려운 과제를 할 때 필요한 환경의 특성이 드러나도록 시각 요소(Ⓐ)와 청각 요소(Ⓑ) 연출 계획을 세울 것</li>
            <li>🎯 자신이 설정한 시각/청각 요소가 글의 내용을 전달하는 데 어떤 효과가 있는지 글의 내용을 근거로 각각 서술할 것</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    ans_3_v = st.text_area("시각 요소(Ⓐ) 및 시각 요소의 효과 서술", key="3_1")
    ans_3_a = st.text_area("청각 요소(Ⓑ) 및 청각 요소의 효과 서술", key="3_2")

    if st.button("문제 1 채점하기", type="primary", key="btn_1"):
        score = 0
        st.markdown("#### 🎯 채점 결과 리포트")
        
        # [서논술 1 채점]
        if ('쉬운' in ans_1_1 or '낮은' in ans_1_1) and ('과제' in ans_1_1 or '취미' in ans_1_1):
            st.success("✅ [서·논술형 1-1] 통과 (과제의 특성 파악 완료)")
            score += 1
        else:
            st.error("❌ [서·논술형 1-1] 오답: 지문의 '비교적 쉬운 취미 생활이나 과제' 내용을 기술해야 합니다.")
            
        if '혼자' in ans_1_2 and ('집중' in ans_1_2 or '차분' in ans_1_2):
            if '도서관' in ans_1_2 or '모임' in ans_1_2:
                st.error("❌ [서·논술형 1-2] 오개념 감점: 어려운 과제 환경에 '모임/도서관' 등 촉진 환경을 혼용했습니다.")
            else:
                st.success("✅ [서·논술형 1-2] 통과 (환경 및 방법 설정 완료)")
                score += 1
        else:
            st.error("❌ [서·논술형 1-2] 오답: '차분하게 혼자 집중하는 시간'의 의미가 포함되어야 합니다.")
            
        if normalize(ans_1_3) == "사회적억제":
            st.success("✅
