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
    
    st.markdown("### 문항 1")
    st.markdown("윗글을 요약하여 표로 정리하였다. ㄱ~ㄷ에 들어갈 내용을 찾아 쓰시오.")
    c1, c2, c3 = st.columns(3)
    ans_1_1 = c1.text_input("(1) ㄱ:", key="1_1")
    ans_1_2 = c2.text_input("(2) ㄴ:", key="1_2")
    ans_1_3 = c3.text_input("(3) ㄷ:", key="1_3")
    
    st.markdown("### 문항 2")
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
    
    st.markdown('<div class="input-label">• 답안 입력</div>', unsafe_allow_html=True)
    c_ans1 = st.text_input("(1)", key="2_1", placeholder="첫 번째 문장을 입력하세요.")
    c_ans2 = st.text_input("(2)", key="2_2", placeholder="두 번째 문장을 입력하세요.")
    
    st.markdown("### 문항 3")
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
    
    st.markdown('<div class="input-label">• 답안 입력</div>', unsafe_allow_html=True)
    ans_3_v = st.text_area("(1) 시각 요소(Ⓐ) 및 효과", key="3_1")
    ans_3_a = st.text_area("(2) 청각 요소(Ⓑ) 및 효과", key="3_2")

    if st.button("문제 1 채점하기", type="primary", key="btn_1"):
        score = 0
        st.markdown("#### 🎯 채점 결과 리포트")
        
        if ('쉬운' in ans_1_1 or '낮은' in ans_1_1) and ('과제' in ans_1_1 or '취미' in ans_1_1):
            st.success("✅ 문항 1 - (1) ㄱ 통과")
            score += 1
        else:
            st.error("❌ 문항 1 - (1) ㄱ 오답: 지문의 '비교적 쉬운 취미 생활이나 과제' 내용을 요약해 주세요.")
            
        if '혼자' in ans_1_2 and ('집중' in ans_1_2 or '차분' in ans_1_2):
            if '도서관' in ans_1_2 or '모임' in ans_1_2:
                st.error("❌ 문항 1 - (2) ㄴ 오개념 발견: 어려운 과제 환경에 도서관, 모임의 속성을 잘못 부여했습니다.")
            else:
                st.success("✅ 문항 1 - (2) ㄴ 통과")
                score += 1
        else:
            st.error("❌ 문항 1 - (2) ㄴ 오답: '차분하게 혼자 집중하는 시간'의 의미가 포함되어야 합니다.")
            
        if normalize(ans_1_3) == "사회적억제":
            st.success("✅ 문항 1 - (3) ㄷ 통과")
            score += 1
        else:
            st.error("❌ 문항 1 - (3) ㄷ 오답: 정확한 고유 용어인 '사회적 억제'를 적어야 합니다.")
            
        m1 = re.search(r'\(([^)]+)\)', c_ans1)
        m2 = re.search(r'\(([^)]+)\)', c_ans2)
        if m1 and m2:
            st.success("✅ 문항 2 통과 (설명 방법 표기 조건 충족)")
            score += 1
        else:
            st.error("❌ 문항 2 미흡: 문장 끝에 활용한 설명 방법 명칭을 괄호 기호 안에 명시하세요.")
            
        if ('혼자' in ans_3_v or '독립' in ans_3_v) and ('조용' in ans_3_a or '소음' in ans_3_a) and ('효과' in ans_3_v and '효과' in ans_3_a):
            st.success("✅ 문항 3 통과 (시청각 연출 계획 및 근거 효과 완비)")
            score += 1
        else:
            st.error("❌ 문항 3 미흡: 어려운 과제의 특성을 반영한 시청각 연출 및 이에 따른 기대 효과가 명시되어야 합니다.")

        if score == 5:
            st.session_state.resolved[1] = True
            st.balloons()

