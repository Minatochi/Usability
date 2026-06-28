"""
Top Artists.
"""

import pandas as pd


def top_artists(
    df: pd.DataFrame,
    limit: int = 10,
):

    return (

        df["master_metadata_album_artist_name"]

        .dropna()

        .value_counts()

        .head(limit)

        .reset_index()

        .rename(

            columns={

                "index": "Artist",

                "master_metadata_album_artist_name": "Streams",

            }

        )

    )