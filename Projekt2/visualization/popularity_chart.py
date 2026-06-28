"""
Popularity Histogram.
"""

import plotly.express as px

from visualization.charts import apply_layout


def popularity_chart(df):

    fig = px.histogram(

        df,

        x="popularity",

        nbins=20,

        color_discrete_sequence=["#1DB954"],

    )

    return apply_layout(fig)