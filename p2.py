import streamlit as st
import numpy as np
import pandas as pd
import joblib

st.title("IRIS品種預測")

# 載入模型
knn = joblib.load("knn.joblib")
lr = joblib.load("lr.joblib")
nb = joblib.load("nb.joblib")
rf = joblib.load("rf.joblib")

# 左側安排選單
ss = st.sidebar.selectbox("請選擇模型:", 
                       ("KNN", "Logistic Regression", "Naive Bayes", "Random Forest"))
if ss == "KNN":
    model = knn
elif ss == "Logistic Regression":
    model = lr
elif ss == "Naive Bayes":
    model = nb
else:    
    model = rf

st.image("iris.png", caption="IRIS花朵圖片")

# 設定輸入的滑動條
df = pd.read_csv("iris.csv")
se1 = st.slider("花萼長度", 
                float(df["sepal.length"].min()-0.5), 
                float(df["sepal.length"].max()+0.5), 
                float(df["sepal.length"].mean()))
se2 = st.slider("花萼寬度", 
                float(df["sepal.width"].min()-0.5), 
                float(df["sepal.width"].max()+0.5), 
                float(df["sepal.width"].mean()))
pe1 = st.slider("花瓣長度", 
                float(df["petal.length"].min()-0.5), 
                float(df["petal.length"].max()+0.5), 
                float(df["petal.length"].mean()))
pe2 = st.slider("花瓣寬度", 
                float(df["petal.width"].min()-0.5), 
                float(df["petal.width"].max()+0.5), 
                float(df["petal.width"].mean()))

labels = ["Setosa", "Versicolor", "Virginica"]

# 預測
if st.button("進行預測"):
    X = np.array([[se1, se2, pe1, pe2]])  #將輸入的數值轉換為二維陣列
    y = model.predict(X) #一維結果
    st.write("### 預測結果:", y[0])
    st.write("### 預測的品種為:", labels[y[0]])