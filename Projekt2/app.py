"""
app.py

Einstiegspunkt der Anwendung.
"""

from core.startup import initialize_app
from core.session import initialize_session
from core.navigation import sidebar_navigation
from core.router import render_current_page


def main():

    initialize_app()

    initialize_session()

    sidebar_navigation()

    render_current_page()


if __name__ == "__main__":

    main()