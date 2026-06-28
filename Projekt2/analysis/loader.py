"""
CSV Loader.

Lädt standardmäßig die Spotify-Historie.
"""

from pathlib import Path

import pandas as pd

from config.constants import DEFAULT_DATASET


def load_default_dataset() -> pd.DataFrame | None:
    """
    Lädt automatisch die Standard-CSV.

    Returns
    -------
    pd.DataFrame | None
    """

    if not DEFAULT_DATASET.exists():
        return None

    return pd.read_csv(DEFAULT_DATASET)


def load_dataset(path: Path) -> pd.DataFrame:
    """
    Lädt eine beliebige CSV.
    """

    return pd.read_csv(path)