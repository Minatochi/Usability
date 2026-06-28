"""
statistics_cards.py

Rendert die wichtigsten Kennzahlen (KPIs) des Spotify-Dashboards.
"""

import streamlit as st

from analysis.statistics import (
    listening_time_hours,
    total_albums,
    total_artists,
    total_tracks,
)

from components.cards.metric_card import metric_card


def render_statistics(df) -> None:
    """
    Rendert die KPI-Karten des Dashboards.

    Parameters
    ----------
    df : pandas.DataFrame
        Aktueller (ggf. gefilterter) Spotify-Datensatz.
    """

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card(
            title="Songs",
            value=f"{total_tracks(df):,}",
            icon="🎵",
            subtitle="Datensätze im aktuellen Filter",
        )

    with col2:
        metric_card(
            title="Künstler",
            value=f"{total_artists(df):,}",
            icon="🎤",
            subtitle="Eindeutige Artists",
        )

    with col3:
        metric_card(
            title="Alben",
            value=f"{total_albums(df):,}",
            icon="💿",
            subtitle="Unterschiedliche Alben",
        )

    with col4:
        metric_card(
            title="Hörzeit",
            value=f"{listening_time_hours(df):.1f} h",
            icon="⏱️",
            subtitle="Gesamtdauer aller Titel",
        )