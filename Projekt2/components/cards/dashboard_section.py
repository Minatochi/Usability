"""
components/cards/dashboard_section.py

Einheitlicher Abschnittsheader für alle Dashboard-Bereiche.
"""

import streamlit as st


def dashboard_section(
    title: str,
    description: str,
) -> None:
    """
    Rendert einen standardisierten Abschnittsheader.

    Parameters
    ----------
    title : str
        Überschrift des Abschnitts.

    description : str
        Kurzbeschreibung des Inhalts.
    """

    st.markdown("---")

    st.subheader(title)

    st.caption(description)

    st.markdown(
        """
<div style="margin-bottom:16px;"></div>
""",
        unsafe_allow_html=True,
    )