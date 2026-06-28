"""
Dashboard View
"""

import streamlit as st

from components.layout.page_header import page_header

from components.cards.metric_card import metric_card

from components.cards.info_card import info_card

from components.cards.insight_card import insight_card

from components.feedback.empty_state import empty_state


df = st.session_state.dataset


def render_dashboard():

    page_header(

        "Spotify Analytics",

        "Professionelle Analyse deiner Spotify-Historie",

    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        metric_card(

            "Songs",

            "-",

            "🎵",

        )

    with col2:

        metric_card(

            "Artists",

            "-",

            "🎤",

        )

    with col3:

        metric_card(

            "Genres",

            "-",

            "🎼",

        )

    with col4:

        metric_card(

            "Stunden",

            "-",

            "⏱️",

        )

    st.write("")

    col1, col2 = st.columns([2, 1])

    with col1:

        info_card(

            "Willkommen",

            """
            Willkommen bei Spotify Analytics.

            Dieses Dashboard führt dich Schritt für Schritt
            durch deine Spotify-Historie.

            Im nächsten Sprint wird hier automatisch
            deine CSV geladen.
            """,

            "🎧",

        )

    with col2:

        insight_card(

            "Noch keine Daten vorhanden.",

            """
            Sobald eine CSV-Datei geladen wurde,
            erscheinen hier automatisch
            die wichtigsten Erkenntnisse.
            """,

        )

    st.write("")

    if df is None:

        empty_state()

    else:
        st.success(
            f"{len(df):,} Datensätze automatisch geladen."
        )