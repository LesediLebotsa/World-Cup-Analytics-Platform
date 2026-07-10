import streamlit as st
from client import APIClient
import os
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)



client = APIClient()

st.title("Team Comparison")

teams = client.get_teams()

col1, col2 = st.columns(2)

with col1:
    team_1 = st.selectbox(
        "Team One",
        teams,
        index=None,
        placeholder="Search for a team..."
    )

with col2:
    team_2 = st.selectbox(
        "Team Two",
        teams,
        index=None,
        placeholder="Search for a team..."
    )

if st.button("Compare Teams"):

    if team_1 == team_2:
        st.warning("Please choose two different teams.")

    else:

        data = client.compare(team_1, team_2)

        left, right = st.columns(2)

        team1 = data["team_one"]
        team2 = data["team_two"]

        with left:

            st.subheader(team1["team"])

            st.metric(
                "Strength Score",
                round(team1["strength_score"], 2)
            )

            st.metric(
                "Matches Played",
                team1["matches_played"]
            )

            st.metric(
                "Wins",
                team1["wins"]
            )

            st.metric(
                "Draws",
                team1["draws"]
            )

            st.metric(
                "Losses",
                team1["losses"]
            )

            st.metric(
                "Win Percentage",
                f'{team1["win_percentage"]:.1f}%'
            )

        with right:

            st.subheader(team2["team"])

            st.metric(
                "Strength Score",
                round(team2["strength_score"], 2)
            )

            st.metric(
                "Matches Played",
                team2["matches_played"]
            )

            st.metric(
                "Wins",
                team2["wins"]
            )

            st.metric(
                "Draws",
                team2["draws"]
            )

            st.metric(
                "Losses",
                team2["losses"]
            )

            st.metric(
                "Win Percentage",
                f'{team2["win_percentage"]:.1f}%'
            )

        st.divider()

        h2h = data["head_to_head"]

        st.subheader("Head-to-Head")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            f"{team_1} Wins",
            h2h["team_1_wins"]
        )

        c2.metric(
            "Draws",
            h2h["draws"]
        )

        c3.metric(
            f"{team_2} Wins",
            h2h["team_2_wins"]
        )