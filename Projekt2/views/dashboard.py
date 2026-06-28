"""
Dashboard View.
"""

import streamlit as st

from components.layout.page_header import page_header
from components.cards.statistics_cards import render_statistics
from components.cards.info_card import info_card
from components.cards.top_insight import render_top_insight
from components.cards.hero_banner import hero_banner
from components.cards.quick_overview import quick_overview
from components.cards.dashboard_section import dashboard_section
from components.feedback.empty_state import empty_state


def render_dashboard() -> None:

    df = st.session_state.get("dataset")

    page_header(
        "Spotify Analytics",
        "Professionelle Analyse deiner Spotify-Historie",
    )

    if df is None:

        empty_state()

        return

    hero_banner(len(df))

    dashboard_section(
        "Kennzahlen",
        "Die wichtigsten Kennzahlen deiner Spotify-Historie.",
    )

    render_statistics(df)

    st.write("")

    dashboard_section(
        "Erste Erkenntnisse",
        "Automatisch erzeugte Insights.",
    )

    left, right = st.columns([2, 1])

    with left:

        info_card(
            title="Willkommen",
            icon="🎧",
            text="""
Dieses Dashboard dient als zentrale Startseite.

Im weiteren Verlauf erscheinen hier
Visualisierungen und interaktive Analysen.
""",
        )

    with right:

        render_top_insight(df)

    st.write("")

    dashboard_section(
        "Überblick",
        "Kurze Einführung in die Analyse.",
    )

    quick_overview(df)

    from components.charts.top_artist_card import (
        render_top_artist_card,
    )

    st.write("")

    dashboard_section(

        "Top Künstler",

        "Die meistgehörten Künstler deiner Spotify-Historie.",

    )

    render_top_artist_card(df)

    st.success(
        f"✅ {len(df):,} Datensätze erfolgreich geladen."
    )