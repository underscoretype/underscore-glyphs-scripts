#!/usr/bin/python
# -*- coding: utf8 -*-
#MenuTitle: Copy selected layers to second font
#
# Copy and overwrite all selected layers and write them to the second font

# TODO recursively copy components first

source = Glyphs.fonts[0]
target = Glyphs.fonts[1]
	
def copyLayer(layer):
	
	glyph = layer.parent
	
	if len(source.masters) != len(target.masters):
		print "Source (%s) and target (%s) font masters differ. Copying the glyphs might have unexpected results." % (source.familyName, target.familyName)
	
	if glyph.name not in target.glyphs:
		# glyph does not exist, create it
		print "Glyph for this layer does not exist in font, copied entire glyph"
		target.glyphs.append(glyph.copy())
	else:
		print "Copy layer %s" % layer.name
		hit = [l for l in target.glyphs[glyph.name].layers if l.name == layer.name][0]
		target.glyphs[glyph.name].layers[hit.layerId] = layer.copy()


if source.selectedLayers:
	for layer in source.selectedLayers:
		copyLayer(layer)
else:
	print "Nothing selected"