# ==============================================================================
# [문제 2] 정전기의 특징
# ==============================================================================
with tab2:
    st.markdown("## 2️⃣ 겨울철 불청객의 비밀 — 정전기의 특징")
    
    st.markdown("""
    <div class="passage-box">
        <span class="passage-title">[대담 지문]</span><br>
        <b>기자</b>: 겨울철 불청객인 '정전기'란 정확히 무엇인지 설명 부탁드립니다.<br>
        <b>전문가</b>: 정전기란 전하가 정지 상태로 있어 그 분포가 시간적으로 변화하지 않는 전기, 그리고 그로 인한 전기 현상을 말합니다. 쉽게 설명하면 흐르지 않고 머물러 있는 전기라고 해서 "움직이지 아니하여 조용하다."는 뜻을 가진 한자 '정(靜)'을 써서 정전기라고 부르는 것이죠.<br>
        <b>기자</b>: 우리가 실생활에서 쓰는 전기와는 어떻게 다른가요? 물에 비유해서 설명해 주시면 이해가 쉬울 것 같습니다.<br>
        <b>전문가</b>: 아주 좋은 비유가 될 수 있습니다. 우리가 실생활에서 쓰는 전기가 '흐르는 물'이라면, 정전기는 '높은 곳에 고여 있는 물'이라고 할 수 있습니다.<br>
        <b>기자</b>: 정전기가 일어날 때 찌릿한 느낌이 드는데, 혹시 위험하지는 않은가요?<br>
        <b>전문가</b>: 정전기의 전압은 매우 높지만, 우리가 실생활에서 쓰는 전기와는 다르게 전하가 이동하지 않고 머물러 있어 위험하지는 않습니다. 어마어마하게 높은 곳에 고여 있는 물이지만 떨어지지 않고 있어서 별 피해가 없는 것과 같다고 이해하시면 됩니다.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 문항 1")
    st.markdown("윗글을 요약하여 표로 정리하였다. ㄱ~ㄷ에 들어갈 내용을 찾아 쓰시오.")
    c1, c2, c3 = st.columns(3)
    ans_2_1_1 = c1.text_input("(1) ㄱ:", key="2_1_1")
    ans_2_1_2 = c2.text_input("(2) ㄴ:", key="2_1_2")
    ans_2_1_3 = c3.text_input("(3) ㄷ:", key="2_1_3")

    st.markdown("### 문항 2")
    st.markdown("윗글을 활용하여 '정전기의 특징'에 대한 설명문을 작성하려 한다. 주어진 첫 문장('겨울철에 흔히 겪는 정전기는 우리가 평소 집에서 사용하는 전기와는 다른 뚜렷한 특징이 있다.')에 이어지는 내용을 완성하시오.")
    st.markdown("""
    <div class="condition-container">
        <div class="condition-title">〈조건〉</div>
        <ul class="condition-list">
            <li>🎯 주어진 문장에 이어지는 문장을 (1), (2)에 각각 하나씩 작성할 것</li>
            <li>🎯 (1)과 (2)에는 서로 다른 설명 방법이 1가지 이상 활용되어야 하며, 각 문장의 끝에 설명 방법의 명칭을 괄호에 넣어 기재할 것</li>
            <li>🎯 윗글에 제시된 내용만을 활용하고, 두 문장이 논리적 흐름을 갖고 이어지도록 서술할 것</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="input-label">• 답안 입력</div>', unsafe_allow_html=True)
    ans_2_2_1 = st.text_input("(1)", key="2_2_1")
    ans_2_2_2 = st.text_input("(2)", key="2_2_2")

    st.markdown("### 문항 3")
    st.markdown("윗글을 바탕으로 '정전기의 특징'을 설명하는 영상 기획안 중, [장면 2] 정전기(고여 있는 물) 부분을 완성하시오.")
    st.markdown("""
    <div class="condition-container">
        <div class="condition-title">〈조건〉</div>
        <ul class="condition-list">
            <li>🎯 윗글을 바탕으로 정전기의 특성이 잘 드러나도록 시각 요소(A)와 청각 요소(B) 연출 계획을 세울 것</li>
            <li>🎯 설정한 시각 및 청각 요소의 연출 효과를 각각 서술하되, 반드시 윗글의 내용을 근거로 포함할 것</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="input-label">• 답안 입력</div>', unsafe_allow_html=True)
    ans_2_3_v = st.text_area("(1) 시각 요소(Ⓐ) 및 효과", key="2_3_v")
    ans_2_3_a = st.text_area("(2) 청각 요소(Ⓑ) 및 효과", key="2_3_a")

    if st.button("문제 2 채점하기", type="primary", key="btn_2"):
        score2 = 0
        st.markdown("#### 🎯 채점 결과 리포트")
        
        if '고여' in ans_2_1_1 or '갇혀' in ans_2_1_1:
            st.success("✅ 문항 1 - (1) ㄱ 통과")
            score2 += 1
        else:
            st.error("❌ 문항 1 - (1) ㄱ 오답: 지문의 '고여 있는 물' 비유를 확인하세요.")
            
        if '이동하지' in ans_2_1_2 or '머물' in ans_2_1_2 or '정지' in ans_2_1_2:
            if '흐르는' in ans_2_1_2:
                st.error("❌ 문항 1 - (2) ㄴ 오개념 발견: 정전기 설명에 실생활 전기의 특징('흐름')을 기술했습니다.")
            else:
                st.success("✅ 문항 1 - (2) ㄴ 통과")
                score2 += 1
        else:
            st.error("❌ 문항 1 - (2) ㄴ 오답: '전하가 이동하지 않고 머물러 있음'의 뜻이 드러나야 합니다.")
            
        if '위험하지' in ans_2_1_3 or '안전' in ans_2_1_3 or '피해가없' in normalize(ans_2_1_3):
            st.success("✅ 문항 1 - (3) ㄷ 통과")
            score2 += 1
        else:
            st.error("❌ 문항 1 - (3) ㄷ 오답: 위험성 유무 결과는 '위험하지 않음'입니다.")
            
        m1 = re.search(r'\(([^)]+)\)', ans_2_2_1)
        m2 = re.search(r'\(([^)]+)\)', ans_2_2_2)
        if m1 and m2:
            st.success("✅ 문항 2 통과")
            score2 += 1
        else:
            st.error("❌ 문항 2 미흡: 설명 방법 명칭을 문장 끝 괄호 안에 정확히 명시해 주세요.")

        if ('댐' in ans_2_3_v or '호수' in ans_2_3_v or '고여' in ans_2_3_v) and ('고요' in ans_2_3_a or '침묵' in ans_2_3_a):
            if '폭포' in ans_2_3_a or '웅장' in ans_2_3_a:
                st.error("❌ 문항 3 오개념 발견: 정전기 연출에 실생활 전기의 성격인 폭포/웅장 소리를 융합했습니다.")
            else:
                st.success("✅ 문항 3 통과")
                score2 += 1
        else:
            st.error("❌ 문항 3 미흡: 정적인 환경을 고려한 연출 기획과 지문 근거 효과 설명이 부족합니다.")

        if score2 == 5:
            st.session_state.resolved[2] = True
            st.balloons()

# ==============================================================================
# [문제 3] AI 그림과 예술
# ==============================================================================
with tab3:
    st.markdown("## 3️⃣ 알고리즘 초상화와 가치 — 인공지능 그림과 예술")
    
    st.markdown("""
    <div class="passage-box">
        <span class="passage-title">[대담 지문]</span><br>
        <b>기자</b>: 최근 생성형 인공 지능이 그린 그림이 미술계에서 큰 화제를 모으고 있습니다. 어떤 작품인지 소개해 주실 수 있을까요?<br>
        <b>전문가</b>: 네, 대표적으로 「에드몽 드 벨라미」라는 작품이 있습니다. 이 작품은 14~20세기에 그려진 초상화 1만 5,000점을 토대로 알고리즘과 데이터를 사용해 그려졌습니다. 뉴욕 크리스티 경매에서 최종 낙찰가 43만 2,000달러에 판매되어 큰 놀라움을 주었죠.<br>
        <b>기자</b>: 그렇다면 이 그림을 인간이 만든 예술 작품과 같다고 볼 수 있을까요?<br>
        <b>전문가</b>: 올림픽 경기를 예로 들어 볼게요. 우리가 올림픽에 열광하는 이유는 선수들이 경기를 위해 기울인 노력이나 열정을 알기 때문입니다. 반면 로봇이 한 번의 실수 없이 완벽하게 피겨 스케이팅을 해내더라도 우리의 마음을 울리지는 못하지요. 이처럼 인간의 작품에는 작가의 고유한 감정이나 철학, 그리고 작가가 살아온 삶의 경험, 세상을 바라보는 관점, 그를 둘러싼 환경 같은 내외부적인 요소가 종합적으로 담겨 있으므로 예술로 볼 수 있습니다. 하지만 인공 지능은 감정도 느끼지 못하고 독자적인 철학이나 이야기가 없기 때문에 이를 예술로 보기는 어렵습니다.<br>
        <b>기자</b>: 그렇다면 인공 지능이 그린 그림은 가치가 전혀 없는 것인가요?<br>
        <b>전문가</b>: 그렇지는 않습니다. 비록 인간과 같은 감정은 없더라도, 기존 미술계에 큰 변화를 가져왔다는 점에서 분명한 의미가 있습니다. 또한 앞으로 우리가 알고 있던 예술의 범주를 확장할 수 있다는 점에서 상징적인 가치를 지닙니다.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 문항 1")
    st.markdown("윗글을 요약하여 표로 정리하였다. ㄱ~ㄷ에 들어갈 내용을 찾아 쓰시오.")
    c1, c2, c3 = st.columns(3)
    ans_3_1_1 = c1.text_input("(1) ㄱ:", key="3_1_1")
    ans_3_1_2 = c2.text_input("(2) ㄴ:", key="3_1_2")
    ans_3_1_3 = c3.text_input("(3) ㄷ:", key="3_1_3")

    st.markdown("### 문항 2")
    st.markdown("윗글을 활용하여 '인공 지능이 그린 그림을 바라보는 시각'에 대한 설명문을 작성하려 한다. 주어진 첫 문장('인공 지능이 그린 그림이 늘어나는 요즘, 우리는 이 작품들을 어떤 눈으로 바라봐야 할지 올바르게 생각해야 한다.')에 이어지는 내용을 완성하시오.")
    st.markdown("""
    <div class="condition-container">
        <div class="condition-title">〈조건〉</div>
        <ul class="condition-list">
            <li>🎯 주어진 문장에 이어지는 문장을 (1), (2)에 각각 하나씩 작성할 것</li>
            <li>🎯 (1)과 (2)에는 서로 다른 설명 방법이 1가지 이상 활용되어야 하며, 각 문장의 끝에 설명 방법의 명칭을 괄호에 넣어 기재할 것</li>
            <li>🎯 윗글에 제시된 내용만을 활용하고, 두 문장이 유기적인 논리적 흐름을 갖도록 서술할 것</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="input-label">• 답안 입력</div>', unsafe_allow_html=True)
    ans_3_2_1 = st.text_input("(1)", key="3_2_1")
    ans_3_2_2 = st.text_input("(2)", key="3_2_2")

    st.markdown("### 문항 3")
    st.markdown("윗글을 바탕으로 '인공 지능이 그린 그림을 바라보는 시각'을 설명하는 영상 기획안 중, [장면 2] 마음에 울림을 주는 진정한 예술 부분을 완성하시오.")
    st.markdown("""
    <div class="condition-container">
        <div class="condition-title">〈조건〉</div>
        <ul class="condition-list">
            <li>🎯 윗글을 바탕으로 인간이 만들어내는 예술의 특성이 잘 드러나도록 시각 요소(A)와 청각 요소(B) 연출 계획을 세울 것</li>
            <li>🎯 설정한 시각 및 청각 요소의 연출 효과를 각각 서술하되, 반드시 윗글의 내용을 근거(인간의 감정, 노력 등)로 포함할 것</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="input-label">• 답안 입력</div>', unsafe_allow_html=True)
    ans_3_3_v = st.text_area("(1) 시각 요소(Ⓐ) 및 효과", key="3_3_v")
    ans_3_3_a = st.text_area("(2) 청각 요소(Ⓑ) 및 효과", key="3_3_a")

    if st.button("문제 3 채점하기", type="primary", key="btn_3"):
        score3 = 0
        st.markdown("#### 🎯 채점 결과 리포트")
        
        if '로봇' in ans_3_1_1 and '피겨' in ans_3_1_1:
            st.success("✅ 문항 1 - (1) ㄱ 통과")
            score3 += 1
        else:
            st.error("❌ 문항 1 - (1) ㄱ 오답: 비유 수단인 '로봇의 피겨 스케이팅' 내용이 명시되어야 합니다.")
            
        if ('아니다' in ans_3_1_2 or '어렵다' in ans_3_1_2) and ('감정' in ans_3_1_2 or '철학' in ans_3_1_2 or '이야기' in ans_3_1_2):
            st.success("✅ 문항 1 - (2) ㄴ 통과")
            score3 += 1
        else:
            st.error("❌ 문항 1 - (2) ㄴ 오답: '예술로 보기 어렵다'는 결론과 '감정/철학의 부재'라는 지문 핵심 근거가 나타나야 합니다.")
            
        if '변화' in ans_3_1_3 or '확장' in ans_3_1_3 or '상징' in ans_3_1_3:
            st.success("✅ 문항 1 - (3) ㄷ 통과")
            score3 += 1
        else:
            st.error("❌ 문항 1 - (3) ㄷ 오답: 지문에 서술된 가치인 '미술계 변화' 혹은 '예술 범주 확장'의 뜻이 기술되어야 합니다.")

        m1 = re.search(r'\(([^)]+)\)', ans_3_2_1)
        m2 = re.search(r'\(([^)]+)\)', ans_3_2_2)
        if m1 and m2:
            st.success("✅ 문항 2 통과")
            score3 += 1
        else:
            st.error("❌ 문항 2 미흡: 문장 끝에 활용한 설명 방법 명칭을 괄호 안에 알맞게 적으세요.")

        if ('인간' in ans_3_3_v or '선수' in ans_3_3_v or '땀' in ans_3_3_v) and ('음악' in ans_3_3_a or '환호' in ans_3_3_a or '박수' in ans_3_3_a):
            if '기계음' in ans_3_3_a:
                st.error("❌ 문항 3 오개념 발견: 인간의 예술 연출 공간에 AI 속성인 '기계음'을 활용했습니다.")
            else:
                st.success("✅ 문항 3 통과")
                score3 += 1
        else:
            st.error("❌ 문항 3 미흡: 인간의 열정적 요소가 강조된 연출 기획과 지문 근거가 명시되어야 합니다.")

        if score3 == 5:
            st.session_state.resolved[3] = True
            st.balloons()

# ==============================================================================
# [📚 복습할 내용]
# ==============================================================================
with tab4:
    st.markdown("### 📚 대단원 핵심 개념 및 가이드 요약")
    st.write("감점 없는 서·논술형 답안 작성을 위해 아래 요약표를 꼭 기억해 주세요.")
    
    st.table([
        {"설명 방법": "정의", "핵심 내용": "대상의 본질이나 개념을 명확하게 규정하여 설명함"},
        {"설명 방법": "예시", "핵심 내용": "구체적이고 친숙한 사례를 들어 독자의 이해를 도움"},
        {"설명 방법": "인과", "핵심 내용": "원인과 결과를 중심으로 대상을 논리적으로 설명함"},
        {"설명 방법": "분석", "핵심 내용": "하나의 대상을 구성 요소나 여러 부분으로 쪼개어 기술함"},
        {"설명 방법": "비교와 대조", "핵심 내용": "두 대상 간의 공통점(비교)과 차이점(대조)을 선명하게 부각함"}
    ])
    
    st.markdown("""
    > 💡 **최종 점검 팁**
    > - **형태 요건 준수**: 문항 요구사항에 설정된 괄호 서식 등 지시 규칙을 반드시 이행하세요.
    > - **오개념 결합 원천 차단**: 한 개념의 특징을 반대되거나 이질적인 다른 개념 공간에 섞어 쓰지 않도록 논리를 정제하세요.
    """)
