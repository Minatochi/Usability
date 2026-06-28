"""
Datenverwaltung.
"""

import streamlit as st


def render_data_menu():

    with st.sidebar.expander("💾 Daten", expanded=True):

        if st.session_state.csv_loaded:

            st.success("Standarddatei geladen")

        else:

            st.warning("Keine CSV gefunden")

        st.button(
            "CSV wechseln",
            use_container_width=True,
        )

        st.button(
            "Neu laden",
            use_container_width=True,
        )