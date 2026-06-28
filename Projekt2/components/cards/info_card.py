"""
Info Card
"""

import streamlit as st


def info_card(
    title: str,
    text: str,
    icon: str = "ℹ️",
):

    with st.container(border=True):

        st.subheader(f"{icon} {title}")

        st.write(text)