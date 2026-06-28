"""
components/cards/dashboard_intro.py

Einführung in das Dashboard.
"""

import streamlit as st


def dashboard_intro() -> None:
    """
    Begrüßt den Benutzer und erklärt den Ablauf
    der Analyse.
    """

    with st.container(border=True):

        st.subheader("Willkommen")

        st.markdown(
            """
Dieses Dashboard führt dich Schritt für Schritt
durch deinen Spotify-Datensatz.

Die Analyse folgt einer klaren Struktur:

1. Überblick über den Datensatz
2. Kennzahlen und wichtigste Erkenntnisse
3. Audio Features
4. Interaktive Visualisierungen
5. Datengrundlage

Alle Diagramme reagieren automatisch
auf die aktuell ausgewählten Filter.
"""
        )