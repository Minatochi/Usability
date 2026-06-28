"""
Top Insight.
"""

import streamlit as st

from analysis.insights import (
    top_artist,
    top_track,
    top_album,
)


def render_top_insight(df):

    st.subheader("💡 Top Insight")

    st.write(
        f"""
**Lieblingsartist**

{top_artist(df)}

---

**Meistgehörter Song**

{top_track(df)}

---

**Meistgehörtes Album**

{top_album(df)}
"""
    )