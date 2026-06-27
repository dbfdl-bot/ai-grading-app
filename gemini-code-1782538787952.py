import streamlit as st
import re

# 페이지 기본 설정 및 스타일 정의
st.set_page_config(page_title="국어 서논술형 답안 작성 연습", layout="wide", page_icon="✏️")

# 커스텀 CSS: 발문-입력란 밀착 배치 및 표 스타일 재현
st.markdown("""
    <style>
    .main-title {
        font-size: 2.2rem !important;
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

    /* 원본 <보기>, <조건> 표 서식 */
    .info-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 8px;
        margin-bottom: 12px;
        font-size: 0.95rem;
    }
    .info-table th {
        background-color: #F1F3F5;
        color: #343A40;
        border: 1px solid #DEE2E6;
        padding: 10px;
        font-weight: bold;
        text-align: center;
        width: 20%;
    }
    .info-table td {
        border: 1px solid #DEE2E6;
        padding: 12px;
        line-height: 1.6;
        background-color: #FFFFFF;
        color: #212529;
    }
    
    /* 발문과 입력란 밀착 레이아웃 (마진 최소화) */
    .question-text {
        font-size: 1.05rem;
        font-weight: 600;
        color: #212529;
        margin-top: 12px !important;
        margin-bottom: 2px !important; 
    }
    div[data-testid="stFormSubmitButton"] {
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 상단 헤더 UI
st.markdown('<div class="main-title">✏️ [국어] 서·논술형 답안 작성 연습</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">작성한 답안을 입력한 뒤 문제의 조건에 맞게 작성하였는지의 여부를 확인하세요. 수업시간에 배운 내용을 복습할 때 마음이 막막할까봐 만든 자료이므로, 참고로만 활용하세요. 선생님과 수업 시간에 공부한 내용이 답안 작성의 초점이에요 😉</div>', unsafe_allow_html=True)

# 세션 상태 및 '리셋 횟수(Key 변형용)' 초기화
if "resolved" not in st.session_state:
    st.session_state.resolved = {1: False, 2: False, 3: False}
if "wrong_details" not in st.session_state:
    st.session_state.wrong_details = {1: [], 2: [], 3: []}
if "reset_count" not in st.session_state:
    st.session_state.reset_count = 0

# 진행 상황바 및 상단 UI 배치
resolved_count = sum(st.session_state.resolved.values())
st.write(f"✅ **완료된 대문항: {resolved_count} / 3**")
st.progress(resolved_count / 3)

# 🔄 처음부터 다시 풀기 버튼 (누르면 reset_count를 1 올려서 모든 입력란의 고유 key를 바꿈 -> 완전 초기화)
if st.button("🔄 처음부터 다시 풀기", type="secondary"):
    st.session_state.resolved = {1: False, 2: False, 3: False}
    st.session_state.wrong_details = {1: [], 2: [], 3: []}
    st.session_state.reset_count += 1
    st.rerun()

st.markdown("---")

def normalize(text):
    return re.sub(r'\s+', '', text).strip()

# 고유 Key 생성을 위한 접미사 설정
r_id = f"_r{st.session_state.reset_count}"

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
        <b>전문가</b>: 그럴 때는 반대입니다. 지나치지 어렵거나 도전이 필요한 과제는 충분히 연습하며 익숙해질 때까지 차분하게 혼자 집중하는 시간을 가지는 것이 좋습니다.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="question-text">[서·논술형 1] 윗글을 요약하여 표로 정리하였다. ㄱ~ㄷ에 들어갈 내용을 찾아 쓰시오.</p>', unsafe_allow_html=True)
    st.markdown("""
    <table class="info-table">
        <tr>
            <th>과제의 특성</th>
            <th>효율적인 환경 및 방법</th>
            <th>관련된 심리 현상</th>
        </tr>
        <tr>
            <td>비교적 쉬운 취미 생활이나 큰 노력을 들일 필요가 없는 과제</td>
            <td>커피숍, 도서관 등에서 하거나 모임을 만들어 다른 사람들과 함께 함</td>
            <td>사회적 촉진</td>
        </tr>
        <tr>
            <td><b>[  ㄱ  ]</b></td>
            <td><b>[  ㄴ  ]</b></td>
            <td><b>[  ㄷ  ]</b></td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    ans_1_1 = c1.text_input("(1) ㄱ (과제의 특성):", key=f"1_1{r_id}")
    ans_1_2 = c2.text_input("(2) ㄴ (환경 및 방법):", key=f"1_2{r_id}")
    ans_1_3 = c3.text_input("(3) ㄷ (심리 현상):", key=f"1_3{r_id}")
    
    st.markdown('<p class="question-text">[서·논술형 2] 윗글을 활용하여 \'과제 난이도에 따른 효율적인 학습 전략\'에 대한 설명문을 작성하려 한다. 주어진 첫 문장에 이어지는 내용을 &lt;조건&gt;에 맞추어 작성하시오.</p>', unsafe_allow_html=True)
    st.markdown("""
    <table class="info-table">
        <tr>
            <th>주어진 문장</th>
            <td>과제의 특성과 난이도에 따라 우리의 학습 효율을 높이는 방법은 다르게 적용되어야 한다.</td>
        </tr>
        <tr>
            <th>&lt;조건&gt;</th>
            <td>
                ○ 서로 다른 2가지의 설명 방법을 사용하여, 주어진 문장에 이어지는 문장을 (1), (2)에 각각 하나씩 작성할 것.<br>
                ○ 윗글에 제시된 내용만을 활용하여 문장을 구성할 것. (지문에 없는 외부 배경지식을 활용할 경우 인정하지 않음.)<br>
                ○ 각 문장의 끝에 자신이 사용한 설명 방법의 명칭을 괄호에 넣어 표기할 것. (예: (예시), (대조))
            </td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
    c_ans1 = st.text_input("(1)", key=f"2_1{r_id}")
    c_ans2 = st.text_input("(2)", key=f"2_2{r_id}")
    
    st.markdown('<p class="question-text">[서·논술형 3] 윗글을 바탕으로 \'상황에 맞는 학습 공간 선택법\'을 설명하는 영상을 제작하려 한다. 다음 기획안을 보고 물음에 답하시오.</p>', unsafe_allow_html=True)
    st.markdown("""
    <table class="info-table">
        <tr>
            <th>[영상 기획안]</th>
            <td>
                ○ 주제: 사회적 촉진과 억제를 활용한 스마트한 공부법<br>
                ○ 세부 내용 계획<br>
                &nbsp;&nbsp;[장면 1] 쉬운 과제를 할 때<br>
                &nbsp;&nbsp;&nbsp;&nbsp;- 시각 요소: 백색소음이 있는 밝은 도서관에서 친구들과 가볍게 미소 지으며 공부하는 학생들의 모습을 넓은 화면(풀샷)으로 보여줌.<br>
                &nbsp;&nbsp;&nbsp;&nbsp;- 청각 요소: 경쾌하고 리듬감 있는 배경음악과 함께 사람들의 가벼운 발소리와 책장 넘기는 소리를 깔아줌<br>
                &nbsp;&nbsp;[장면 2] 어려운 과제를 할 때<br>
                &nbsp;&nbsp;&nbsp;&nbsp;- 시각 요소: <b>Ⓐ ( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; )</b><br>
                &nbsp;&nbsp;&nbsp;&nbsp;- 청각 요소: <b>Ⓑ ( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; )</b>
            </td>
        </tr>
        <tr>
            <th>&lt;조건&gt;</th>
            <td>
                ○ 윗글을 참고하여 어려운 과제를 할 때 필요한 환경의 특성이 잘 드러나도록 Ⓐ와 Ⓑ에 들어갈 연출 계획을 세울 것.<br>
                ○ 자신이 설정한 시각/청각 요소가 글의 내용을 전달하는 데 어떤 효과가 있는지 각각 서술할 것.
            </td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
    ans_3_v = st.text_input("(1) 시각 요소(Ⓐ):", key=f"3_1{r_id}")
    ans_3_v_eff = st.text_input("시각 요소(Ⓐ)의 효과:", key=f"3_1_eff{r_id}")
    ans_3_a = st.text_input("(2) 청각 요소(Ⓑ):", key=f"3_2{r_id}")
    ans_3_a_eff = st.text_input("청각 요소(Ⓑ)의 효과:", key=f"3_2_eff{r_id}")

    if st.button("제출하기", type="primary", key="btn_1"):
        errors = []
        if not (('어려' in ans_1_1 or '복잡' in ans_1_1 or '도전' in ans_1_1) and '과제' in ans_1_1):
            errors.append({"문항": "[서·논술형 1] (1) ㄱ", "포인트": "과제의 특성 요약 (지나치게 어렵거나 도전이 필요한 과제)", "부족": "지문에서 대조되는 어려운 과제의 특성 원형 요약이 누락되었습니다."})
        if not ('혼자' in ans_1_2 and ('집중' in ans_1_2 or '차분' in ans_1_2)):
            errors.append({"문항": "[서·논술형 1] (2) ㄴ", "포인트": "효율적인 환경 도출 (차분하게 혼자 집중하는 시간)", "부족": "어려운 과제를 해결하는 방법으로 '혼자 차분하게 집중'한다는 핵심 지문 근거가 빠져 있습니다."})
        if normalize(ans_1_3) != "사회적억제":
            errors.append({"문항": "[서·논술형 1] (3) ㄷ", "포인트": "심리학 용어 개념 매칭 (사회적 억제)", "부족": "사회적 촉진과 대조되는 정확한 개념 용어인 '사회적 억제'가 올바르게 입력되지 않았습니다."})
            
        m1 = re.search(r'\(([^)]+)\)', c_ans1)
        m2 = re.search(r'\(([^)]+)\)', c_ans2)
        if not (m1 and m2):
            errors.append({"문항": "[서·논술형 2]", "포인트": "설명 방법 조건 사용 및 문장 끝 괄호 표기 요건 준수", "부족": "각 문장 끝 괄호 안에 활용한 설명 방법의 명칭을 명시하는 규칙(예: (예시), (대조))을 충족하지 못했습니다."})
            
        if not (('혼자' in ans_3_v or '독립' in ans_3_v or '방' in ans_3_v) and ('조용' in ans_3_a or '소음' in ans_3_a or '고요' in ans_3_a) and len(ans_3_v_eff) > 5 and len(ans_3_a_eff) > 5):
            errors.append({"문항": "[서·논술형 3]", "포인트": "매체 복합양식성 고려 및 지문 연계 효과 기술", "부족": "어려운 과제에 알맞은 시청각 요소(독방, 조용함 등)와 그것이 내용을 전달하는 인과적 효과 기술이 부족합니다."})

        st.session_state.wrong_details[1] = errors
        st.markdown("#### 🎯 채점 결과 리포트")
        if not errors:
            st.session_state.resolved[1] = True
            st.success("🎉 모든 조건을 완벽하게 충족하셨습니다!")
            st.balloons()
        else:
            st.session_state.resolved[1] = False
            st.error(f"❌ 감점 혹은 조건 미충족 사항이 발견되었습니다.")

    with st.expander("📖 문제 1 모범답안 보기"):
        st.markdown("""
        - **[서·논술형 1]** (1) ㄱ: 지나치게 어렵거나 도전이 필요한 과제 / (2) ㄴ: 차분하게 혼자 집중하는 시간을 가짐 / (3) ㄷ: 사회적 억제
        - **[서·논술형 2]** - (1) 예를 들어 비교적 쉬운 과제나 취미생활은 커피숍이나 도서관에서 남들과 함께 할 때 효율이 오른다. **(예시)**
          - (2) 반면 지나치게 어렵거나 도전이 필요한 과제는 다른 사람과 함께하는 대신 차분히 혼자 집중해야 한다. **(대조)**
        - **[서·논술형 3]**
          - (1) 시각 요소(Ⓐ): 혼자만 있는 차분하고 독립된 공부방 배경을 클로즈업하여 보여준다. / 효과: 다른 사람의 시선이 차단되어 혼자 집중해야 하는 과제 환경을 명확히 시각화하여 전달한다.
          - (2) 청각 요소(Ⓑ): 백색소음이나 주변 소리를 모두 없애고 고요한 침묵을 유지한다. / 효과: 지나치게 어려운 문제를 풀 때 소음을 통제함으로써 차분하게 마인드 컨트롤을 할 수 있도록 유도한다.
        """)

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
    
    st.markdown('<p class="question-text">[서·논술형 1] 윗글을 요약하여 표로 정리하였다. ㄱ~ㄷ에 들어갈 내용을 찾아 쓰시오.</p>', unsafe_allow_html=True)
    st.markdown("""
    <table class="info-table">
        <tr>
            <th>대상</th>
            <th>물의 상태에 비유</th>
            <th>전하의 상태</th>
            <th>위험성</th>
        </tr>
        <tr>
            <td>실생활 전기</td>
            <td>흐르는 물</td>
            <td>전하가 이동함</td>
            <td>감전 등의 위험이 있음</td>
        </tr>
        <tr>
            <td>정전기</td>
            <td><b>[  ㄱ  ]</b></td>
            <td><b>[  ㄴ  ]</b></td>
            <td><b>[  ㄷ  ]</b></td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    ans_2_1_1 = c1.text_input("(1) ㄱ (물의 상태 비유):", key=f"2_1_1{r_id}")
    ans_2_1_2 = c2.text_input("(2) ㄴ (전하의 상태):", key=f"2_1_2{r_id}")
    ans_2_1_3 = c3.text_input("(3) ㄷ (위험성 여부):", key=f"2_1_3{r_id}")

    st.markdown('<p class="question-text">[서·논술형 2] 윗글을 활용하여 \'정전기의 특징\'에 대한 설명문을 작성하려 한다. 주어진 첫 문장에 이어지는 내용을 &lt;조건&gt;에 맞추어 작성하시오.</p>', unsafe_allow_html=True)
    st.markdown("""
    <table class="info-table">
        <tr>
            <th>주어진 문장</th>
            <td>겨울철에 흔히 겪는 정전기는 우리가 평소 집에서 사용하는 전기와는 다른 뚜렷한 특징이 있다.</td>
        </tr>
        <tr>
            <th>&lt;조건&gt;</th>
            <td>
                ○ 주어진 문장에 이어지는 문장을 (1), (2)에 각각 하나씩 작성할 것.<br>
                ○ (1)과 (2)에는 서로 다른 설명 방법이 1가지 이상 활용되어야 하며, 각 문장에 사용된 설명 방법의 명칭을 괄호에 넣어 문장 끝에 기재할 것.<br>
                ○ 윗글에 제시된 내용만을 활용하고, 두 문장이 논리적 흐름을 갖고 이어지도록 할 것.
            </td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
    ans_2_2_1 = st.text_input("(1)", key=f"2_2_1{r_id}")
    ans_2_2_2 = st.text_input("(2)", key=f"2_2_2{r_id}")

    st.markdown('<p class="question-text">[서·논술형 3] 윗글을 바탕으로 \'정전기의 특징\'을 설명하는 영상을 제작하려 한다. 다음 기획안을 보고 물음에 답하시오.</p>', unsafe_allow_html=True)
    st.markdown("""
    <table class="info-table">
        <tr>
            <th>[영상 기획안]</th>
            <td>
                ○ 주제: 전압은 높지만 위험하지 않은 정전기의 비밀<br>
                ○ 세부 내용 계획<br>
                &nbsp;&nbsp;[장면 1] 실생활 전기 (흐르는 물)<br>
                &nbsp;&nbsp;&nbsp;&nbsp;- 시각 요소: 거대한 폭포수가 콸콸 쏟아져 내려오며 물레방아를 힘차게 돌리는 역동적인 그래픽을 보여줌.<br>
                &nbsp;&nbsp;&nbsp;&nbsp;- 청각 요소: 물이 거세게 부딪히는 웅장하고 큰 소리를 배경음으로 사용함.<br>
                &nbsp;&nbsp;[장면 2] 정전기 (고여 있는 물)<br>
                &nbsp;&nbsp;&nbsp;&nbsp;- 시각 요소: <b>Ⓐ ( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; )</b><br>
                &nbsp;&nbsp;&nbsp;&nbsp;- 청각 요소: <b>Ⓑ ( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; )</b>
            </td>
        </tr>
        <tr>
            <th>&lt;조건&gt;</th>
            <td>
                ○ 윗글을 바탕으로 정전기의 특성이 잘 드러나도록 Ⓐ와 Ⓑ에 들어갈 연출 계획을 세울 것.<br>
                ○ 설정한 시각 및 청각 요소의 연출 효과를 각각 서술하되, 반드시 윗글의 내용을 근거로 포함할 것.
            </td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
    ans_2_3_v = st.text_input("(1) 시각 요소(Ⓐ):", key=f"2_3_v{r_id}")
    ans_2_3_v_eff = st.text_input("시각 요소(Ⓐ)의 효과:", key=f"2_3_v_eff{r_id}")
    ans_2_3_a = st.text_input("(2) 청각 요소(Ⓑ):", key=f"2_3_a{r_id}")
    ans_2_3_a_eff = st.text_input("청각 요소(Ⓑ)의 효과:", key=f"2_3_a_eff{r_id}")

    if st.button("제출하기", type="primary", key="btn_2"):
        errors = []
        if not ('고여' in ans_2_1_1 or '갇혀' in ans_2_1_1):
            errors.append({"문항": "[서·논술형 1] (1) ㄱ", "포인트": "비유법 이해 (높은 곳에 고여 있는 물)", "부족": "실생활 전하와 대조되는 정전기 고유의 비유 표현인 '높은 곳에 고여 있는 물'이 기술되지 않았습니다."})
        if not ('이동하지' in ans_2_1_2 or '머물' in ans_2_1_2 or '정지' in ans_2_1_2) or '흐르는' in ans_2_1_2:
            errors.append({"문항": "[서·논술형 1] (2) ㄴ", "포인트": "개념 속성 추출 (전하가 이동하지 않고 머물러 있음)", "부족": "한자 '정'의 의미와 연계된 전하의 정지 상태 및 머무름 속성이 누락되었습니다."})
        if not ('위험하지' in ans_2_1_3 or '안전' in ans_2_1_3 or '피해가없' in normalize(ans_2_1_3)):
            errors.append({"문항": "[서·논술형 1] (3) ㄷ", "포인트": "지문 인과 관계 판단 (위험하지 않음 / 별 피해가 없음)", "부족": "전하가 이동하지 않기 때문에 도출되는 결론인 '위험하지 않음'이 나타나지 않았습니다."})
            
        m1 = re.search(r'\(([^)]+)\)', ans_2_2_1)
        m2 = re.search(r'\(([^)]+)\)', ans_2_2_2)
        if not (m1 and m2):
            errors.append({"문항": "[서·논술형 2]", "포인트": "설명 기법 명칭 괄호 표기 일치 여부", "부족": "조건에 규정된 설명 방법 명칭(예: (정의), (비교))을 문장 끝 괄호에 기입하지 않았거나 구조가 부적절합니다."})
            
        if not (('댐' in ans_2_3_v or '호수' in ans_2_3_v or '고여' in ans_2_3_v) and ('고요' in ans_2_3_a or '침묵' in ans_2_3_a)) or '폭포' in ans_2_3_a:
            errors.append({"문항": "[서·논술형 3]", "포인트": "정적 속성의 시청각적 시각화 및 지문 유기성", "부족": "정전기의 본질인 '고여 있고 움직이지 않음'을 형상화할 시청각 계획 및 효과가 일반 전기(폭포)의 성격과 혼동되었습니다."})

        st.session_state.wrong_details[2] = errors
        st.markdown("#### 🎯 채점 결과 리포트")
        if not errors:
            st.session_state.resolved[2] = True
            st.success("🎉 모든 조건을 완벽하게 충족하셨습니다!")
            st.balloons()
        else:
            st.session_state.resolved[2] = False
            st.error(f"❌ 감점 혹은 조건 미충족 사항이 발견되었습니다.")

    with st.expander("📖 문제 2 모범답안 보기"):
        st.markdown("""
        - **[서·논술형 1]** (1) ㄱ: 높은 곳에 고여 있는 물 / (2) ㄴ: 전하가 이동하지 않고 머물러 있음 / (3) ㄷ: 위험하지 않음 (별 피해가 없음)
        - **[서·논술형 2]**
          - (1) 정전기란 전하가 정지 상태로 있어 그 분포가 시간적으로 변화하지 않는 전기를 말한다. **(정의)**
          - (2) 우리가 쓰는 전기가 흐르는 물이라면 정전기는 높은 곳에 고여 있는 물과 같다. **(비교)**
        - **[서·논술형 3]**
          - (1) 시각 요소(Ⓐ): 높은 산정호수나 댐에 가득 차서 잔잔하게 멈추어 있는 맑은 물의 전경을 보여준다. / 효과: 전하가 이동하지 않고 멈추어 가만히 고여 있는 정전기의 상태적 비유를 직관적으로 전달한다.
          - (2) 청각 요소(Ⓑ): 물 흐르는 소리를 완전히 소거하고 산속의 고요한 새소리나 미풍 소리만 잔잔하게 깔아준다. / 효과: 전하가 흐르지 않아 안전하고 조용한 전기적 상태를 청각적으로 부각한다.
        """)

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
    
    st.markdown('<p class="question-text">[서·논술형 1] 윗글을 요약하여 표로 정리하였다. ㄱ~ㄷ에 들어갈 내용을 찾아 쓰시오.</p>', unsafe_allow_html=True)
    st.markdown("""
    <table class="info-table">
        <tr>
            <th>대상</th>
            <th>올림픽 경기에 비유</th>
            <th>예술로 볼 수 있는가 (근거 포함하여 쓰기)</th>
            <th>예술로서의 가치</th>
        </tr>
        <tr>
            <td>인간의 예술</td>
            <td>인간 선수의 노력과 열정이 담긴 올림픽 경기</td>
            <td>작가의 경험, 관점, 환경이 담겨 있으므로 예술이다.</td>
            <td>감상자에게 남다른 감동을 줌</td>
        </tr>
        <tr>
            <td>인공 지능의 예술</td>
            <td><b>[  ㄱ  ]</b></td>
            <td><b>[  ㄴ  ]</b></td>
            <td><b>[  ㄷ  ]</b></td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    ans_3_1_1 = c1.text_input("(1) ㄱ (올림픽 경기 비유):", key=f"3_1_1{r_id}")
    ans_3_1_2 = c2.text_input("(2) ㄴ (예술 가능 여부 및 근거):", key=f"3_1_2{r_id}")
    ans_3_1_3 = c3.text_input("(3) ㄷ (예술로서의 가치):", key=f"3_1_3{r_id}")

    st.markdown('<p class="question-text">[서·논술형 2] 윗글을 활용하여 \'인공 지능이 그린 그림을 바라보는 시각\'에 대한 설명문을 작성하려 한다. 주어진 첫 문장에 이어지는 내용을 &lt;조건&gt;에 맞추어 작성하시오.</p>', unsafe_allow_html=True)
    st.markdown("""
    <table class="info-table">
        <tr>
            <th>주어진 문장</th>
            <td>인공 지능이 그린 그림이 늘어나는 요즘, 우리는 이 작품들을 어떤 눈으로 바라봐야 할지 올바르게 생각해야 한다.</td>
        </tr>
        <tr>
            <th>&lt;조건&gt;</th>
            <td>
                ○ 주어진 문장에 이어지는 문장을 (1), (2)에 각각 하나씩 작성할 것.<br>
                ○ (1)과 (2)에는 서로 다른 설명 방법이 1가지 이상 활용되어야 하며, 각 문장에 사용된 설명 방법의 명칭을 괄호에 넣어 문장 끝에 기재할 것.<br>
                ○ 윗글에 제시된 내용만을 활용하고, (1)과 (2)가 논리적 흐름을 갖고 이어지도록 할 것.
            </td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
    ans_3_2_1 = st.text_input("(1)", key=f"3_2_1{r_id}")
    ans_3_2_2 = st.text_input("(2)", key=f"3_2_2{r_id}")

    st.markdown('<p class="question-text">[서·논술형 3] 윗글을 바탕으로 \'인공 지능이 그린 그림을 바라보는 시각\'을 설명하는 영상을 제작하려 한다. 다음 기획안을 보고 물음에 답하시오.</p>', unsafe_allow_html=True)
    st.markdown("""
    <table class="info-table">
        <tr>
            <th>[영상 기획안]</th>
            <td>
                ○ 주제: 인간의 감정이 담긴 진정한 예술의 가치<br>
                ○ 세부 내용 계획<br>
                &nbsp;&nbsp;[장면 1] 감정이 없는 완벽한 기술<br>
                &nbsp;&nbsp;&nbsp;&nbsp;- 시각 요소: 로봇이 한 번의 실수 없이 완벽하게 피겨 스케이팅을 해내지만 우리의 마음을 울리지는 못하는 동영상을 보여줌.<br>
                &nbsp;&nbsp;&nbsp;&nbsp;- 청각 요소: 기계음이나 일정한 박자의 메트로놈 소리를 깔아 차갑고 정형화된 분위기를 조성함.<br>
                &nbsp;&nbsp;[장면 2] 마음에 울림을 주는 진정한 예술<br>
                &nbsp;&nbsp;&nbsp;&nbsp;- 시각 요소: <b>Ⓐ ( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; )</b><br>
                &nbsp;&nbsp;&nbsp;&nbsp;- 청각 요소: <b>Ⓑ ( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; )</b>
            </td>
        </tr>
        <tr>
            <th>&lt;조건&gt;</th>
            <td>
                ○ 윗글을 바탕으로 인간이 만들어내는 예술의 특성이 잘 드러나도록 Ⓐ와 에 들어갈 연출 계획을 세울 것.<br>
                ○ 설정한 시각 및 청각 요소의 연출 효과를 각각 서술하되, 반드시 윗글의 내용을 근거로 포함할 것.
            </td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
    ans_3_3_v = st.text_input("(1) 시각 요소(Ⓐ):", key=f"3_3_v{r_id}")
    ans_3_3_v_eff = st.text_input("시각 요소(Ⓐ)의 효과:", key=f"3_3_v_eff{r_id}")
    ans_3_3_a = st.text_input("(2) 청각 요소(Ⓑ):", key=f"3_3_a{r_id}")
    ans_3_3_a_eff = st.text_input("청각 요소(Ⓑ)의 효과:", key=f"3_3_a_eff{r_id}")

    if st.button("제출하기", type="primary", key="btn_3"):
        errors = []
        if not ('로봇' in ans_3_1_1 and '피겨' in ans_3_1_1):
            errors.append({"문항": "[서·논술형 1] (1) ㄱ", "포인트": "비유적 대응 유추 (로봇이 실수 없이 완벽하게 해내는 피겨 스케이팅)", "부족": "지문 속에서 인공지능에 일치시켜 비유한 대상인 '로봇의 피겨 스케이팅' 내용이 유실되었습니다."})
        if not (('아니다' in ans_3_1_2 or '어렵다' in ans_3_1_2) and ('감정' in ans_3_1_2 or '철학' in ans_3_1_2 or '이야기' in ans_3_1_2)):
            errors.append({"문항": "[서·논술형 1] (2) ㄴ", "포인트": "판단 결과와 명확한 본문 근거 기술 (예술로 보기 어려움 - 감정과 철학 부재)", "부족": "감정이나 독자적 철학이 없기 때문에 예술로 보기 어렵다는 인과적 근거 서술이 충족되지 않았습니다."})
        if not ('변화' in ans_3_1_3 or '확장' in ans_3_1_3 or '상징' in ans_3_1_3):
            errors.append({"문항": "[서·논술형 1] (3) ㄷ", "포인트": "대상의 가치 및 의의 서술 (미술계 변화 / 예술 범주 확장 / 상징적 가치)", "부족": "인공지능 작품이 가지는 가치인 '미술계의 변화 초래' 또는 '예술 범주 확장'의 의미 규정이 미흡합니다."})
            
        m1 = re.search(r'\(([^)]+)\)', ans_3_2_1)
        m2 = re.search(r'\(([^)]+)\)', ans_3_2_2)
        if not (m1 and m2):
            errors.append({"문항": "[서·논술형 2]", "포인트": "국어과 설명 기법 활용 및 지정 문장 구조화", "부족": "문장 끝 괄호 서식 조건 및 두 문장 간의 유기적 논리 흐름 형성이 조건에 부합하지 않습니다."})
            
        if not (('인간' in ans_3_3_v or '선수' in ans_3_3_v or '땀' in ans_3_3_v) and ('음악' in ans_3_3_a or '환호' in ans_3_3_a or '박수' in ans_3_3_a)) or '기계음' in ans_3_3_a:
            errors.append({"문항": "[서·논술형 3]", "포인트": "인간 고유의 감성/노력에 대응하는 미디어 연출 기획", "부족": "인간 예술 고유의 가치인 감정, 노력, 열정이 살아나는 미디어 구성안과 마음의 울림 효과가 올바르게 드러나지 않았습니다."})

        st.session_state.wrong_details[3] = errors
        st.markdown("#### 🎯 채점 결과 리포트")
        if not errors:
            st.session_state.resolved[3] = True
            st.success("🎉 모든 조건을 완벽하게 충족하셨습니다!")
            st.balloons()
        else:
            st.session_state.resolved[3] = False
            st.error(f"❌ 감점 혹은 조건 미충족 사항이 발견되었습니다.")

    with st.expander("📖 문제 3 모범답안 보기"):
        st.markdown("""
        - **[서·논술형 1]** (1) ㄱ: 로봇이 한 번의 실수 없이 완벽하게 피겨 스케이팅을 해내는 것 / (2) ㄴ: 감정도 느끼지 못하고 독자적인 철학이나 이야기가 없기 때문에 예술로 보기 어렵다 / (3) ㄷ: 미술계에 큰 변화를 가져오고 예술의 범주를 확장할 수 있는 상징적 가치
        - **[서·논술형 2]**
          - (1) 인간이 만든 예술이란 작가의 고유한 감정이나 철학, 살아온 경험 등이 종합적으로 담겨 마음을 울리는 것을 뜻한다. **(정의)**
          - (2) 반면 인공 지능은 감정이 전혀 없고 독자적인 이야기가 없으므로 인간의 예술과 차이가 있다. **(대조)**
        - **[서·논술형 3]**
          - (1) 시각 요소(Ⓐ): 올림픽 경기에서 피와 땀을 흘리며 열정적으로 연기한 뒤 관객들의 환호 속에 눈물을 흘리는 인간 선수의 얼굴을 클로즈업한다. / 효과: 작가의 치열한 노력과 고유한 감정이 예술의 본질임을 극적으로 각인시킨다.
          - (2) 청각 요소(Ⓑ): 가슴을 울리는 웅장한 오케스트라 선율 위에 관객들의 뜨거운 박수와 거친 숨소리를 입힌다. / 효과: 기계적 정형성과 대조되는 인간 고유의 감정선과 생명력을 청각적으로 전달하여 마음의 울림(감동)을 유발한다.
        """)

# ==============================================================================
# [📚 복습할 내용]
# ==============================================================================
with tab4:
    st.markdown("### 📚 오답 노트 및 맞춤형 조건 피드백")
    total_errors = sum(len(st.session_state.wrong_details[i]) for i in [1, 2, 3])
    
    if total_errors == 0:
        st.info("💡 제출 버튼을 누른 문제 중, 조건을 충족하지 못한 문제가 있을 때 여기에 핵심 복습 가이드와 내 답안의 부족한 점이 실시간으로 표시됩니다. 먼저 문제를 풀고 '제출하기'를 진행해 주세요!")
    else:
        st.warning(f"⚠️ 현재 보완해야 할 조건 미충족 사항이 {total_errors}개 있습니다. 피드백을 확인한 후 다시 작성해 보세요.")
        
        for q_num in [1, 2, 3]:
            if st.session_state.wrong_details[q_num]:
                st.markdown(f"#### 🔍 [문제 {q_num}]번 세부 미흡 사항 안내")
                for detail in st.session_state.wrong_details[q_num]:
                    with st.expander(f"📌 {detail['문항']} 보기 조건 피드백", expanded=True):
                        st.markdown(f"**💡 해당 개념 핵심 복습 포인트:**\n> {detail['포인트']}")
                        st.markdown(f"**❌ 내 답안의 부족한 부분:**\n> <span style='color:#E74C3C; font-weight:600;'>{detail['부족']}</span>", unsafe_allow_html=True)
                for detail in st.session_state.wrong_details[q_num]:
                    with st.expander(f"📌 {detail['문항']} 보기 조건 피드백", expanded=True):
                        st.markdown(f"**💡 해당 개념 핵심 복습 포인트:**\n> {detail['포인트']}")
                        st.markdown(f"**❌ 내 답안의 부족한 부분:**\n> <span style='color:#E74C3C; font-weight:600;'>{detail['부족']}</span>", unsafe_allow_html=True)
