import streamlit as st
import re

st.set_page_config(page_title="중등 국어 서논술형 자동 채점기", layout="wide")

st.title("📝 2회 시험 대비 서·논술형 답안 자동 채점 시스템")
st.markdown("---")

# 세트 선택 세션
set_option = st.sidebar.selectbox(
    "채점할 문항 세트를 선택하세요",
    ["[1번 세트] 사회적 촉진과 억제", "[2번 세트] 정전기의 특징", "[3번 세트] AI 그림과 예술"]
)

# 텍스트 정규화 함수 (공백 제거 및 소문자화, 특수문자 제거로 매칭률 향상)
def normalize(text):
    return re.sub(r'\s+', '', text).strip()

# ==============================================================================
# [1번 세트] 채점 로직
# ==============================================================================
if set_option == "[1번 세트] 사회적 촉진과 억제":
    st.header("📌 [1번 세트] 사회적 촉진과 억제 채점")
    
    col1, col2 = st.columns(2)
    with col1:
        ans_1_1 = st.text_input("[서·논술형 1] (1) 과제의 특성 빈칸", placeholder="예: 비교적 쉬운 취미 생활이나...")
        ans_1_2 = st.text_input("[서·논술형 1] (2) 효율적인 환경 및 방법 빈칸", placeholder="예: 차분하게 혼자 집중하는 시간을 가짐")
        ans_1_3 = st.text_input("[서·논술형 1] (3) 관련된 심리 현상 빈칸", placeholder="예: 사회적 억제")
    with col2:
        ans_2_1 = st.text_input("[서·논술형 2] (1) 첫 번째 문장 + (설명방법)", placeholder="예: 예를 들어... (예시)")
        ans_2_2 = st.text_input("[서·논술형 2] (2) 두 번째 문장 + (설명방법)", placeholder="예: 반면... (대조)")
    
    st.subheader("[서·논술형 3] 영상 기획안")
    col3, col4 = st.columns(2)
    with col3:
        ans_3_v = st.text_area("(1) 시각 요소(Ⓐ) 및 효과", placeholder="시각 요소: ... \n시각 요소의 효과: ...")
    with col4:
        ans_3_a = st.text_area("(2) 청각 요소(Ⓑ) 및 효과", placeholder="청각 요소: ... \n청각 요소의 효과: ...")

    if st.button("1번 세트 채점하기", type="primary"):
        st.subheader("📊 채점 결과 리포트")
        total_score = 0
        
        # [서·논술형 1] 채점 (총 3점)
        n_1_1 = normalize(ans_1_1)
        if ('쉬운' in ans_1_1 or '낮은' in ans_1_1 or '노력' in ans_1_1) and ('과제' in ans_1_1 or '취미' in ans_1_1 or '일' in ans_1_1):
            st.success("✅ [1-1] 정답 (1.0 / 1.0점)")
            total_score += 1
        else:
            st.error("❌ [1-1] 오답 (0.0 / 1.0점) - '쉬운 과제/취미'의 의미가 누락되었습니다.")
            
        if '혼자' in ans_1_2 and ('집중' in ans_1_2 or '차분' in ans_1_2 or '시간' in ans_1_2):
            if '도서관' in ans_1_2 or '모임' in ans_1_2: # 오개념 방지 규칙
                st.error("❌ [1-2] 오답 (0.0 / 1.0점) - 오개념 발견: 어려운 과제에 '모임/도서관 함께함' 특성을 부여했습니다.")
            else:
                st.success("✅ [1-2] 정답 (1.0 / 1.0점)")
                total_score += 1
        else:
            st.error("❌ [1-2] 오답 (0.0 / 1.0점) - '혼자 집중'의 핵심 내용이 없습니다.")
            
        if n_1_1 == "사회적억제":
            st.success("✅ [1-3] 정답 (1.0 / 1.0점)")
            total_score += 1
        elif "억제" in ans_1_3:
            st.warning("⚠️ [1-3] 부분점수 (0.5 / 1.0점) - '사회적 억제' 용어 확인 필요 (맞춤법 유의)")
            total_score += 0.5
        else:
            st.error("❌ [1-3] 오답 (0.0 / 1.0점) - 고유 용어 '사회적 억제'가 아닙니다.")

        # [서·논술형 2] 채점 (총 4점, 각 2점)
        for idx, ans_2 in enumerate([ans_2_1, ans_2_2], 1):
            method_match = re.search(r'\(([^)]+)\)', ans_2)
            if method_match:
                method = normalize(method_match.group(1))
                # 방법의 특성 및 결론 방향 확인
                if "예시" in method and ('예를들어' in normalize(ans_2) or '예로' in normalize(ans_2)):
                    st.success(f"✅ [2-{idx}] 정답 [예시] (2.0 / 2.0점)")
                    total_score += 2
                elif ("대조" in method or "비교" in method) and ('반면' in normalize(ans_2) or '달리' in normalize(ans_2) or '혼자' in normalize(ans_2)):
                    st.success(f"✅ [2-{idx}] 정답 [대조/비교] (2.0 / 2.0점)")
                    total_score += 2
                else:
                    st.error(f"❌ [2-{idx}] 오답 (0.0 / 2.0점) - 선택한 설명 방법의 특성이나 결론이 문장에 드러나지 않습니다.")
            else:
                st.error(f"❌ [2-{idx}] 오답 (0.0 / 2.0점) - 문장 끝에 괄호 표기 '(설명방법)'가 누락되었습니다.")

        # [서·논술형 3] 채점 (총 6점, 각 3점)
        # 시각 요소 검증
        if ('혼자' in ans_3_v or '독립' in ans_3_v or '방' in ans_3_v or '독서실' in ans_3_v) and ('효과' in ans_3_v or '전달' in ans_3_v):
            st.success("✅ [3-시각] 정답 (3.0 / 3.0점) - 연출 및 지문 근거 효과 포함")
            total_score += 3
        else:
            st.error("❌ [3-시각] 오답/감점 (0.0 / 3.0점) - '혼자 집중하는 환경' 연출 또는 지문 근거 효과가 미흡합니다.")
            
        # 청각 요소 검증
        if ('조용' in ans_3_a or '소음' in ans_3_a or '잔잔' in ans_3_a or '음악' in ans_3_a) and ('집중' in ans_3_a or '효과' in ans_3_a):
            st.success("✅ [3-청각] 정답 (3.0 / 3.0점) - 연출 및 분위기 효과 포함")
            total_score += 3
        else:
            st.error("❌ [3-청각] 오답/감점 (0.0 / 3.0점) - '정적인 청각 분위기' 연출 혹은 효과가 누락되었습니다.")

        st.metric(label="최종 산출 점수", value=f"{total_score} / 13.0 점")

