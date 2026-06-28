"""
Verwaltet den globalen Session State.
"""

import streamlit as st


DEFAULT_SESSION = {

    "csv_loaded": False,

    "current_page": "dashboard",

    "dataset": None,

    "filtered_dataset": None,

    "selected_artist": None,

    "selected_genre": None,

    "selected_year": None,

    "theme": "dark",

}


def initialize_session():

    for key, value in DEFAULT_SESSION.items():

        if key not in st.session_state:

            st.session_state[key] = value