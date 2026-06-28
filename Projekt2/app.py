"""
app.py

Einstiegspunkt der Anwendung.
"""

from core.startup import initialize_app
from core.session import initialize_session
from core.navigation import sidebar_navigation
from core.router import render_current_page
from core.app_state import initialize_dataset

from components.filters.filter_panel import render_filter_panel

import streamlit as st


def main():

    initialize_app()

    initialize_session()

    initialize_dataset()

    if st.session_state.dataset is not None:

        st.session_state.filtered_dataset = render_filter_panel(
            st.session_state.dataset
        )

    sidebar_navigation()

    render_current_page()


if __name__ == "__main__":

    main()