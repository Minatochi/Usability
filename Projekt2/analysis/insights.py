"""
analysis/insights.py

Automatisch erzeugte Erkenntnisse.
"""

import pandas as pd


def top_artist(df: pd.DataFrame):

    if "master_metadata_album_artist_name" not in df.columns:
        return "-"

    return (
        df["master_metadata_album_artist_name"]
        .value_counts()
        .idxmax()
    )


def top_track(df: pd.DataFrame):

    if "master_metadata_track_name" not in df.columns:
        return "-"

    return (
        df["master_metadata_track_name"]
        .value_counts()
        .idxmax()
    )


def top_album(df: pd.DataFrame):

    if "master_metadata_album_album_name" not in df.columns:
        return "-"

    return (
        df["master_metadata_album_album_name"]
        .value_counts()
        .idxmax()
    )