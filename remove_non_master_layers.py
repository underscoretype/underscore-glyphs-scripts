#!/usr/bin/python
# -*- coding: utf8 -*-
#MenuTitle: Remove all non-master layers
# Note: Also removes Brace and Bracket layers!!

font = Glyphs.fonts[0]

ignoreBacketAndBraceLayers = False

print("Font masters", font, [n.name for n in font.masters])
masterNames = [n.name for n in font.masters]

for glyph in font.glyphs:
	if glyph.export:
		layers = []
		for layer in glyph.layers:
			if layer.name in masterNames:
				if ignoreBacketAndBraceLayers and ("{" in layer.name or "[" in layer.name):
					print("Skip bracket or brace layer", glyph.name, layer.name)
					continue

				layers.append(layer)
			else:
				print("Drop", glyph.name, layer.name)
				continue
		
		if len(glyph.layers) > len(layers):
			glyph.layers = layers