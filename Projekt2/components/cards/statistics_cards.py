"""
Dashboard KPI Bereich.
"""

import streamlit as st

from analysis.statistics import (
    total_tracks,
    total_artists,
    total_albums,
    listening_time_hours,
)

from components.cards.metric_card import metric_card


def render_statistics(df):

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        metric_card(
            "Songs",
            f"{total_tracks(df):,}",
            "🎵",
        )

    with col2:

        metric_card(
            "Artists",
            f"{total_artists(df):,}",
            "🎤",
        )

    with col3:

        metric_card(
            "Alben",
            f"{total_albums(df):,}",
            "💿",
        )

    with col4:

        metric_card(
            "Hörstunden",
            f"{listening_time_hours(df):,.1f}",
            "⏱️",
        )