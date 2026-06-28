"""
core/startup.py

Initialisiert die gesamte Anwendung.
"""

import streamlit as st

from config.settings import (
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT,
    SIDEBAR_STATE,
)

from styles.css import load_css


def initialize_app():
    """
    Initialisiert Streamlit.
    """

    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        layout=LAYOUT,
        initial_sidebar_state=SIDEBAR_STATE,
    )

    st.markdown(
        load_css(),
        unsafe_allow_html=True,
    )