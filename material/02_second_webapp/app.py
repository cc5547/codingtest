import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

st.title("붓꽃 데이터 분석")

# 데이터 로드
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name="species")

# 훈련/테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 모델 학습
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# 예측 결과 출력
st.subheader("예측 결과")
y_pred = clf.predict(X_test)
result_df = pd.DataFrame({"실제값": y_test, "예측값": y_pred})
st.write(result_df)

# 정확도 출력
st.subheader("정확도")
accuracy = clf.score(X_test, y_test)
st.write(accuracy)