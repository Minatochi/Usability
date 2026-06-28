"""
Filter Summary Card.
"""

import streamlit as st


def render_filter_summary(df):

    st.info(
        f"""
### Aktuelle Auswahl

Songs: **{len(df):,}**

Genres: **{df['track_genre'].nunique()}**

Artists: **{df['artists'].nunique()}**
"""
    )