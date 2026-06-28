"""
core/navigation.py

Verwaltet die Navigation der Streamlit-Anwendung.
"""

import streamlit as st

from components.navigation.data_menu import render_data_menu


# ==========================================================
# Verfügbare Seiten
# ==========================================================

PAGES = {
    "dashboard": "🏠 Dashboard",
    "listening": "🎧 Hörverhalten",
    "artists": "🎤 Künstler",
    "genres": "🎼 Genres",
    "timeline": "📅 Zeitverlauf",
    "insights": "💡 Insights",
    "quality": "🛠 Datenqualität",
    "settings": "⚙ Einstellungen",
}


# ==========================================================
# Sidebar Navigation
# ==========================================================

def sidebar_navigation() -> None:
    """
    Rendert die komplette Sidebar der Anwendung.
    """

    # ------------------------------------------------------
    # Logo / Titel
    # ------------------------------------------------------

    st.sidebar.markdown(
        """
# 🎵 Spotify Analytics

Professionelle Datenanalyse
"""
    )

    st.sidebar.caption(
        "Analysiere Songs, Künstler und Audio-Features."
    )

    st.sidebar.markdown("---")

    # ------------------------------------------------------
    # Datenbereich
    # ------------------------------------------------------

    render_data_menu()

    st.sidebar.markdown("---")

    # ------------------------------------------------------
    # Navigation
    # ------------------------------------------------------

    st.sidebar.caption("Navigation")

    for page_id, page_name in PAGES.items():

        if st.sidebar.button(
            page_name,
            use_container_width=True,
        ):
            st.session_state.current_page = page_id

    # ------------------------------------------------------
    # Footer
    # ------------------------------------------------------

    st.sidebar.markdown("---")

    st.sidebar.caption(
        "Spotify Analytics\n\nVersion 0.1"
    )