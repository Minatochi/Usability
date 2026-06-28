"""
Top Artists.
"""

import pandas as pd

from analysis.schema import ARTIST


def top_artists(
    df: pd.DataFrame,
    limit: int = 10,
):

    artists = (
        df[ARTIST]
        .dropna()
        .value_counts()
        .head(limit)
        .rename_axis("Artist")
        .reset_index(name="Streams")
    )

    return artists