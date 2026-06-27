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
    
    /* image_5630fe.png 내 [학생 일기] 등 지문 박스 스타일 구현 */
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
    
    /* image_5630fe.png 내 <조건> 박스 스타일 구현 */
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

# 세션 상태 초기화 (진행 상황 체크용)
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
    st.markdown("## 경쟁도 없는데 왜 집중이 잘 됐을까? — 올포트 vs 트리플렛")
    
    # 지문 영역 (image_5630fe.png 스타일 반영)
    st.markdown("""
    <div class="passage-box">
        <span class="passage-title">[학생 일기]</span> 오늘 카페에 가서 영어 단어를 외웠다. 옆자리에는 모르는 대학생 두 명이 열심히 태블릿을 두드리며 공부하고 있었다. 그 사람들과 내가 같은 시험을 보는 것도 아닌데 이상하게, 나도 가만히 있을 수 없어서 평소보다 단어가 훨씬 잘 외워졌다.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("이 현상은 노먼 트리플렛과 플로이드 올포트 중 누구의 이론으로 더 잘 설명되는지 판단하고, 두 학자의 이론 차이가 드러나게 서술하시오. [6점]")
    
    # 조건 영역 (image_5630fe.png 스타일 반영)
    st.markdown("""
    <div class="condition-container">
        <div class="condition-title">〈조건〉</div>
        <ul class="condition-list">
            <li>🎯 답안은 반드시 두 학자 중 한 명을 고를 것</li>
            <li>🎯 답안 안에 자신이 선택한 학자의 주장이 명확히 제시될 것</li>
            <li>🎯 선택하지 않은 학자의 이론이 왜 이 사례에 맞지 않는지도 한 문장 이상 서술할 것</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # 답안 입력 영역 분리
    st.markdown('<div class="input-label">• 답안 입력</div>', unsafe_allow_html=True)
    ans_1 = st.text_area("답안을 여기에 입력하세요.", key="q_1", label_visibility="collapsed", placeholder="답안을 입력해주세요.")
    
    if st.button("문제 1 채점하기", type="primary"):
        if not ans_1.strip():
            st.warning("답안을 입력한 후 채점 버튼을 눌러주세요.")
        else:
            score = 0
            st.markdown("#### 🎯 채점 결과 및 피드백")
            
            # 1. 학자 선택 여부 및 결론 확인
            if '올포트' in ans_1:
                st.success("✅ [조건 1 통과] '올포트'를 올바르게 선택했습니다.")
                score += 2
                
                # 올포트의 주장 특성 확인
                if '단순' in ans_1 or '존재' in ans_1 or '타인' in ans_1 or '혼자' in ans_1:
                    st.success("✅ [조건 2 통과] 선택한 학자(올포트)의 이론적 특성이 답안에 잘 드러나 있습니다.")
                    score += 2
                else:
                    st.error("❌ [조건 2 미흡] 올포트 이론의 핵심(타인의 단순한 존재가 능률을 높임)에 대한 설명이 부족합니다.")
            
            elif '트리플렛' in ans_1:
                st.error("❌ [결론 오류 / 오개념] 트리플렛은 '경쟁'이나 '협동'이 있을 때 능률이 오른다고 보았으므로, 경쟁이 없는 본 지문의 사례를 설명하기에는 부적절합니다. (오답 처리)")
            else:
                st.error("❌ [조건 1 미흡] '올포트'와 '트리플렛' 중 어떤 학자의 이론에 해당하는지 명시하지 않았습니다.")
                
            # 2. 선택하지 않은 학자 비판 검증
            if '트리플렛' in ans_1 and '경쟁' in ans_1 and '올포트' in ans_1:
                if '올포트' in ans_1 and ('없' in ans_1 or '아님' in ans_1): 
                    st.success("✅ [조건 3 통과] 트리플렛 이론이 이 사례에 맞지 않는 이유(경쟁이 없음)를 논리적으로 서술했습니다.")
                    score += 2
            elif '올포트' in ans_1 and not '트리플렛' in ans_1:
                st.error("❌ [조건 3 미흡] 선택하지 않은 학자(트리플렛)의 이론이 맞지 않는 이유에 대한 서술이 누락되었습니다.")

            if score == 6:
                st.session_state.resolved[1] = True
                st.balloons()

# ==============================================================================
# [문제 2] 정전기의 특징
# ==============================================================================
with tab2:
    st.markdown("## 겨울철 불청객의 비밀 — 흐르지 않는 전기")
    
    st.markdown("""
    <div class="passage-box">
        <span class="passage-title">[과학 에세이]</span> 실생활에서 쓰는 전기가 '흐르는 물'이라면, 정전기는 '높은 곳에 고여 있는 물'과 같습니다. 전하가 이동하지 않고 머물러 있기 때문에 높은 전압을 가졌음에도 우리에게 치명적이거나 위험하지는 않습니다.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("정전기가 지닌 전하의 상태를 지문에 제시된 비유를 활용하여 설명하고, 실생활 전기와의 차이점을 바탕으로 위험성 여부에 대한 결론을 내어 서술하시오. [6점]")
    
    st.markdown("""
    <div class="condition-container">
        <div class="condition-title">〈조건〉</div>
        <ul class="condition-list">
            <li>🎯 '물'과 관련된 지문 속 비유 표현을 그대로 활용할 것</li>
            <li>🎯 전하의 움직임 상태(이동 여부)가 답안에 명확히 포함될 것</li>
            <li>🎯 흐르는 실생활 전기와 대조하여 위험하지 않다는 결론을 정확히 명시할 것</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="input-label">• 답안 입력</div>', unsafe_allow_html=True)
    ans_2 = st.text_area("답안을 여기에 입력하세요.", key="q_2", label_visibility="collapsed", placeholder="답안을 입력해주세요.")

    if st.button("문제 2 채점하기", type="primary"):
        if not ans_2.strip():
            st.warning("답안을 입력한 후 채점 버튼을 눌러주세요.")
        else:
            score = 0
            st.markdown("#### 🎯 채점 결과 및 피드백")
            
            if '고여' in ans_2 or '고인 물' in ans_2:
                st.success("✅ [조건 1 통과] '고여 있는 물' 비유를 적절히 활용했습니다.")
                score += 2
            else:
                st.error("❌ [조건 1 미흡] 지문에 제시된 물의 비유 표현('고여 있는 물')이 나타나 있지 않습니다.")
                
            if '이동하지' in ans_2 or '머물' in ans_2 or '멈춰' in ans_2:
                if '흐르는' in ans_2 and not '실생활' in ans_2:
                    st.error("❌ [오개념 방지] 정전기의 전하 상태 설명에 실생활 전기의 특성('흐름')을 혼동하여 사용했습니다.")
                else:
                    st.success("✅ [조건 2 통과] 전하가 이동하지 않고 머물러 있는 상태를 정확히 기술했습니다.")
                    score += 2
            else:
                st.error("❌ [조건 2 미흡] 전하가 움직이지 않고 멈춰 있다는 상태 설명이 누락되었습니다.")
                
            if '위험하지' in ans_2 or '안전' in ans_2:
                st.success("✅ [조건 3 통과] 실생활 전기와 대조하여 위험하지 않다는 명확한 결론 방향을 제시했습니다.")
                score += 2
            else:
                st.error("❌ [조건 3 미흡] 문장 마지막에 '위험하지 않다'는 최종 결론이 빠져 있습니다.")

            if score == 6:
                st.session_state.resolved[2] = True
                st.balloons()

# ==============================================================================
# [문제 3] AI 그림과 예술
# ==============================================================================
with tab3:
    st.markdown("## 알고리즘 초상화 — 인공지능 작품을 예술로 볼 수 있는가")
    
    st.markdown("""
    <div class="passage-box">
        <span class="passage-title">[비평문 발췌]</span> 인간의 작품에는 작가의 고유한 감정, 철학, 세상을 바라보는 관점이 녹아 있습니다. 반면 인공지능은 데이터 조합 능력이 뛰어날 뿐 독자적인 철학이나 이야기가 없습니다. 그러나 기존 미술계의 범주를 확장했다는 상징적 가치는 분명히 존재합니다.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("인공지능의 그림을 진정한 예술 작품으로 인정하기 어려운 이유를 인간의 작품 특성과 대조하여 서술하고, 그럼에도 불구하고 인정할 수 있는 가치는 무엇인지 서술하시오. [6점]")
    
    st.markdown("""
    <div class="condition-container">
        <div class="condition-title">〈조건〉</div>
        <ul class="condition-list">
            <li>🎯 인간의 작품이 가지는 고유한 구성 요소적 특징이 답안에 드러날 것</li>
            <li>🎯 인공지능에게는 그것(요소)이 왜 부재하는지 대조적 성격으로 밝힐 것</li>
            <li>🎯 마지막 문장에는 인공지능 그림이 지닌 미술사적 가치 결론이 포함될 것</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="input-label">• 답안 입력</div>', unsafe_allow_html=True)
    ans_3 = st.text_area("답안을 여기에 입력하세요.", key="q_3", label_visibility="collapsed", placeholder="답안을 입력해주세요.")

    if st.button("문제 3 채점하기", type="primary"):
        if not ans_3.strip():
            st.warning("답안을 입력한 후 채점 버튼을 눌러주세요.")
        else:
            score = 0
            st.markdown("#### 🎯 채점 결과 및 피드백")
            
            if '감정' in ans_3 or '철학' in ans_3 or '관점' in ans_3:
                st.success("✅ [조건 1 통과] 인간 작품의 특성인 감정 및 철학 요소를 정확히 언급했습니다.")
                score += 2
            else:
                st.error("❌ [조건 1 미흡] 인간 작품만이 지닌 핵심 내적 요소(감정, 철학 등)에 대한 설명이 없습니다.")
                
            if '없' in ans_3 or '부재' in ans_3 or '아니다' in ans_3:
                if '기계음' in ans_3: # 타 단원 오개념 믹스 방지
                    st.error("❌ [오개념 발견] 영상/청각 단원의 개념 키워드('기계음')가 본문 비평문 설명에 잘못 혼용되었습니다.")
                else:
                    st.success("✅ [조건 2 통과] 인공지능에게는 이러한 주체적 감정이나 철학이 없다는 점을 명확히 대조했습니다.")
                    score += 2
            else:
                st.error("❌ [조건 2 미흡] 인공지능에게 해당 요소들이 왜 결여되어 있는지에 대한 대조 설명이 부족합니다.")
                
            if '가치' in ans_3 or '범주' in ans_3 or '확장' in ans_3 or '변화' in ans_3:
                st.success("✅ [조건 3 통과] 예술의 범주 확장 혹은 상징적 가치라는 최종 결론 방향을 올바르게 제시했습니다.")
                score += 2
            else:
                st.error("❌ [조건 3 미흡] 한계점 외에 인공지능 그림이 주는 '미술사적 가치/의의'에 대한 최종 결론 서술이 빠져 있습니다.")

            if score == 6:
                st.session_state.resolved[3] = True
                st.balloons()

# ==============================================================================
# [문제 4] 복습할 내용
# ==============================================================================
with tab4:
    st.markdown("### 📚 대단원 핵심 개념 및 서논술형 가이드")
    st.write("감점 없는 완벽한 서·논술형 답안 작성을 위해 아래 요약표를 꼭 기억해 주세요.")
    
    st.table([
        {"설명 방법": "정의", "핵심 내용": "대상의 본질이나 개념을 명확하게 규정하여 설명함"},
        {"설명 방법": "예시", "핵심 내용": "구체적이고 친숙한 사례를 들어 독자의 이해를 도움"},
        {"설명 방법": "분석", "핵심 내용": "하나의 대상을 구성 요소나 부분으로 쪼개어 설명함"},
        {"설명 방법": "비교와 대조", "핵심 내용": "두 대상 간의 공통점(비교)과 차이점(대조)을 부각함"}
    ])
    
    st.markdown("""
    > 💡 **감점 예방 마지막 점검!**
    > - **조건 지키기:** '학자를 고를 것', '비유를 활용할 것' 등 문제에서 지정한 제한 조건을 빼놓으면 내용이 좋아도 감점됩니다.
    > - **오개념 섞지 않기:** 개념 간의 특징을 명확히 분리하여 엉뚱한 성격(예: 정전기 설명에 흐르는 물의 성격 기술)을 덧붙이지 않도록 주의하세요.
    """)
