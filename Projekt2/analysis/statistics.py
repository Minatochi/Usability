"""
analysis/statistics.py

Berechnet grundlegende Kennzahlen der Spotify-Historie.
"""

import pandas as pd


def total_tracks(df: pd.DataFrame) -> int:
    """Anzahl aller abgespielten Songs."""
    return len(df)


def total_artists(df: pd.DataFrame) -> int:
    """Anzahl unterschiedlicher Künstler."""

    if "master_metadata_album_artist_name" not in df.columns:
        return 0

    return df["master_metadata_album_artist_name"].nunique()


def total_albums(df: pd.DataFrame) -> int:
    """Anzahl unterschiedlicher Alben."""

    if "master_metadata_album_album_name" not in df.columns:
        return 0

    return df["master_metadata_album_album_name"].nunique()


def total_tracks_unique(df: pd.DataFrame) -> int:
    """Anzahl unterschiedlicher Songs."""

    if "master_metadata_track_name" not in df.columns:
        return 0

    return df["master_metadata_track_name"].nunique()


def listening_time_hours(df: pd.DataFrame) -> float:
    """
    Gesamte Hörzeit in Stunden.
    """

    if "ms_played" not in df.columns:
        return 0

    hours = df["ms_played"].sum() / 1000 / 60 / 60

    return round(hours, 1)