# ==============================================================================
# [2번 세트] 채점 로직
# ==============================================================================
elif set_option == "[2번 세트] 정전기의 특징":
    st.header("📌 [2번 세트] 정전기의 특징 채점")
    
    col1, col2 = st.columns(2)
    with col1:
        ans_1_1 = st.text_input("[서·논술형 1] (1) 물의 상태 빈칸", placeholder="예: 높은 곳에 고여 있는 물")
        ans_1_2 = st.text_input("[서·논술형 1] (2) 전하의 상태 빈칸", placeholder="예: 이동하지 않고 머물러 있음")
        ans_1_3 = st.text_input("[서·논술형 1] (3) 위험성 빈칸", placeholder="예: 위험하지 않음")
    with col2:
        ans_2_1 = st.text_input("[서·논술형 2] (1) 첫 번째 문장 + (설명방법)", placeholder="예: 정전기란... (정의)")
        ans_2_2 = st.text_input("[서·논술형 2] (2) 두 번째 문장 + (설명방법)", placeholder="예: 실생활 전기는... (대조)")
        
    st.subheader("[서·논술형 3] 영상 기획안")
    col3, col4 = st.columns(2)
    with col3:
        ans_3_v = st.text_area("(1) 시각 요소(Ⓐ) 및 효과")
    with col4:
        ans_3_a = st.text_area("(2) 청각 요소(Ⓑ) 및 효과")

    if st.button("2번 세트 채점하기", type="primary"):
        st.subheader("📊 채점 결과 리포트")
        total_score = 0
        
        # [서·논술형 1] 채점
        if '고여' in ans_1_1 or '갇혀' in ans_1_1 or '멈춘' in ans_1_1:
            st.success("✅ [1-1] 정답 (1.0 / 1.0점)")
            total_score += 1
        else:
            st.error("❌ [1-1] 오답 (0.0 / 1.0점) - 고여 있거나 정지된 물의 비유가 부족합니다.")
            
        if '이동하지' in ans_1_2 or '머물' in ans_1_2 or '정지' in ans_1_2 or '움직이지' in ans_1_2:
            st.success("✅ [1-2] 정답 (1.0 / 1.0점)")
            total_score += 1
        else:
            st.error("❌ [1-2] 오답 (0.0 / 1.0점) - 전하가 멈춰있다는 핵심 상태 기술 누락.")
            
        if '위험하지' in ans_1_3 or '안전' in ans_1_3 or '피해가없' in normalize(ans_1_3):
            st.success("✅ [1-3] 정답 (1.0 / 1.0점)")
            total_score += 1
        else:
            st.error("❌ [1-3] 오답 (0.0 / 1.0점) - 위험성 판단 결론 오류.")

        # [서·논술형 2] 채점
        for idx, ans_2 in enumerate([ans_2_1, ans_2_2], 1):
            method_match = re.search(r'\(([^)]+)\)', ans_2)
            if method_match:
                method = normalize(method_match.group(1))
                if "정의" in method and ('란' in ans_2 or '말한다' in ans_2 or '뜻한다' in ans_2):
                    st.success(f"✅ [2-{idx}] 정답 [정의] (2.0 / 2.0점)")
                    total_score += 2
                elif ("비교" in method or "대조" in method) and ('물' in ans_2 or '전기' in ans_2):
                    st.success(f"✅ [2-{idx}] 정답 [비교/대조] (2.0 / 2.0점)")
                    total_score += 2
                else:
                    st.error(f"❌ [2-{idx}] 오답 (0.0 / 2.0점) - 설명 방법의 언어적 특성이 문장에 보이지 않습니다.")
            else:
                st.error(f"❌ [2-{idx}] 오답 (0.0 / 2.0점) - 문장 끝 괄호 표기 누락.")

        # [서·논술형 3] 채점
        if ('댐' in ans_3_v or '호수' in ans_3_v or '고여' in ans_3_v or '갇혀' in ans_3_v) and ('이동' in ans_3_v or '머물' in ans_3_v or '효과' in ans_3_v):
            st.success("✅ [3-시각] 정답 (3.0 / 3.0점)")
            total_score += 3
        else:
            st.error("❌ [3-시각] 오답/감점 (0.0 / 3.0점) - '고여 있는 물'의 시각화와 지문 근거(전하 머무름) 부족.")
            
        if ('고요' in ans_3_a or '침묵' in ans_3_a or '소리없' in normalize(ans_3_a)) and ('위험하지' in ans_3_a or '안전' in ans_3_a or '효과' in ans_3_a):
            if '폭포' in ans_3_a or '웅장' in ans_3_a: # 오개념 방지 규칙
                st.error("❌ [3-청각] 오답 (0.0 / 3.0점) - 오개념 발견: 정전기 장면에 폭포나 큰 소리를 연출했습니다.")
            else:
                st.success("✅ [3-청각] 정답 (3.0 / 3.0점)")
                total_score += 3
        else:
            st.error("❌ [3-청각] 오답/감점 (0.0 / 3.0점) - 정적인 분위기 연출 또는 위험성 무해의 근거 부족.")

        st.metric(label="최종 산출 점수", value=f"{total_score} / 13.0 점")

