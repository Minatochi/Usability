"""
Hero Banner Component.

Begrüßt den Benutzer und zeigt den Status der aktuellen Analyse.
"""

import streamlit as st


def hero_banner(dataset_size: int) -> None:
    """
    Zeigt den Hero-Bereich des Dashboards.
    """

    st.markdown(
        f"""
# 🎵 Spotify Analytics

Analysiere deinen Spotify-Datensatz
mit interaktiven Visualisierungen
und wissenschaftlich fundierten
Auswertungen.

"""
    )

    st.divider()