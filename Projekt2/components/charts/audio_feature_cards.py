"""
Audio Feature Cards.
"""

import streamlit as st


def render_audio_features(df):

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Danceability",
        f"{df['danceability'].mean():.2f}",
    )

    col2.metric(
        "Energy",
        f"{df['energy'].mean():.2f}",
    )

    col3.metric(
        "Valence",
        f"{df['valence'].mean():.2f}",
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Acousticness",
        f"{df['acousticness'].mean():.2f}",
    )

    col2.metric(
        "Instrumental",
        f"{df['instrumentalness'].mean():.2f}",
    )

    col3.metric(
        "Popularity",
        f"{df['popularity'].mean():.0f}",
    )