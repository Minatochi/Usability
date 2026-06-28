"""
Grundlegende Spotify Statistiken.
"""

import pandas as pd

from analysis.schema import (
    ARTIST,
    ALBUM,
    TRACK,
    DURATION,
)


def total_tracks(df: pd.DataFrame) -> int:
    return len(df)


def total_artists(df: pd.DataFrame) -> int:
    return df[ARTIST].dropna().nunique()


def total_albums(df: pd.DataFrame) -> int:
    return df[ALBUM].dropna().nunique()


def total_tracks_unique(df: pd.DataFrame) -> int:
    return df[TRACK].dropna().nunique()


def listening_time_hours(df: pd.DataFrame) -> float:
    hours = df[DURATION].sum() / 1000 / 60 / 60
    return round(hours, 1)