"""
Metric Card.
"""

import streamlit as st


def metric_card(
    title: str,
    value: str,
    icon: str = "",
    subtitle: str = "",
):

    with st.container(border=True):

        left, right = st.columns([1, 5])

        with left:

            st.markdown(
                f"""
            <div style="
            font-size:38px;
            text-align:center;
            padding-top:8px;
            ">
            {icon}
            </div>
            """,
                unsafe_allow_html=True,
            )

        with right:

            st.caption(title)

            st.markdown(
                f"## {value}"
            )

            if subtitle:

                st.caption(subtitle)