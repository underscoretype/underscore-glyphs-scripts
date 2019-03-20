#!/usr/bin/python
# -*- coding: utf8 -*-
#MenuTitle: Sync anchors to other masters
#
# Copy anchors and their position from this master to all others

def syncAnchorsToOtherMasters(layer):
	glyph = layer.parent
	anchors = layer.anchors
	anchorsNames = [a.name for a in anchors]
	
	# also run when syncing "empty" anchors to other masters, e.g. removing
	# all anchors for all layers; otherwise the following could be retained
# 	if not anchors:
# 		return
	
	for l in glyph.layers:
		if l != layer:
			layeranchors = [la.name for la in l.anchors]
			
			# add missing anchors in other layers
			for a in anchors:
				if a.name not in layeranchors:
					# position the x component of synced anchors at the same percentual
					# position in the glyph advance width					
					oldXPercent = a.position.x / layer.width
					newX = int(l.width * oldXPercent)
					
					# when copying an anchor that is on a metrics line in the original
					# layer try to insert the synced anchor at same metrics line in that layer
					newY = a.position.y
					for ypos in ["descender", "xHeight", "capHeight", "ascender"]:
						if a.position.y == layer.master.__getattribute__(ypos):
							# print "Set anchor y also to %s" % ypos
							newY = l.master.__getattribute__(ypos)

					l.anchors = [GSAnchor(a.name, NSPoint(newX, newY)) for a in anchors]
					
			# remove anchors in layer that are not in source
			l.anchors = [a for a in l.anchors if a.name in anchorsNames]

font = Glyphs.fonts[0]
selection = font.selectedLayers[0]

if selection:
	syncAnchorsToOtherMasters(selection)