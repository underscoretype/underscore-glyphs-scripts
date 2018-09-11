#!/usr/bin/python
# -*- coding: utf8 -*-
#MenuTitle: Set missing kerning groups from first component

font = Glyphs.font
selection = font.selection
master = font.masterIndex

if selection:
	for glyph in selection:
		if glyph.layers[master].components:
			first = glyph.layers[master].components[0]
			componentGlyph = font.glyphs[first.name]
			
			if glyph.leftKerningGroup is None and componentGlyph.leftKerningGroup is not None:
				glyph.leftKerningGroup = componentGlyph.leftKerningGroup
				
			if glyph.rightKerningGroup is None and componentGlyph.rightKerningGroup is not None:
				glyph.rightKerningGroup = componentGlyph.rightKerningGroup