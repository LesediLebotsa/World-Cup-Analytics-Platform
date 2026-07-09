import streamlit as st

from client import APIClient

client = APIClient()

st.title("Match Predictor")

teams = client.get_teams()

col1, col2 = st.columns(2)

with col1:
    team_one = st.selectbox(
        "Home Team",
        teams,
        index=None,
        placeholder="Search for a team..."
    )

with col2:
    team_two = st.selectbox(
        "Away Team",
        teams,
        index=None,
        placeholder="Search for a team..."
    )

if st.button("Predict Match"):

    if team_one == team_two:
        st.warning("Please select two different teams.")

    else:

        prediction = client.prediction(
            team_one,
            team_two
        )

        st.divider()

        st.subheader("Prediction")

        st.success(prediction["prediction"])

        st.metric(
            "Confidence",
            prediction["confidence"]
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                team_one,
                prediction["team_1_strength"]
            )

        with col2:
            st.metric(
                team_two,
                prediction["team_2_strength"]
            )

        st.divider()

        st.subheader("Prediction Explanation")

        explanations = prediction["explanation"]

        for explanation in prediction["explanation"]:
            st.markdown(f"### {explanation['category']}")
            st.write(explanation["message"])