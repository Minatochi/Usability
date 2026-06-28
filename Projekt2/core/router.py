"""
Einfacher Router der SPA.
"""

import streamlit as st

from views.dashboard import render_dashboard


def render_current_page():

    page = st.session_state.current_page

    if page == "dashboard":

        render_dashboard()

    else:

        st.title("🚧")

        st.info(
            "Dieser Bereich wird in einem späteren Sprint entwickelt."
        )