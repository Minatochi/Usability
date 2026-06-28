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

Willkommen zu deiner persönlichen Spotify-Auswertung.

Aktuell werden **{dataset_size:,} Wiedergaben**
analysiert.

Nutze die Navigation auf der linken Seite,
um verschiedene Bereiche deiner Hörhistorie
zu erkunden.
"""
    )

    st.divider()