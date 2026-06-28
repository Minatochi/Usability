"""
Dashboard View.
"""

import streamlit as st

from components.cards.dashboard_intro import dashboard_intro
from components.cards.dashboard_section import dashboard_section
from components.cards.filter_summary import render_filter_summary
from components.cards.hero_banner import hero_banner
from components.cards.info_card import info_card
from components.cards.quick_overview import quick_overview
from components.cards.statistics_cards import render_statistics
from components.cards.top_insight import render_top_insight

from components.charts.audio_feature_cards import render_audio_features
from components.charts.popularity_card import render_popularity_card
from components.charts.top_artist_card import render_top_artist_card
from components.charts.top_genre_card import render_top_genre_card

from components.feedback.empty_state import empty_state

from components.layout.footer import footer
from components.layout.page_header import page_header

from components.tables.data_preview import data_preview


def render_dashboard() -> None:
    """
    Rendert das Dashboard.
    """

    df = st.session_state.get("filtered_dataset")

    page_header(
        "Spotify Analytics",
        "Professionelle Analyse deiner Spotify-Daten",
    )

    if df is None:
        empty_state()
        return

    # --------------------------------------------------
    # Hero
    # --------------------------------------------------

    hero_banner(len(df))

    # --------------------------------------------------
    # Einführung
    # --------------------------------------------------

    dashboard_intro()

    # --------------------------------------------------
    # Filterübersicht
    # --------------------------------------------------

    render_filter_summary(df)

    # --------------------------------------------------
    # Kennzahlen
    # --------------------------------------------------

    dashboard_section(
        "Kennzahlen",
        "Die wichtigsten Kennzahlen des aktuell gefilterten Datensatzes.",
    )

    render_statistics(df)

    # --------------------------------------------------
    # Insights
    # --------------------------------------------------

    dashboard_section(
        "Top Insights",
        "Automatisch erzeugte Erkenntnisse aus dem Datensatz.",
    )

    left, right = st.columns([2, 1])

    with left:
        info_card(
            title="Zusammenfassung",
            icon="🎧",
            text="""
Dieses Dashboard unterstützt dich bei der Analyse
deiner Spotify-Daten.

Alle Kennzahlen und Diagramme reagieren
automatisch auf die aktuell ausgewählten Filter.
""",
        )

    with right:
        render_top_insight(df)

    # --------------------------------------------------
    # Audio Features
    # --------------------------------------------------

    dashboard_section(
        "Audio Features",
        "Durchschnittliche musikalische Eigenschaften der Songs.",
    )

    render_audio_features(df)

    # --------------------------------------------------
    # Visualisierungen
    # --------------------------------------------------

    dashboard_section(
        "Visualisierungen",
        "Interaktive Diagramme zur Analyse der Daten.",
    )

    render_top_artist_card(df)

    st.write("")

    render_top_genre_card(df)

    st.write("")

    render_popularity_card(df)

    # --------------------------------------------------
    # Überblick
    # --------------------------------------------------

    dashboard_section(
        "Überblick",
        "Kurze Einführung in die Analyseplattform.",
    )

    quick_overview(df)

    # --------------------------------------------------
    # Datengrundlage
    # --------------------------------------------------

    dashboard_section(
        "Datengrundlage",
        "Vorschau der aktuell analysierten Daten.",
    )

    data_preview(df)

    # --------------------------------------------------
    # Footer
    # --------------------------------------------------

    footer()