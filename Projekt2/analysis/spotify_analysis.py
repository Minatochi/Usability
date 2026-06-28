"""
spotify_analysis.py

Enthält sämtliche Auswertungen für den Spotify-Datensatz.
"""

import pandas as pd

from analysis.schema import (
    ALBUM,
    ARTIST,
    DURATION,
    GENRE,
    TRACK,
)


class SpotifyAnalysis:
    """
    Sammlung aller Analysefunktionen.
    """

    @staticmethod
    def top_artists(
        df: pd.DataFrame,
        limit: int = 10,
    ) -> pd.DataFrame:

        return (
            df[ARTIST]
            .dropna()
            .value_counts()
            .head(limit)
            .rename_axis("Artist")
            .reset_index(name="Streams")
        )

    @staticmethod
    def top_tracks(
        df: pd.DataFrame,
        limit: int = 10,
    ) -> pd.DataFrame:

        return (
            df[TRACK]
            .dropna()
            .value_counts()
            .head(limit)
            .rename_axis("Track")
            .reset_index(name="Streams")
        )

    @staticmethod
    def top_albums(
        df: pd.DataFrame,
        limit: int = 10,
    ) -> pd.DataFrame:

        return (
            df[ALBUM]
            .dropna()
            .value_counts()
            .head(limit)
            .rename_axis("Album")
            .reset_index(name="Streams")
        )

    @staticmethod
    def top_genres(
        df: pd.DataFrame,
        limit: int = 10,
    ) -> pd.DataFrame:

        return (
            df[GENRE]
            .dropna()
            .value_counts()
            .head(limit)
            .rename_axis("Genre")
            .reset_index(name="Tracks")
        )

    @staticmethod
    def total_duration_hours(df: pd.DataFrame) -> float:

        return round(df[DURATION].sum() / 1000 / 60 / 60, 1)