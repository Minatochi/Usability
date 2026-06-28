"""
Quick Overview Card.
"""

import streamlit as st


def quick_overview(df) -> None:
    """
    Zeigt eine kompakte Zusammenfassung.
    """

    st.subheader("📖 Überblick")

    st.markdown(
        """
Diese Analyse basiert auf deiner Spotify-Historie.

Die Anwendung berechnet automatisch:

- wichtigste Kennzahlen
- Lieblingskünstler
- Lieblingssongs
- Hörverhalten
- Zeitliche Entwicklung
- Genres
- weitere Erkenntnisse

Nutze anschließend die Navigation,
um tiefer in deine Daten einzutauchen.
"""
    )