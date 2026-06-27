import streamlit as st
import re

# 페이지 기본 설정 및 스타일 정의
st.set_page_config(page_title="국어 서논술형 답안 작성 연습", layout="wide", page_icon="✏️")

# 커스텀 CSS: image_5630fe.png 스타일 및 밀착 배치 레이아웃 재현
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

    /* 표 서식 공통 스타일 (보기 / 조건) */
    .info-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
        margin-bottom: 15px;
        font-size: 1rem;
    }
    .info-table th {
        background-color: #F1F3F5;
        color: #343A40;
        border: 1px solid #DEE2E6;
        padding: 10px;
        font-weight: bold;
        text-align: center;
        width: 15%;
    }
    .info-table td {
        border: 1px solid #DEE2E6;
        padding: 12px;
        line-height: 1.6;
        background-color: #FFFFFF;
    }
    
    /* 발문 스타일 - 입력창과 밀착시키기 위해 하단 마진 제거 */
    .question-text {
        font-size: 1.1rem;
        font-weight: 600;
        color: #212529;
        margin-top: 15px;
        margin-bottom: 2px !important; 
    }
    
    /* 스크립트 내 수직 간격 최소화 */
    .block-container {
        padding-top: 2rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# 상단 헤더 UI
st.markdown('<div class="main-title">✏️ [국어] 서·논술형 답안 작성 연습</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">작성한 답안을 입력한 뒤 문제의 조건에 맞게 작성하였는지의 여부를 확인하세요. 수업시간에 배운 내용을 복습할 때 마음이 막막할까봐 만든 자료이므로, 참고로만 활용하세요. 선생님과 수업 시간에 공부한 내용이 답안 작성의 초점이에요 😉</div>', unsafe_allow_html=True)

# 세션 상태 초기화 (각 문제별 통과 여부 및 오답 정보 트래킹)
if "resolved" not in st.session_state:
    st.session_state.resolved = {1: False, 2: False, 3: False}
if "wrong_details" not in st.session_state:
    st.session_state.wrong_details = {1: [], 2: [], 3: []}

# 진행 상황바 및 상단 UI 배치
resolved_count = sum(st.session_state.resolved.values())
st.write(f"✅ **완료된 대문항: {resolved_count} / 3**")
st.progress(resolved_count / 3)

# 처음부터 다시 풀기 버튼
if st.button("🔄 처음부터 다시 풀기", type="secondary"):
    st.session_state.resolved = {1: False, 2: False, 3: False}
    st.session_state.wrong_details = {1: [], 2: [], 3: []}
    st.rerun()

st.markdown("---")

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
    
    # [서·논술형 1]
    st.markdown('<p class="question-text">[서·논술형 1] 윗글을 요약하여 &lt;보기&gt;의 표로 정리하였다. ㄱ~ㄷ에 들어갈 내용을 찾아 쓰시오.</p>', unsafe_allow_html=True)
    st.markdown("""
    <table class="info-table">
        <tr>
            <th>&lt;보기&gt;</th>
            <td>
                • 과제의 특성: 비교적 쉬운 취미 생활이나 과제 ➔ 효율적인 환경 및 방법: 커피숍, 도서관, 공부 모임 ➔ 관련 심리 현상: 사회적 촉진<br>
                • 과제의 특성: <b>[  ㄱ  ]</b> ➔ 효율적인 환경 및 방법: <b>[  ㄴ  ]</b> ➔ 관련 심리 현상: <b>[  ㄷ  ]</b>
            </td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    ans_1_1 = c1.text_input("(1) ㄱ :", key="1_1")
    ans_1_2 = c2.text_input("(2) ㄴ :", key="1_2")
    ans_1_3 = c3.text_input("(3) ㄷ :", key="1_3")
    
    # [서·논술형 2]
    st.markdown('<p class="question-text">[서·논술형 2] 윗글을 활용하여 \'과제 난이도에 따른 효율적인 학습 전략\'에 대한 설명문을 작성하려 한다. 주어진 첫 문장에 이어지는 내용을 완성하시오.</p>', unsafe_allow_html=True)
    st.markdown("""
    <table class="info-table">
        <tr>
            <th>주어진 첫 문장</th>
            <td>과제의 특성과 난이도에 따라 우리의 학습 효율을 높이는 방법은 다르게 적용되어야 한다.</td>
        </tr>
        <tr>
            <th>&lt;조건&gt;</th>
            <td>
                1. 서로 다른 2가지의 설명 방법을 사용하여 이어지는 문장을 (1), (2)에 각각 하나씩 작성할 것.<br>
                2. 윗글에 제시된 내용만을 활용하여 문장을 구성할 것.<br>
                3. 각 문장의 끝에 자신이 사용한 설명 방법의 명칭을 괄호에 넣어 표기할 것. (예: (예시), (대조))
            </td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
    c_ans1 = st.text_input("(1) :", key="2_1")
    c_ans2 = st.text_input("(2) :", key="2_2")
    
    # [서·논술형 3]
    st.markdown('<p class="question-text">[서·논술형 3] 윗글을 바탕으로 \'상황에 맞는 학습 공간 선택법\'을 설명하는 영상을 제작할 때, 어려운 과제를 할 때의 [장면 2] 기획안을 완성하시오.</p>', unsafe_allow_html=True)
    st.markdown("""
    <table class="info-table">
        <tr>
            <th>&lt;조건&gt;</th>
            <td>
                1. 어려운 과제를 할 때 필요한 환경의 특성이 드러나도록 시각 요소(Ⓐ)와 청각 요소(Ⓑ) 연출 계획을 세울 것.<br>
                2. 자신이 설정한 시각 요소와 청각 요소가 글의 내용을 전달하는 데 어떤 효과가 있는지 글의 내용을 근거로 각각 서술할 것.
            </td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
    ans_3_v = st.text_area("(1) 시각 요소(Ⓐ) 및 효과 :", key="3_1", height=80)
    ans_3_a = st.text_area("(2) 청각 요소(Ⓑ) 및 효과 :", key="3_2", height=80)

    if st.button("문제 1 채점하기", type="primary", key="btn_1"):
        errors = []
        
        # 1-1 채점
        if not (('쉬운' in ans_1_1 or '낮은' in ans_1_1 or '어려운' in ans_1_1 or '복잡한' in ans_1_1) and '과제' in ans_1_1):
            errors.append({"문항": "[서·논술형 1] (1) ㄱ", "포인트": "핵심어휘(과제/난이도) 추출 및 대조적 관계 이해", "부족": "지문에서 대조되는 과제의 핵심 특성(어렵고 복잡한 과제 등)이 누락되었거나 명확하지 않습니다."})
        # 1-2 채점
        if not ('혼자' in ans_1_2 and ('집중' in ans_1_2 or '차분' in ans_1_2)):
            errors.append({"문항": "[서·논술형 1] (2) ㄴ", "포인트": "지문 근거에 기반한 명확한 해결 환경 도출", "부족": "어려운 과제를 해결하기 위해 필요한 환경인 '차분하게 혼자 집중하는 공간/시간'의 의미가 부족합니다."})
        # 1-3 채점
        if normalize(ans_1_3) != "사회적억제":
            errors.append({"문항": "[서·논술형 1] (3) ㄷ", "포인트": "핵심 심리학 용어 원형 매칭", "부족": "사회적 촉진과 정확히 대비되는 정식 학술 용어인 '사회적 억제'를 올바르게 작성해야 합니다."})
            
        # 2번 채점
        m1 = re.search(r'\(([^)]+)\)', c_ans1)
        m2 = re.search(r'\(([^)]+)\)', c_ans2)
        if not (m1 and m2):
            errors.append({"문항": "[서·논술형 2]", "포인트": "설명 방법 활용 및 문장 끝 괄호 표기 조건 준수", "부족": "각 문장 끝에 활용한 설명 방법의 명칭을 명시하는 규칙(예: (예시), (대조))을 충족하지 못했습니다."})
            
        # 3번 채점
        if not (('혼자' in ans_3_v or '독립' in ans_3_v) and ('조용' in ans_3_a or '소음' in ans_3_a) and ('효과' in ans_3_v and '효과' in ans_3_a)):
            errors.append({"문항": "[서·논술형 3]", "포인트": "매체 복합양식성(시청각) 연출 기획 및 지문 연계 효과 도출", "부족": "어려운 과제 상황에 알맞은 시각/청각 연출 계획과, 그것이 유발하는 실제 지문 속 효과(집중, 익숙함 등)에 대한 인과적 설명이 미흡합니다."})

        st.session_state.wrong_details[1] = errors
        st.markdown("#### 🎯 채점 결과 리포트")
        if not errors:
            st.session_state.resolved[1] = True
            st.success("🎉 모든 조건을 완벽하게 충족하셨습니다! 다음 문제로 넘어가세요.")
            st.balloons()
        else:
            st.session_state.resolved[1] = False
            st.error(f"❌ {len(errors)}개의 문항에서 조건 미충족 혹은 오답이 발견되었습니다. '📚 복습할 내용' 탭을 확인해 보세요.")

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
    
    # [서·논술형 1]
    st.markdown('<p class="question-text">[서·논술형 1] 윗글을 요약하여 &lt;보기&gt;의 표로 정리하였다. ㄱ~ㄷ에 들어갈 내용을 찾아 쓰시오.</p>', unsafe_allow_html=True)
    st.markdown("""
    <table class="info-table">
        <tr>
            <th>&lt;보기&gt;</th>
            <td>
                • 실생활에서 쓰는 전기: 물의 상태 비유 ➔ 흐르는 물 | 전하의 상태 ➔ 이동함 | 위험성 ➔ 전압이 높고 전류가 흘러 위험함<br>
                • 정전기: 물의 상태 비유 ➔ <b>[  ㄱ  ]</b> | 전하의 상태 ➔ <b>[  ㄴ  ]</b> | 위험성 ➔ <b>[  ㄷ  ]</b>
            </td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    ans_2_1_1 = c1.text_input("(1) ㄱ :", key="2_1_1")
    ans_2_1_2 = c2.text_input("(2) ㄴ :", key="2_1_2")
    ans_2_1_3 = c3.text_input("(3) ㄷ :", key="2_1_3")

    # [서·논술형 2]
    st.markdown('<p class="question-text">[서·논술형 2] 윗글을 활용하여 \'정전기의 특징\'에 대한 설명문을 작성하려 한다. 주어진 첫 문장에 이어지는 내용을 완성하시오.</p>', unsafe_allow_html=True)
    st.markdown("""
    <table class="info-table">
        <tr>
            <th>주어진 첫 문장</th>
            <td>겨울철에 흔히 겪는 정전기는 우리가 평소 집에서 사용하는 전기와는 다른 뚜렷한 특징이 있다.</td>
        </tr>
        <tr>
            <th>&lt;조건&gt;</th>
            <td>
                1. 주어진 문장에 이어지는 문장을 (1), (2)에 각각 하나씩 작성할 것.<br>
                2. (1)과 (2)에는 서로 다른 설명 방법이 1가지 이상 활용되어야 하며, 각 문장의 끝에 설명 방법의 명칭을 괄호에 넣어 기재할 것.<br>
                3. 윗글에 제시된 내용만을 활용하고, 두 문장이 논리적 흐름을 갖고 이어지도록 서술할 것.
            </td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
    ans_2_2_1 = st.text_input("(1) :", key="2_2_1")
    ans_2_2_2 = st.text_input("(2) :", key="2_2_2")

    # [서·논술형 3]
    st.markdown('<p class="question-text">[서·논술형 3] 윗글을 바탕으로 \'정전기의 특징\'을 설명하는 영상 기획안 중, [장면 2] 정전기(고여 있는 물) 부분을 완성하시오.</p>', unsafe_allow_html=True)
    st.markdown("""
    <table class="info-table">
        <tr>
            <th>&lt;조건&gt;</th>
            <td>
                1. 윗글을 바탕으로 정전기의 특성이 잘 드러나도록 시각 요소(A)와 청각 요소(B) 연출 계획을 세울 것.<br>
                2. 설정한 시각 및 청각 요소의 연출 효과를 각각 서술하되, 반드시 윗글의 내용을 근거로 포함할 것.
            </td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
    ans_2_3_v = st.text_area("(1) 시각 요소(Ⓐ) 및 효과 :", key="2_3_v", height=80)
    ans_2_3_a = st.text_area("(2) 청각 요소(Ⓑ) 및 효과 :", key="2_3_a", height=80)

    if st.button("문제 2 채점하기", type="primary", key="btn_2"):
        errors = []
        
        if not ('고여' in ans_2_1_1 or '갇혀' in ans_2_1_1):
            errors.append({"문항": "[서·논술형 1] (1) ㄱ", "포인트": "비유적 표현의 핵심 속성 추출", "부족": "실생활 전기의 '흐르는 물'과 완벽히 대비되는 정전기의 비유적 표현인 '고여 있는 물'이 기술되지 않았습니다."})
        if not ('이동하지' in ans_2_1_2 or '머물' in ans_2_1_2 or '정지' in ans_2_1_2) or '흐르는' in ans_2_1_2:
            errors.append({"문항": "[서·논술형 1] (2) ㄴ", "포인트": "과학적 대상의 상태 기술 및 오개념 배제", "부족": "정전기 한자의 핵심 뜻인 '전하가 이동하지 않고 머물러 있음(정지상태)'의 서술이 불충분하거나 일반 전기의 속성을 혼용했습니다."})
        if not ('위험하지' in ans_2_1_3 or '안전' in ans_2_1_3 or '피해가없' in normalize(ans_2_1_3)):
            errors.append({"문항": "[서·논술형 1] (3) ㄷ", "포인트": "지문 기반의 명확한 인과 판단 및 결론 도출", "부족": "정전기의 전류 특성에 따른 최종적 위험성 판단 결과인 '위험하지 않음'이 올바르게 나타나지 않았습니다."})
            
        m1 = re.search(r'\(([^)]+)\)', ans_2_2_1)
        m2 = re.search(r'\(([^)]+)\)', ans_2_2_2)
        if not (m1 and m2):
            errors.append({"문항": "[서·논술형 2]", "포인트": "다양한 설명 방법 매칭 및 구조적 일치", "부족": "조건에 규정된 설명 방법의 명칭(예: (정의), (비교))을 문장 끝에 기입하지 않았거나 논리적 연결이 어색합니다."})
            
        if not (('댐' in ans_2_3_v or '호수' in ans_2_3_v or '고여' in ans_2_3_v) and ('고요' in ans_2_3_a or '침묵' in ans_2_3_a)) or '폭포' in ans_2_3_a:
            errors.append({"문항": "[서·논술형 3]", "포인트": "매체 특성에 맞는 정적 속성 시청각 형상화", "부족": "정전기의 본질인 '고여 있음/정지함'을 구현하기 위한 시청각적 연출 계획 및 지문 근거 서술이 잘못되었거나 흐르는 물의 특성과 혼동했습니다."})

        st.session_state.wrong_details[2] = errors
        st.markdown("#### 🎯 채점 결과 리포트")
        if not errors:
            st.session_state.resolved[2] = True
            st.success("🎉 모든 조건을 완벽하게 충족하셨습니다! 다음 문제로 넘어가세요.")
            st.balloons()
        else:
            st.session_state.resolved[2] = False
            st.error(f"❌ {len(errors)}개의 문항에서 조건 미충족 혹은 오답이 발견되었습니다. '📚 복습할 내용' 탭을 확인해 보세요.")

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
    
    # [서·논술형 1]
    st.markdown('<p class="question-text">[서·논술형 1] 윗글을 요약하여 &lt;보기&gt;의 표로 정리하였다. ㄱ~ㄷ에 들어갈 내용을 찾아 쓰시오.</p>', unsafe_allow_html=True)
    st.markdown("""
    <table class="info-table">
        <tr>
            <th>&lt;보기&gt;</th>
            <td>
                • 인간의 작품: 올림픽 경기 비유 대상 ➔ 선수들의 노력과 열정 | 예술 판단 여부 ➔ 고유한 감정, 경험, 철학 등이 담겨 예술로 봄<br>
                • 인공지능 작품: 올림픽 경기 비유 대상 ➔ <b>[  ㄱ  ]</b> | 예술 판단 여부 ➔ <b>[  ㄴ  ]</b> | 예술적 가치 여부 ➔ <b>[  ㄷ  ]</b>
            </td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    ans_3_1_1 = c1.text_input("(1) ㄱ :", key="3_1_1")
    ans_3_1_2 = c2.text_input("(2) ㄴ :", key="3_1_2")
    ans_3_1_3 = c3.text_input("(3) ㄷ :", key="3_1_3")

    # [서·논술형 2]
    st.markdown('<p class="question-text">[서·논술형 2] 윗글을 활용하여 \'인공 지능이 그린 그림을 바라보는 시각\'에 대한 설명문을 작성하려 한다. 주어진 첫 문장에 이어지는 내용을 완성하시오.</p>', unsafe_allow_html=True)
    st.markdown("""
    <table class="info-table">
        <tr>
            <th>주어진 첫 문장</th>
            <td>인공 지능이 그린 그림이 늘어나는 요즘, 우리는 이 작품들을 어떤 눈으로 바라봐야 할지 올바르게 생각해야 한다.</td>
        </tr>
        <tr>
            <th>&lt;조건&gt;</th>
            <td>
                1. 주어진 문장에 이어지는 문장을 (1), (2)에 각각 하나씩 작성할 것.<br>
                2. (1)과 (2)에는 서로 다른 설명 방법이 1가지 이상 활용되어야 하며, 각 문장의 끝에 설명 방법의 명칭을 괄호에 넣어 기재할 것.<br>
                3. 윗글에 제시된 내용만을 활용하고, 두 문장이 유기적인 논리적 흐름을 갖도록 서술할 것.
            </td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
    ans_3_2_1 = st.text_input("(1) :", key="3_2_1")
    ans_3_2_2 = st.text_input("(2) :", key="3_2_2")

    # [서·논술형 3]
    st.markdown('<p class="question-text">[서·논술형 3] 윗글을 바탕으로 \'인공 지능이 그린 그림을 바라보는 시각\'을 설명하는 영상 기획안 중, [장면 2] 마음에 울림을 주는 진정한 예술 부분을 완성하시오.</p>', unsafe_allow_html=True)
    st.markdown("""
    <table class="info-table">
        <tr>
            <th>&lt;조건&gt;</th>
            <td>
                1. 윗글을 바탕으로 인간이 만들어내는 예술의 특성이 잘 드러나도록 시각 요소(A)와 청각 요소(B) 연출 계획을 세울 것.<br>
                2. 설정한 시각 및 청각 요소의 연출 효과를 각각 서술하되, 반드시 윗글의 내용을 근거(인간의 감정, 노력 등)로 포함할 것.
            </td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
    ans_3_3_v = st.text_area("(1) 시각 요소(Ⓐ) 및 효과 :", key="3_3_v", height=80)
    ans_3_3_a = st.text_area("(2) 청각 요소(Ⓑ) 및 효과 :", key="3_3_a", height=80)

    if st.button("문제 3 채점하기", type="primary", key="btn_3"):
        errors = []
        
        if not ('로봇' in ans_3_1_1 and '피겨' in ans_3_1_1):
            errors.append({"문항": "[서·논술형 1] (1) ㄱ", "포인트": "비유적 유추 관계 매칭", "부족": "지문에서 인공지능 그림을 설명하기 위해 활용한 올림픽 비유 대상인 '로봇의 완벽한 피겨 스케이팅' 내용이 빠져 있습니다."})
        if not (('아니다' in ans_3_1_2 or '어렵다' in ans_3_1_2) and ('감정' in ans_3_1_2 or '철학' in ans_3_1_2 or '이야기' in ans_3_1_2)):
            errors.append({"문항": "[서·논술형 1] (2) ㄴ", "포인트": "판단 결과와 명확한 텍스트 근거 매칭", "부족": "인공지능 작품을 예술로 규정하기 어려운 명확한 이유인 '독자적 철학이나 감정의 부재'가 결론과 함께 명시되어야 합니다."})
        if not ('변화' in ans_3_1_3 or '확장' in ans_3_1_3 or '상징' in ans_3_1_3):
            errors.append({"문항": "[서·논술형 1] (3) ㄷ", "포인트": "대상의 다각적 의미 및 가치 인정성 기술", "부족": "인간의 예술적 감동은 없으나 지문에 기술된 '미술계 변화 유도' 혹은 '예술 범주 확장'의 의의 설명이 명확하지 않습니다."})
            
        m1 = re.search(r'\(([^)]+)\)', ans_3_2_1)
        m2 = re.search(r'\(([^)]+)\)', ans_3_2_2)
        if not (m1 and m2):
            errors.append({"문항": "[서·논술형 2]", "포인트": "요구 조건 서식 엄밀 적용 및 논리 전개", "부족": "문장 끝 괄호 안에 알맞은 국어 설명 기법 명칭을 누락했거나, 텍스트 전반의 유기성이 부족합니다."})
            
        if not (('인간' in ans_3_3_v or '선수' in ans_3_3_v or '땀' in ans_3_3_v) and ('음악' in ans_3_3_a or '환호' in ans_3_3_a or '박수' in ans_3_3_a)) or '기계음' in ans_3_3_a:
            errors.append({"문항": "[서·논술형 3]", "포인트": "인간의 예술성 발현 조건과 일치하는 미디어 연출 기획", "부족": "인간 예술 고유의 가치인 감정, 노력, 철학 등이 살아나는 시청각 기획안과 마음의 울림 효과가 명시되지 않고 기계적 요소를 혼합했습니다."})

        st.session_state.wrong_details[3] = errors
        st.markdown("#### 🎯 채점 결과 리포트")
        if not errors:
            st.session_state.resolved[3] = True
            st.success("🎉 모든 조건을 완벽하게 충족하셨습니다! 고생하셨습니다.")
            st.balloons()
        else:
            st.session_state.resolved[3] = False
            st.error(f"❌ {len(errors)}개의 문항에서 조건 미충족 혹은 오답이 발견되었습니다. '📚 복습할 내용' 탭을 확인해 보세요.")

# ==============================================================================
# [📚 복습할 내용] - 동적 조건 불충족 문제 피드백 바인딩
# ==============================================================================
with tab4:
    st.markdown("### 📚 오답 노트 및 맞춤형 조건 피드백")
    
    # 세션에 기록된 에러(오답) 총합 산출
    total_errors = sum(len(st.session_state.wrong_details[i]) for i in [1, 2, 3])
    
    if total_errors == 0:
        st.info("💡 아직 채점을 진행하지 않았거나 틀린 문제가 없습니다. 조건을 충족하지 못한 문항이 있으면 여기에 개별 맞춤형 복습 포인트가 실시간으로 표시됩니다.")
    else:
        st.warning(f"⚠️ 현재 {total_errors}개의 세부 문항에서 조건 미충족 사항이 발견되었습니다. 아래 요소를 보완하여 다시 작성해 보세요.")
        
        for q_num in [1, 2, 3]:
            if st.session_state.wrong_details[q_num]:
                st.markdown(f"#### 🔍 [문제 {q_num}]번 세부 미흡 사항 안내")
                for detail in st.session_state.wrong_details[q_num]:
                    with st.expander(f"📌 {detail['문항']} 보기 조건 피드백", expanded=True):
                        st.markdown(f"**💡 해당 개념 핵심 복습 포인트:**\n> {detail['포인트']}")
                        st.markdown(f"**❌ 내 답안의 부족한 부분:**\n> <span style='color:#E74C3C; font-weight:600;'>{detail['부족']}</span>", unsafe_allow_html=True)
