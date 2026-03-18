import streamlit as st
import requests
import base64
from googletrans import Translator

# 폰트 파일 로드 및 base64 인코딩
with open("fonts/NotoSansKR-Bold.ttf", "rb") as f:
    font_data = f.read()
font_base64 = base64.b64encode(font_data).decode()

# CSS로 폰트 적용
css = f"""
<style>
@font-face {{
    font-family: 'Noto Sans KR';
    src: url(data:font/ttf;base64,{font_base64}) format('truetype');
}}
body {{
    font-family: 'Noto Sans KR', sans-serif;
}}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# 페이지 제목
st.title("📋 번역기")

# 번역기
st.header("🌐 실시간 번역")

# 텍스트 입력
text_input = st.text_area("번역할 텍스트를 입력하세요", height=100, placeholder="한국어 또는 영어 텍스트를 입력하세요...")

# 번역 버튼
if st.button("🔄 번역", key="translate_button"):
    if text_input.strip():
        try:
            # 번역기 초기화
            translator = Translator()
            
            # 언어 감지
            detected = translator.detect(text_input)
            source_lang = detected.lang
            
            # 번역 방향 결정
            if source_lang == 'ko':
                target_lang = 'en'
                target_name = '영어'
            elif source_lang == 'en':
                target_lang = 'ko'
                target_name = '한국어'
            else:
                # 다른 언어는 영어로 번역
                target_lang = 'en'
                target_name = '영어'
            
            # 번역 실행
            translated = translator.translate(text_input, src=source_lang, dest=target_lang)
            
            # 결과 표시
            st.success("✅ 번역 완료")
            
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("📝 원본 텍스트")
                st.write(f"**감지된 언어**: {source_lang.upper()}")
                st.text_area("원본", text_input, height=100, disabled=True, key="original")
            
            with col2:
                st.subheader(f"🔄 번역 결과 ({target_name})")
                st.text_area("번역", translated.text, height=100, disabled=True, key="translated")
            
            # 추가 정보
            with st.expander("📊 번역 정보"):
                st.write(f"**원본 언어**: {source_lang}")
                st.write(f"**대상 언어**: {target_lang}")
                st.write(f"**신뢰도**: {detected.confidence:.2f}")
                
        except Exception as e:
            st.error(f"❌ 번역 오류: {str(e)}")
            st.info("💡 인터넷 연결을 확인하고 다시 시도해주세요.")
    else:
        st.warning("⚠️ 번역할 텍스트를 입력해주세요.")

# 사용 방법
with st.expander("📖 사용 방법"):
    st.markdown("""
    1. **텍스트 입력**: 번역할 한국어 또는 영어 텍스트를 입력하세요.
    2. **번역 버튼 클릭**: '🔄 번역' 버튼을 눌러 번역을 시작합니다.
    3. **결과 확인**: 왼쪽에 원본, 오른쪽에 번역 결과가 표시됩니다.
    4. **언어 자동 감지**: 입력 언어를 자동으로 감지하여 반대 언어로 번역합니다.
    
    **지원 언어**: 한국어 ↔ 영어
    """)
