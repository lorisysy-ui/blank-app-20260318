import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import base64

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
st.title("📈 데이터 분석")

# 평균 및 편차 계산
st.header("🧮 평균 및 편차 계산")
st.write("값들을 입력하면 평균과 표준편차를 자동으로 계산합니다.")

col1, col2 = st.columns([3, 1])
with col1:
    st.write("**값 입력** (쉼표로 구분)")
    values_input = st.text_area("예) 10, 20, 30, 40, 50", key="values_input")

if values_input:
    try:
        # 입력값 파싱
        values = [float(x.strip()) for x in values_input.split(',') if x.strip()]
        
        if values:
            # 계산
            mean = np.mean(values)
            std = np.std(values, ddof=1) if len(values) > 1 else 0
            
            # 결과 표시
            st.success("✅ 계산 완료")
            
            result_col1, result_col2, result_col3 = st.columns(3)
            with result_col1:
                st.metric("평균", f"{mean:.2f}")
            with result_col2:
                st.metric("표준편차", f"{std:.2f}")
            with result_col3:
                st.metric("데이터 개수", len(values))
            
            # 상세 통계
            with st.expander("📊 상세 통계"):
                stats_df = pd.DataFrame({
                    '통계': ['최소값', '제1사분위수', '중앙값', '제3사분위수', '최대값'],
                    '값': [
                        np.min(values),
                        np.percentile(values, 25),
                        np.median(values),
                        np.percentile(values, 75),
                        np.max(values)
                    ]
                })
                st.dataframe(stats_df.style.format({'값': '{:.2f}'}), use_container_width=True)
            
            # 분포 시각화
            st.write("**값의 분포**")
            fig_hist = px.histogram(x=values, nbins=10, title='데이터 분포', labels={'x': '값', 'count': '개수'})
            fig_hist.update_layout(font=dict(family='Noto Sans KR'))
            st.plotly_chart(fig_hist)
        else:
            st.warning("⚠️ 유효한 값을 입력해주세요.")
    except ValueError:
        st.error("❌ 입력 형식이 잘못되었습니다. 숫자를 쉼표로 구분해서 입력해주세요.")
