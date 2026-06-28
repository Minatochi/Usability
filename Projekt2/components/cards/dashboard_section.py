"""
Dashboard Section Header.
"""

import streamlit as st


def dashboard_section(
    title: str,
    description: str,
):
    """
    Einheitlicher Abschnitt.
    """

    st.markdown(f"## {title}")

    st.caption(description)

    st.markdown(
        "<div style='margin-bottom:20px'></div>",
        unsafe_allow_html=True,
    )