#!/usr/bin/python
# -*- coding: utf8 -*-
#MenuTitle: Copy selected paths to other masters
#
# Copy the selected paths (of which any node is selected) to all other masters

font = Glyphs.fonts[0]
layer = Glyphs.font.currentTab.activeLayer()
glyph = layer.parent
selection = layer.selection
otherLayers = [l for l in glyph.layers if l.layerId != layer.layerId]

def layerHasIdenticalPath(layer, path):
	for p in layer.paths:
		if len(p.nodes) != len(path.nodes) or len(p.segments) != len(path.segments):
			continue
		
		for i, n in enumerate(path.nodes):
			if (n.x == p.nodes[i].x and n.y == p.nodes[i].y and n.type == p.nodes[i].type) != True:
				return False
				
		return True


# step through other layers and sync selection:
if selection:
	copyPaths = []
	for node in selection:
		if node.parent not in copyPaths:
			copyPaths.append(node.parent)
		
	if otherLayers:
		for o in otherLayers:
			for p in copyPaths:
				copy = p.copy()
				if layerHasIdenticalPath(o, p) == False:
					o.addPath_(copy)