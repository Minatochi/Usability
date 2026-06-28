"""
Globales Filterpanel.
"""

import streamlit as st


def render_filter_panel(df):
    """
    Rendert die globalen Filter und gibt den gefilterten
    DataFrame zurück.
    """

    st.sidebar.markdown("## 🎛️ Filter")

    filtered_df = df.copy()

    # ---------------------------
    # Genre
    # ---------------------------

    genres = sorted(df["track_genre"].dropna().unique())

    selected_genres = st.sidebar.multiselect(
        "Genre",
        genres,
    )

    if selected_genres:

        filtered_df = filtered_df[
            filtered_df["track_genre"].isin(selected_genres)
        ]

    # ---------------------------
    # Künstler
    # ---------------------------

    artists = sorted(df["artists"].dropna().unique())

    selected_artists = st.sidebar.multiselect(
        "Künstler",
        artists,
    )

    if selected_artists:

        filtered_df = filtered_df[
            filtered_df["artists"].isin(selected_artists)
        ]

    # ---------------------------
    # Popularität
    # ---------------------------

    popularity = st.sidebar.slider(
        "Popularität",
        int(df["popularity"].min()),
        int(df["popularity"].max()),
        (
            int(df["popularity"].min()),
            int(df["popularity"].max()),
        ),
    )

    filtered_df = filtered_df[
        filtered_df["popularity"].between(
            popularity[0],
            popularity[1],
        )
    ]

    return filtered_df