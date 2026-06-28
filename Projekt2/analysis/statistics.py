"""
Grundlegende Spotify Statistiken.
"""

import pandas as pd


def total_tracks(df: pd.DataFrame) -> int:
    return len(df)


def total_artists(df: pd.DataFrame) -> int:

    if "master_metadata_album_artist_name" not in df.columns:
        return 0

    return (
        df["master_metadata_album_artist_name"]
        .dropna()
        .nunique()
    )


def total_albums(df: pd.DataFrame) -> int:

    if "master_metadata_album_album_name" not in df.columns:
        return 0

    return (
        df["master_metadata_album_album_name"]
        .dropna()
        .nunique()
    )


def total_tracks_unique(df: pd.DataFrame) -> int:

    if "master_metadata_track_name" not in df.columns:
        return 0

    return (
        df["master_metadata_track_name"]
        .dropna()
        .nunique()
    )


def listening_time_hours(df: pd.DataFrame) -> float:

    if "ms_played" not in df.columns:
        return 0.0

    hours = df["ms_played"].sum() / 1000 / 60 / 60

    return round(hours, 1)