# ==============================================================================
# [3번 세트] 채점 로직
# ==============================================================================
elif set_option == "[3번 세트] AI 그림과 예술":
    st.header("📌 [3번 세트] AI 그림과 예술 채점")
    
    col1, col2 = st.columns(2)
    with col1:
        ans_1_1 = st.text_input("[서·논술형 1] (1) 올림픽 경기에 비유 빈칸", placeholder="예: 로봇이 완벽하게 해내는 피겨 스케이팅 경기")
        ans_1_2 = st.text_input("[서·논술형 1] (2) 예술로 볼 수 있는가 빈칸", placeholder="예: 예술이 아니다. 감정이나 철학이 없기 때문이다.")
        ans_1_3 = st.text_input("[서·논술형 1] (3) 예술로서의 가치 빈칸", placeholder="예: 미술계에 큰 변화를 가져왔고 예술의 범주를 확장함")
    with col2:
        ans_2_1 = st.text_input("[서·논술형 2] (1) 첫 번째 문장 + (설명방법)")
        ans_2_2 = st.text_input("[서·논술형 2] (2) 두 번째 문장 + (설명방법)")
        
    st.subheader("[서·논술형 3] 영상 기획안")
    col3, col4 = st.columns(2)
    with col3:
        ans_3_v = st.text_area("(1) 시각 요소(Ⓐ) 및 효과")
    with col4:
        ans_3_a = st.text_area("(2) 청각 요소(Ⓑ) 및 효과")

    if st.button("3번 세트 채점하기", type="primary"):
        st.subheader("📊 채점 결과 리포트")
        total_score = 0
        
        # [서·논술형 1] 채점
        if '로봇' in ans_1_1 and '피겨' in ans_1_1:
            st.success("✅ [1-1] 정답 (1.0 / 1.0점)")
            total_score += 1
        else:
            st.error("❌ [1-1] 오답 (0.0 / 1.0점) - 대조 비유군인 '로봇의 피겨 스케이팅'이 명시되지 않았습니다.")
            
        if ('어렵다' in ans_1_2 or '아니다' in ans_1_2) and ('감정' in ans_1_2 or '철학' in ans_1_2 or '이야기' in ans_1_2):
            st.success("✅ [1-2] 정답 (1.0 / 1.0점) - 결론 방향과 지문 근거 일치")
            total_score += 1
        else:
            st.error("❌ [1-2] 오답 (0.0 / 1.0점) - 예술 여부 결론 판단 혹은 지문 핵심 근거(감정/철학 부재) 누락.")
            
        if '변화' in ans_1_3 or '확장' in ans_1_3 or '상징' in ans_1_3:
            st.success("✅ [1-3] 정답 (1.0 / 1.0점)")
            total_score += 1
        else:
            st.error("❌ [1-3] 오답 (0.0 / 1.0점) - 지문에 제시된 미술사적 의의 가치 서술 부족.")

        # [서·논술형 2] 채점
        for idx, ans_2 in enumerate([ans_2_1, ans_2_2], 1):
            method_match = re.search(r'\(([^)]+)\)', ans_2)
            if method_match:
                method = normalize(method_match.group(1))
                if "분석" in method and ('감정' in ans_2 or '철학' in ans_2 or '경험' in ans_2 or '요소' in ans_2):
                    st.success(f"✅ [2-{idx}] 정답 [분석] (2.0 / 2.0점)")
                    total_score += 2
                elif "대조" in method and ('반면' in ans_2 or '하지만' in ans_2 or '아니다' in ans_2):
                    st.success(f"✅ [2-{idx}] 정답 [대조] (2.0 / 2.0점)")
                    total_score += 2
                elif ("정의" in method or "예시" in method) and len(normalize(ans_2)) > 10:
                    st.success(f"✅ [2-{idx}] 정답 [정의/예시 의미 통과] (2.0 / 2.0점)")
                    total_score += 2
                else:
                    st.error(f"❌ [2-{idx}] 오답 (0.0 / 2.0점) - 제시된 설명 방법의 특성이 문장에 구현되지 않았습니다.")
            else:
                st.error(f"❌ [2-{idx}] 오답 (0.0 / 2.0점) - 문장 끝 괄호 표기 누락.")

        # [서·논술형 3] 채점
        if ('인간' in ans_3_v or '선수' in ans_3_v) and ('땀' in ans_3_v or '노력' in ans_3_v or '눈물' in ans_3_v) and ('가치' in ans_3_v or '효과' in ans_3_v):
            st.success("✅ [3-시각] 정답 (3.0 / 3.0점)")
            total_score += 3
        else:
            st.error("❌ [3-시각] 오답/감점 (0.0 / 3.0점) - '인간의 노력과 열정' 시각화 혹은 예술적 가치 효과 미흡.")
            
        if ('음악' in ans_3_a or '오케스트라' in ans_3_a or '환호' in ans_3_a or '박수' in ans_3_a) and ('울림' in ans_3_a or '감동' in ans_3_a or '효과' in ans_3_a):
            if '기계음' in ans_3_a or '메트로놈' in ans_3_a: # 오개념 방지 규칙
                st.error("❌ [3-청각] 오답 (0.0 / 3.0점) - 오개념 발견: 진정한 예술 장면에 차가운 기계음/메트로놈을 연출했습니다.")
            else:
                st.success("✅ [3-청각] 정답 (3.0 / 3.0점)")
                total_score += 3
        else:
            st.error("❌ [3-청각] 오답/감점 (0.0 / 3.0점) - 서정적 사운드 연출 혹은 마음의 울림 효과 설명 부족.")

        st.metric(label="최종 산출 점수", value=f"{total_score} / 13.0 점")