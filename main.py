import streamlit as st

pg = st.navigation(
    [
        st.Page("p1.py", title="IRIS資料集資訊", icon="🌹"),
        st.Page("p2.py", title="IRIS品種預測", icon="👌")
    ]
)
pg.run()