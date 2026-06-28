"""
Dashboard Section Header.
"""

import streamlit as st


def dashboard_section(
    title: str,
    description: str,
):

    st.markdown("---")

    st.subheader(title)

    st.caption(description)

    st.write("")