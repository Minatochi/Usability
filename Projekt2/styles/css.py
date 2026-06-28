"""
styles/css.py

Erzeugt das globale CSS der Anwendung.
"""

from styles.theme import theme


def load_css() -> str:
    """
    Gibt das globale CSS als String zurück.
    """

    return f"""
<style>

/* ============================
   Allgemein
============================ */

html,
body,
[class*="css"] {{
    font-family: {theme.typography.FONT_FAMILY}, sans-serif;
    background-color: {theme.colors.BACKGROUND};
    color: {theme.colors.TEXT_PRIMARY};
}}

/* Hauptbereich */

.stApp {{
    background-color: {theme.colors.BACKGROUND};
}}

/* Content */

.main .block-container {{

    max-width: 1600px;

    padding-top: {theme.spacing.MD}px;

    padding-left: {theme.spacing.LG}px;

    padding-right: {theme.spacing.LG}px;

    padding-bottom: {theme.spacing.XL}px;

}}

/* Sidebar */

section[data-testid="stSidebar"] {{

    background-color: {theme.colors.SIDEBAR};

    border-right: 1px solid {theme.colors.BORDER};

}}

/* Buttons */

.stButton button {{

    background-color: {theme.colors.PRIMARY};

    color: white;

    border-radius: {theme.radius.MEDIUM}px;

    border: none;

    padding: 0.6rem 1.3rem;

    transition: all 0.2s ease;

}}

.stButton button:hover {{

    background-color: {theme.colors.PRIMARY_HOVER};

}}

.stButton button:active {{

    background-color: {theme.colors.PRIMARY_ACTIVE};

}}

/* Dataframe */

div[data-testid="stDataFrame"] {{

    border: 1px solid {theme.colors.BORDER};

    border-radius: {theme.radius.LARGE}px;

}}

/* Metrics */

div[data-testid="metric-container"] {{

    background-color: {theme.colors.CARD};

    border-radius: {theme.radius.LARGE}px;

    border: 1px solid {theme.colors.BORDER};

    padding: 20px;

}}

/* Tabs */

button[data-baseweb="tab"] {{

    color: {theme.colors.TEXT_SECONDARY};

}}

button[data-baseweb="tab"][aria-selected="true"] {{

    color: {theme.colors.PRIMARY};

}}

p {
    line-height: 1.6;
    font-size: 16px;
}

li {

    line-height: 1.7;

    margin-bottom: 6px;

}

h1 {

    font-weight:700;

    margin-bottom:12px;

}

h2{

    margin-top:32px;

    margin-bottom:12px;

}

h3{

    margin-top:24px;

    margin-bottom:8px;

}

hr{

    margin-top:32px;

    margin-bottom:32px;

    border-color:#30343C;

}

div[data-testid="metric-container"]{

    padding:24px;

    min-height:140px;

}

div[data-testid="stDataFrame"]{

    border-radius:16px;

    overflow:hidden;

}

section[data-testid="stSidebar"]{

    padding-top:20px;

}



</style>
"""