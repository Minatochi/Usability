"""
Chart Card Component.

Einheitlicher Container für alle Diagramme.
"""

from typing import Optional

import streamlit as st


def chart_card(
    title: str,
    description: str,
    chart,
    interpretation: Optional[str] = None,
):
    """
    Zeigt eine standardisierte Chart Card.
    """

    with st.container(border=True):

        st.subheader(title)

        st.caption(description)

        st.plotly_chart(
            chart,
            use_container_width=True,
        )

        if interpretation:

            st.info(
                interpretation
            )