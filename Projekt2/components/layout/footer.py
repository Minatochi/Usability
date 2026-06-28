"""
components/layout/footer.py

Einheitlicher Footer der Anwendung.
"""

import streamlit as st


def footer() -> None:
    """
    Rendert den Footer der Anwendung.
    """

    st.markdown("---")

    left, right = st.columns([3, 1])

    with left:

        st.caption(
            """
Spotify Analytics

Entwickelt im Rahmen des Moduls
**Usability Engineering**.

Die Anwendung demonstriert die Optimierung einer
datengetriebenen Streamlit-Anwendung hinsichtlich
Typografie, Farbleitsystem und Informationsarchitektur.
"""
        )

    with right:

        st.caption(
            """
Version

0.1.0
"""
        )