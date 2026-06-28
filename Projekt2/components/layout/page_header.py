"""
Page Header.
"""

import streamlit as st


def page_header(
    title: str,
    subtitle: str,
):
    """
    Einheitlicher Seitenkopf.
    """

    st.title(title)

    st.caption(subtitle)

    st.markdown(
        """
<div style="margin-bottom:32px"></div>
""",
        unsafe_allow_html=True,
    )