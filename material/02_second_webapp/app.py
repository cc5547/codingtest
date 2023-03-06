# streamlit 라이브러리 호출
# 상대경로 복사 : material/02_second_webapp/app.py
import streamlit as st
# 은행 이자 계산기

start_picture = "https://i.imgur.com/D7uu8FN.jpg"
# , use_column_width = True << 가운데 정렬
# st.number_input(label, value) << 데이터 입력

start_ment = "# 은행 이자 계산기"

st.write(start_ment)
st.image(start_picture, width=300, height=200)



# 적금 사진 링크

# start_img = "https://i.imgur.com/D7uu8FN.jpg"
# st.image(
#   "https://i.imgur.com/D7uu8FN.jpg"  width="300" height="200"

    
#     use_column_width=True
#     # 유튜브 사진 // "https://blog.kakaocdn.net/dn/JvPqb/btqAiWpd8sf/Ah9IYr6lDRBb8oxSCJYQyK/img.png"
#   )
