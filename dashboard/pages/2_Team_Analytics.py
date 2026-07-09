import streamlit as st
from client import APIClient

client = APIClient()

st.title("Team Analytics")

teams = client.get_teams()

selected_team = st.selectbox(
    "Search for a Team",
    teams,
    index=None,
    placeholder="Type a country's name..."
)

if st.button("Load Analytics"):

    summary = client.team_summary(selected_team)

    st.subheader(summary["team"])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Matches",
            summary["matches_played"]
        )

        st.metric(
            "Wins",
            summary["wins"]
        )

    with col2:
        st.metric(
            "Draws",
            summary["draws"]
        )

        st.metric(
            "Losses",
            summary["losses"]
        )

    with col3:
        st.metric(
            "Goal Difference",
            summary["goal_difference"]
        )

        st.metric(
            "Win %",
            summary["win_percentage"]
        )

    st.json(summary)