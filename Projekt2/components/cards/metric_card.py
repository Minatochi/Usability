"""
Metric Card.
"""

import streamlit as st


def metric_card(
    title: str,
    value: str,
    icon: str = "",
    subtitle: str = "",
):

    with st.container(border=True):

        left, right = st.columns([1, 5])

        with left:

            st.markdown(
                f"# {icon}"
            )

        with right:

            st.caption(title)

            st.markdown(
                f"## {value}"
            )

            if subtitle:

                st.caption(subtitle)