import pandas as pd
import plotly.express as px
import streamlit as st
from dashboard.client import APIClient

client = APIClient()
st.title("World Cup History")

overview = client.history_overview()
timeline = client.history_timeline()

winners = client.history_winners()

facts = client.history_facts()

st.subheader("Tournament Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "World Cups",
        overview["total_tournaments"]
    )

with col2:
    st.metric(
        "Matches",
        overview["total_matches"]
    )

with col3:
    st.metric(
        "Goals",
        overview["total_goals"]
    )

with col4:
    st.metric(
        "Champions",
        overview["different_champions"]
    )
st.divider()

st.subheader("Tournament Timeline")

timeline_df = pd.DataFrame(timeline)

st.dataframe(
    timeline_df,
    use_container_width=True
)

# Successful nations

st.divider()

st.subheader("Most Successful Nations")

winner_df = pd.DataFrame(winners)

fig = px.bar(
    winner_df,
    x="country",
    y="titles"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("Tournament Explorer")

years = timeline_df["year"].tolist()

selected = st.selectbox(
    "Select Tournament",
    years
)
tournament = client.tournament(
    selected
)

# Display Tournament
col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Winner",
        tournament["winner"]
    )

    st.metric(
        "Runner-up",
        tournament["runner_up"]
    )

    st.metric(
        "Host",
        tournament["host"]
    )

with col2:

    st.metric(
        "Third Place",
        tournament["third"]
    )

    st.metric(
        "Fourth Place",
        tournament["fourth"]
    )

    st.metric(
        "Goals",
        tournament["goals"]
    )

st.divider()

st.subheader("Interesting Facts")

st.write(
    f"Most Successful Nation: "
    f"{facts['most_successful_country']} "
    f"({facts['titles']} titles)"
)

st.write(
    f"Highest Scoring Tournament: "
    f"{facts['highest_scoring_year']} "
    f"({facts['highest_goals']} goals)"
)