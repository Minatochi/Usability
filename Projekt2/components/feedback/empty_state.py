"""
Empty State
"""

import streamlit as st


def empty_state():

    st.markdown("# 🎵")

    st.subheader("Noch keine Spotify-Datei geladen")

    st.write(
        """
        Lade zunächst deine Spotify CSV-Datei hoch.

        Danach werden automatisch

        • KPIs

        • Diagramme

        • Statistiken

        • Insights

        erstellt.
        """
    )