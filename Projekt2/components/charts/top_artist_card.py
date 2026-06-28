"""
Top Artist Dashboard Card.
"""

from analysis.spotify_analysis import SpotifyAnalysis

from visualization.top_artists_chart import (
    top_artists_chart,
)

from components.cards.chart_card import (
    chart_card,
)


def render_top_artist_card(df):

    artists = SpotifyAnalysis.top_artists(df)

    figure = top_artists_chart(artists)

    chart_card(

        title="Top Künstler",

        description="Die zehn meistgehörten Künstler.",

        chart=figure,

        interpretation="""
Diese Grafik zeigt,
welche Künstler deine Hörhistorie dominieren.
""",

    )