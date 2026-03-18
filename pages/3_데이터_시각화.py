import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
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
st.title("📊 데이터 시각화")

# 샘플 데이터 생성
data = {
    '카테고리': ['제품 A', '제품 B', '제품 C', '제품 D'],
    '판매량': [120, 150, 100, 180],
    '수익': [2400, 3000, 2000, 3600],
    '비율': [20, 25, 17, 38]
}
df = pd.DataFrame(data)

# 데이터 표
st.header("📋 데이터 표")
st.dataframe(df)

# 막대 그래프
st.header("📈 막대 그래프")
fig_bar = px.bar(df, x='카테고리', y='판매량', title='카테고리별 판매량', labels={'판매량': '판매량 (개)', '카테고리': '카테고리'})
fig_bar.update_layout(font=dict(family='Noto Sans KR'))
st.plotly_chart(fig_bar)

# 선 그래프
st.header("📉 선 그래프")
fig_line = px.line(df, x='카테고리', y='수익', title='카테고리별 수익 추이', labels={'수익': '수익 (원)', '카테고리': '카테고리'})
fig_line.update_layout(font=dict(family='Noto Sans KR'))
st.plotly_chart(fig_line)

# 파이 차트
st.header("🥧 파이 차트")
fig_pie = px.pie(df, values='비율', names='카테고리', title='카테고리별 비율')
fig_pie.update_layout(font=dict(family='Noto Sans KR'))
st.plotly_chart(fig_pie)

# 산점도
st.header("🔵 산점도")
fig_scatter = px.scatter(df, x='판매량', y='수익', title='판매량 vs 수익', labels={'판매량': '판매량 (개)', '수익': '수익 (원)'})
fig_scatter.update_layout(font=dict(family='Noto Sans KR'))
st.plotly_chart(fig_scatter)
