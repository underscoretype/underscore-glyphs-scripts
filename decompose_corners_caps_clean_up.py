#MenuTitle: Decompose Corners and Caps & clean up
# -*- coding: utf-8 -*-
__doc__="""
An slightly expanded @mekkablue script that:
Decomposes all corner and cap components in selected glyphs. Reports to Macro Window.
"""

thisFont = Glyphs.font
selectedLayers = thisFont.selectedLayers

def process( thisLayer ):
	count = len([h for h in Layer.hints if h.type in (CORNER,CAP) ])
	if count:
		thisLayer.decomposeCorners()
		thisLayer.cleanUpPaths()
		thisLayer.correctPathDirection()
		print "-- Decomposed %i caps and/or corners" % count

Glyphs.clearLog()
for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	print "Processing", thisGlyph.name
	thisGlyph.beginUndo()
	process( thisLayer )
	thisGlyph.endUndo()
