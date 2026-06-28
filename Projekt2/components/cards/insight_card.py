"""
Insight Card
"""

import streamlit as st


def insight_card(
    insight: str,
    explanation: str,
):

    with st.container(border=True):

        st.markdown("### 💡 Insight")

        st.write(insight)

        with st.expander("Warum ist das interessant?"):

            st.write(explanation)