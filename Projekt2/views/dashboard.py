"""
Dashboard View.

Startseite der Anwendung.
"""

import streamlit as st

from components.layout.page_header import page_header
from components.cards.statistics_cards import render_statistics
from components.cards.info_card import info_card
from components.cards.top_insight import render_top_insight
from components.feedback.empty_state import empty_state


def render_dashboard() -> None:
    """
    Rendert das Dashboard.
    """

    # --------------------------------------------------
    # Datensatz laden
    # --------------------------------------------------

    df = st.session_state.get("dataset")

    # --------------------------------------------------
    # Seitenkopf
    # --------------------------------------------------

    page_header(
        "Spotify Analytics",
        "Professionelle Analyse deiner Spotify-Historie",
    )

    # --------------------------------------------------
    # Keine Daten vorhanden
    # --------------------------------------------------

    if df is None:

        empty_state()

        return

    # --------------------------------------------------
    # KPI Bereich
    # --------------------------------------------------

    render_statistics(df)

    st.write("")

    # --------------------------------------------------
    # Dashboard Inhalt
    # --------------------------------------------------

    left, right = st.columns([2, 1])

    with left:

        info_card(
            title="Willkommen",
            icon="🎧",
            text="""
Willkommen bei Spotify Analytics.

Dieses Dashboard bietet dir einen Überblick über deine
Spotify-Historie.

Im weiteren Verlauf werden hier Diagramme,
Filter und KI-gestützte Analysen ergänzt.
""",
        )

    with right:

        render_top_insight(df)

    st.write("")

    st.success(f"✅ {len(df):,} Datensätze erfolgreich geladen.")