"""
theme.py

Fasst sämtliche Design Tokens
in einem Theme zusammen.
"""

from dataclasses import dataclass

from styles import colors
from styles import spacing
from styles import typography
from styles import radius
from styles import shadows


@dataclass(frozen=True)
class Theme:
    colors = colors
    spacing = spacing
    typography = typography
    radius = radius
    shadows = shadows


theme = Theme()