# # streamlit 라이브러리 호출
# # 상대경로 복사 : material/02_second_webapp/app.py
# import streamlit as st
# # 은행 이자 계산기
# <center>
# st.write("# 은행 이자 계산기")

# # st.img(
# #   <center>
# #   <img src="https://i.imgur.com/D7uu8FN.jpg" width="300" height="200">
# #   </center>
# #   )

# st.image(
#     # <img src="https://imgur.com/D7uu8FN"  width="300" height="200">

#     "https://i.imgur.com/D7uu8FN.jpg"
#     # 유튜브 사진 // "https://blog.kakaocdn.net/dn/JvPqb/btqAiWpd8sf/Ah9IYr6lDRBb8oxSCJYQyK/img.png"
#   )
# </center>
import streamlit as st
import requests
from bs4 import BeautifulSoup

# 사이트 url
url = 'http://support.lawtop.co.kr/Interest_renew/index_all.asp'

# requests를 사용하여 HTML 페이지 가져오기
res = requests.get(url)

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(res.content, 'html.parser')

# 웹사이트에서 필요한 내용 가져오기
title = soup.find('title').text
table = soup.find('table', attrs={'class': 'board_list'})
table_rows = table.find_all('tr')

# Streamlit을 사용하여 결과 보여주기
st.title(title)
for row in table_rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    st.write(cols)