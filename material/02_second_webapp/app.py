# streamlit 라이브러리 호출
# 상대경로 복사 : material/02_second_webapp/app.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("데이터 시각화 예제")

# 데이터 생성
df = pd.DataFrame({
    'x': np.random.randn(1000),
    'y': np.random.randn(1000),
    'category': pd.Categorical(np.random.choice(['A', 'B', 'C'], 1000))
})

# 그래프 그리기
fig = px.scatter(df, x='x', y='y', color='category')
st.plotly_chart(fig)

# 표 그리기
st.subheader("데이터 표시")
st.write(df)