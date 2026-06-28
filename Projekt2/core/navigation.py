"""
Navigation der SPA.
"""

import streamlit as st
from components.navigation.data_menu import render_data_menu

PAGES = {

    "dashboard": "🏠 Dashboard",

    "listening": "🎧 Hörverhalten",

    "artists": "🎤 Künstler",

    "genres": "🎼 Genres",

    "timeline": "📅 Zeit",

    "insights": "🤖 KI Insights",

    "quality": "🛠 Datenqualität",

    "settings": "⚙ Einstellungen",

}


def sidebar_navigation():

    st.sidebar.title("Spotify Analytics")

    render_data_menu()

    st.sidebar.markdown("---")

    st.sidebar.markdown("---")

    for page_id, page_name in PAGES.items():

        if st.sidebar.button(
            page_name,
            use_container_width=True,
        ):

            st.session_state.current_page = page_id