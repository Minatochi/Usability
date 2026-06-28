"""
Dashboard Startseite.
"""

import streamlit as st


def render_dashboard():

    st.title("Spotify Analytics")

    st.caption(
        "Professionelle Analyse deiner Spotify-Historie"
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Songs", "-")
    col2.metric("Artists", "-")
    col3.metric("Genres", "-")
    col4.metric("Stunden", "-")

    st.info(
        """
        👋 Willkommen!

        Dies ist das neue Dashboard von Projekt2.

        Im nächsten Sprint werden CSV-Import,
        Datenanalyse und Visualisierungen integriert.
        """
    )