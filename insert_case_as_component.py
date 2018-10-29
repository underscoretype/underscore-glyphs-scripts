#!/usr/bin/python
# -*- coding: utf8 -*-
#MenuTitle: Insert other case as component
#
# Into the selected layers insert their upper/lowercase equivalent as component

font = Glyphs.fonts[0]
selection = font.selectedLayers

if selection:
	for layer in selection:
		glyph = layer.parent		
		uni = unichr(int(glyph.unicode, 16))
		
		if uni.isupper():
			# add uppercase as component to lowercase
			otherCase = uni.lower()
			
		elif uni.islower():			
			# add lowercase as component to uppercase
			otherCase = uni.upper()
			
		glyphsInfo = Glyphs.objectWithClassName_("GSGlyphsInfo")
		uniOther = "{0:0{1}X}".format(ord(otherCase), 4)
		otherGlyph = font.glyphs[ glyphsInfo.niceGlyphNameForName_("uni" + uniOther) ]
		
		for lay in glyph.layers:
			if otherGlyph.name not in [g.componentName for g in lay.components]:
				lay.components.append(GSComponent(otherGlyph))