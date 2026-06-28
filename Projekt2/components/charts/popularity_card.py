"""
Popularity Card.
"""

from visualization.popularity_chart import (
    popularity_chart,
)

from components.cards.chart_card import (
    chart_card,
)


def render_popularity_card(df):

    fig = popularity_chart(df)

    chart_card(

        title="Popularität",

        description="Verteilung der Popularität aller Songs.",

        chart=fig,

        interpretation="""
Die meisten Songs besitzen
eine mittlere Popularität.

Später werden wir diese
nach Genres filtern können.
""",
    )