"""
Loading Component
"""

import streamlit as st


def loading(text="Lade Daten..."):

    with st.spinner(text):

        st.write("")