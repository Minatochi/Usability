"""
Page Header
"""

import streamlit as st


def page_header(
    title: str,
    subtitle: str,
):

    st.title(title)

    st.caption(subtitle)

    st.divider()