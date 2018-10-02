#!/usr/bin/python
# -*- coding: utf8 -*-
#MenuTitle: Sync anchors to other masters
#
# Copy anchors and their position from this master to all others

def syncAnchorsToOtherMasters(layer):
	glyph = layer.parent
	anchors = layer.anchors

	print "anchors", anchors
	
	if not anchors:
		return
	
	for l in glyph.layers:
		print l, l == layer
		if l != layer:
			l.anchors = anchors



font = Glyphs.fonts[0]
selection = font.selectedLayers[0]

if selection:
	syncAnchorsToOtherMasters(selection)