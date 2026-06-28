"""
Automatische Spotify Insights.
"""

import pandas as pd

from analysis.schema import (
    ARTIST,
    TRACK,
    ALBUM,
)


def _safe_mode(df: pd.DataFrame, column: str) -> str:

    values = df[column].dropna()

    if values.empty:
        return "-"

    return values.value_counts().idxmax()


def top_artist(df):

    return _safe_mode(df, ARTIST)


def top_track(df):

    return _safe_mode(df, TRACK)


def top_album(df):

    return _safe_mode(df, ALBUM)