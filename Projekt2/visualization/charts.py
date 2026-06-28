"""
Globale Diagramme.
"""

import plotly.express as px


def apply_layout(fig):

    fig.update_layout(

        template="plotly_dark",

        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20,
        ),

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        legend_title="",

    )

    return fig