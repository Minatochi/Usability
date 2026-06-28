"""
Section Header.
"""

import streamlit as st


def dashboard_section(
    title: str,
    description: str,
):
    """
    Einheitlicher Abschnitt im Dashboard.
    """

    st.markdown(f"## {title}")

    st.caption(description)