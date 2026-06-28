"""
Verwaltet den Zustand der Anwendung.
"""

import streamlit as st

from analysis.loader import load_default_dataset


def initialize_dataset():
    """
    Lädt beim Start automatisch den Datensatz.
    """

    if st.session_state.dataset is not None:
        return

    dataframe = load_default_dataset()

    if dataframe is None:
        return

    st.session_state.dataset = dataframe
    st.session_state.filtered_dataset = dataframe.copy()
    st.session_state.csv_loaded = True