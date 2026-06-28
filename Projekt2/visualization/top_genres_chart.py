"""
Top Genres Chart.
"""

import plotly.express as px

from visualization.charts import apply_layout


def top_genres_chart(df):

    fig = px.bar(

        df,

        x="Tracks",

        y="Genre",

        orientation="h",

        color="Tracks",

        color_continuous_scale="Greens",

    )

    fig.update_yaxes(
        categoryorder="total ascending"
    )

    return apply_layout(fig)