"""
components/cards/hero_banner.py

Hero-Bereich des Dashboards.
"""

import streamlit as st


def hero_banner(dataset_size: int) -> None:
    """
    Zeigt den Hero-Bereich des Dashboards.
    """

    st.markdown(
        f"""
# 🎵 Spotify Analytics

### Analysiere deine Musikdaten mit interaktiven Visualisierungen

Dieses Dashboard unterstützt dich dabei,
Spotify-Daten systematisch auszuwerten und Muster
in deinem Datensatz zu erkennen.

**Aktuell werden {dataset_size:,} Songs analysiert.**
"""
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("✅ Datensatz erfolgreich geladen")

    with col2:
        st.info("📊 Dashboard bereit")

    with col3:
        st.success("🎧 Analyse aktiv")

    st.divider()