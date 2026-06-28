"""
Globale Diagrammgestaltung.
"""

from styles.theme import theme


def apply_layout(fig):
    """
    Einheitliches Styling aller Plotly-Diagramme.
    """

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20,
        ),

        font=dict(
            family=theme.typography.FONT_FAMILY,
            size=14,
            color=theme.colors.TEXT_PRIMARY,
        ),

        title_font_size=20,

        legend_title="",

    )

    return fig