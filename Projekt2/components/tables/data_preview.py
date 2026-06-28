"""
Data Preview.
"""

import streamlit as st


def data_preview(df):

    st.subheader("Vorschau")

    st.dataframe(

        df.head(20),

        use_container_width=True,

        hide_index=True,

    )