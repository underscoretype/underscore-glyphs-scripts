#MenuTitle: Delete All Hints in Glyph master
# -*- coding: utf-8 -*-
__doc__="""
Removes all PS hints in the selected layers.
"""

for layer in Glyphs.font.selectedLayers:
	layer.hints = []