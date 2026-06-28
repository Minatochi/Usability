"""
Top Genre Card.
"""

from analysis.spotify_analysis import SpotifyAnalysis

from visualization.top_genres_chart import (
    top_genres_chart,
)

from components.cards.chart_card import (
    chart_card,
)


def render_top_genre_card(df):

    genres = SpotifyAnalysis.top_genres(df)

    figure = top_genres_chart(genres)

    chart_card(

        title="Top Genres",

        description="Die häufigsten Genres des Datensatzes.",

        chart=figure,

        interpretation="""
Diese Visualisierung zeigt,
welche Musikgenres im Datensatz
am häufigsten vertreten sind.
""",
    )