#!/usr/bin/python
# -*- coding: utf8 -*-
#MenuTitle: Get metrics string
#
# Open a tab with the selected letter padded in some metrcis testing characters

font = Glyphs.font
layer = font.selectedLayers[0]

def wrap(letter, padding, occurances):
	text = padding
	for i in range(occurances):
		text += letter + padding
	return text

	
def metricsString(letter):
	paddings = [u"H", u"O", u"A", u"n", u"o", u"v", u"-", u".", u"(", u")", u"“", u"„", u"»", u"«"]
	text = ""
	
	# if the selection has components, print the first of in one row so it's easy 
	# to manipulate them without messing up the metrics string we are printing below
	components = iterateComponents(font.glyphs[letter].layers[font.masterIndex])
	if components:
		text = "".join(["/" + x.parent.name for x in components]) + "\n"
	
	# for every tab print HOHO row first	
	text = text + wrap(u"H", u"O", 10) + "\n"
	
	# escape a slash glyph
	if letter == "/":
		letter = "//"	

	# print a row for each padding char defined
	for pad in paddings:
		text = text + wrap(letter, pad, 10) + "\n"
		
	# for every tab print nono row last
	text = text + wrap(u"n", u"o", 10)
	return text


def iterateComponents(layer):
	components = []
	if layer.components:
		for component in layer.components:
			componentGlyphLayer = component.component.layers[font.masterIndex]
			
			if componentGlyphLayer.paths:
				components.append(componentGlyphLayer)				
				
			if componentGlyphLayer.components:
				return iterateComponents(componentGlyphLayer)
				
	return list(set(components))
	


def getSelected():
	selected = []
	selection = font.selectedLayers
	if selection:
		for layer in selection:
			glyph = layer.parent
    			if glyph.unicode:
        			selected.append( unichr(int(glyph.unicode, 16) ) )
	return selected

for glyph in getSelected():
	Glyphs.font.newTab(metricsString(glyph))