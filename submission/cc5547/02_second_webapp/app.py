from tkinter.tix import COLUMN
from pyparsing import empty
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.set_page_config(layout="wide")
empty1,con1,empty2 = st.columns([0.3,1.0,0.3])
empyt1,con2,con3,empty2 = st.columns([0.3,0.5,0.5,0.3])
empyt1,con4,empty2 = st.columns([0.3,1.0,0.3])
empyt1,con5,con6,empty2 = st.columns([0.3,0.5,0.5,0.3])

def start():
  picture_URL = "https://i.imgur.com/D7uu8FN.jpg" 
  st.image(picture_URL)


def main() :

    with empty1 :
        # empty() # 여백부분1
   
    with con1 :
      img = start()
        

    with con2 :
      pass
        # 셀렉트박스
        # 라디오버튼
        # 라디오버튼

    with con3 :
      pass
     	# 데이터프레임

    with con4 :
      pass
		# 긴 셀렉트박스

    with con5 :
      pass
		# 동영상 
     
    with con6 :
		# 동영상 제목
    #     동영상 설명
      pass

    with empty2 :
	  #  empty() # 여백부분2
      pass

























# streamlit 라이브러리 호출
# 상대경로 복사 : material/02_second_webapp/app.py
# , use_column_width = True << 가운데 정렬
# st.number_input(label, value) << 데이터 입력

# -----------------------------------------------------
# # 은행 이자 계산기
# import streamlit as st
# from PIL import Image
# st.set_page_config(layout="wide")

# def start():
#   start_ment = "# 은행 이자 계산기"
#   picture_URL = "https://i.imgur.com/D7uu8FN.jpg" 
#   st.image(picture_URL, use_column_width = True)
#   st.write(start_ment, use_column_width = True)
#   st.image(picture_URL, use_column_width = True)


# start()

# -----------------------------------------------------



# st.write(
#   start_ment
#   )


# st.image(
#   "https://i.imgur.com/D7uu8FN.jpg", width=800, height= 500)



# 적금 사진 링크

# start_img = "https://i.imgur.com/D7uu8FN.jpg"
# st.image(
#   "https://i.imgur.com/D7uu8FN.jpg"  width="300" height="200"

    
#     use_column_width=True
#     # 유튜브 사진 // "https://blog.kakaocdn.net/dn/JvPqb/btqAiWpd8sf/Ah9IYr6lDRBb8oxSCJYQyK/img.png"
#   )
