"""
Top Insight Card.
"""

import streamlit as st

from analysis.insights import (
    top_album,
    top_artist,
    top_track,
)


def render_top_insight(df) -> None:
    """
    Zeigt die wichtigsten Erkenntnisse.
    """

    if df is None:
        return

    st.subheader("💡 Top Insights")

    st.markdown(
        f"""
**🎤 Lieblingsartist**

{top_artist(df)}

---

**🎵 Meistgehörter Song**

{top_track(df)}

---

**💿 Meistgehörtes Album**

{top_album(df)}
"""
    )