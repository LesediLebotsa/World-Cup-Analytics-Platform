import streamlit as st

st.set_page_config(
    page_title="World Cup Analytics Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("World Cup Analytics & Prediction Platform")

st.markdown(
"""
Welcome to the World Cup Analytics Platform.

Use the navigation menu on the left to explore:

- Team Analytics
- Team Comparison
- Match Prediction
- World Cup History
"""
)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Teams",
        "225"
    )

with col2:
    st.metric(
        "Matches",
        "17,769"
    )

with col3:
    st.metric(
        "World Cups",
        "1930 - 2022"
    )

st.success("API Status: Connected")