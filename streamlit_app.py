import streamlit as st

# 페이지 설정
st.set_page_config(page_title="자기소개", page_icon="👤", layout="wide")

# 제목
st.title("👤 자기소개")

# 프로필 사진 (플레이스홀더)
st.image("https://via.placeholder.com/150", caption="프로필 사진", width=150)

# 기본 정보
st.header("기본 정보")
col1, col2 = st.columns(2)
with col1:
    st.subheader("이름")
    st.write("여기에 이름을 입력하세요")
with col2:
    st.subheader("직업/직위")
    st.write("여기에 직업을 입력하세요")

# 자기소개 텍스트
st.header("자기소개")
st.write("""
여기에 자기소개를 작성하세요. 예를 들어:

안녕하세요! 저는 [이름]입니다. [간단한 소개 문장].

저는 [관심 분야]에 관심이 많으며, [경험]을 가지고 있습니다.
""")

# 기술 스택
st.header("기술 스택")
st.write("여기에 기술 스택을 나열하세요:")
st.markdown("""
- 언어: Python, JavaScript 등
- 프레임워크: Streamlit, React 등
- 도구: Git, Docker 등
""")

# 프로젝트
st.header("프로젝트")
st.write("여기에 주요 프로젝트를 소개하세요:")
st.markdown("""
- **프로젝트 1**: 설명
- **프로젝트 2**: 설명
""")

# 연락처
st.header("연락처")
st.write("연락처 정보를 입력하세요:")
st.markdown("""
- 이메일: example@email.com
- LinkedIn: [링크]
- GitHub: [링크]
""")

# 추가 섹션 (필요시)
st.header("기타")
st.write("추가 정보를 여기에 추가하세요.")
