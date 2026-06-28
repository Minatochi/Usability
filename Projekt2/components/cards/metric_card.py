"""
Metric Card Component

Eigene KPI-Karte für das Dashboard.
"""

import streamlit as st


def metric_card(
    title: str,
    value: str,
    icon: str = "",
    delta: str | None = None,
    help_text: str | None = None,
):
    """
    Zeigt eine KPI Card an.
    """

    with st.container(border=True):

        col1, col2 = st.columns([1, 6])

        with col1:
            st.markdown(
                f"<h2 style='text-align:center'>{icon}</h2>",
                unsafe_allow_html=True,
            )

        with col2:

            st.caption(title)

            st.markdown(
                f"## {value}"
            )

            if delta:
                st.success(delta)

            if help_text:
                st.caption(help_text)