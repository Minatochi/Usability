"""
Top Artists Chart.
"""

import plotly.express as px

from visualization.charts import apply_layout


def top_artists_chart(df):

    fig = px.bar(

        df,

        x="Streams",

        y="Artist",

        orientation="h",

    )

    fig.update_yaxes(

        categoryorder="total ascending"

    )

    return apply_layout(fig)