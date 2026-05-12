import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("IRIS資料集資訊")
df = pd.read_csv("iris.csv")
st.write(df.head())  # 顯示前五筆資料

st.write("### iris樣本分布圖")
mapping = {"Setosa": 0, "Versicolor": 1, "Virginica": 2}
colors = ["red", "green", "blue"]

# 分頁顯示
tab1, tab2 = st.tabs(['依花萼長寬', '依花瓣長寬'])

fig, ax = plt.subplots()
with tab1:
    for i,s in mapping.items():
        subset = df[df["variety"] == i]
        ax.scatter(subset["sepal.length"], subset["sepal.width"], c=colors[s])
    ax.set_xlabel("sepal.length")
    ax.set_ylabel("sepal.width")
    ax.legend()
    st.pyplot(fig)

fig2, ax2 = plt.subplots()
with tab2:
    for i,s in mapping.items():
        subset = df[df["variety"] == i]
        ax2.scatter(subset["petal.length"], subset["petal.width"], c=colors[s])
    ax2.set_xlabel("petal.length")
    ax2.set_ylabel("petal.width")
    ax2.legend()
    st.pyplot(fig2)
