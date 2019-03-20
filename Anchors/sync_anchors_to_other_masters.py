#!/usr/bin/python
# -*- coding: utf8 -*-
#MenuTitle: Sync anchors to other masters
#
# Copy anchors and their position from this master to all others

def syncAnchorsToOtherMasters(layer):
	glyph = layer.parent
	anchors = layer.anchors
	anchorsNames = [a.name for a in anchors]
	
	if not anchors:
		return
	
	for l in glyph.layers:
		if l != layer:
			layeranchors = [la.name for la in l.anchors]
			
			# add missing anchors in other layers
			for a in anchors:
				if a.name not in layeranchors:
					# TODO position new anchors smartly; either relative to original, or as per set_default_anchors.py
					l.anchors = [GSAnchor(a.name, NSPoint(a.x, a.y)) for a in anchors]
					
			# remove anchors in layer that are not in source
			l.anchors = [a for a in l.anchors if a.name in anchorsNames]

font = Glyphs.fonts[0]
selection = font.selectedLayers[0]

if selection:
	syncAnchorsToOtherMasters(selection)