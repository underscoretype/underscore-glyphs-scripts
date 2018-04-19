#!/usr/bin/python
# -*- coding: utf8 -*-
#MenuTitle: Copy selected glyphs to second font
#
# Copy and overwrite the selected glyphs to the second font

source = Glyphs.fonts[0]
target = Glyphs.fonts[1]
	
def copyGlyph(glyph):
	if len(source.masters) != len(target.masters):
		print "Source (%s) and target (%s) font masters differ. Copying the glyphs might have unexpected results." % (source.familyName, target.familyName)
	
	if glyph.name in target.glyphs:
		# if glyph exists, delete current contents
		print "Existing glyph %s deleted from %s and replaced with copied glyph %s" % (glyph.name, source.familyName, glyph.name)
		del(target.glyphs[glyph.name])

	# if glyph does not yet exist, copy it over as such
	print "Copied glyph %s" % glyph.name
	target.glyphs.append(glyph.copy())



if source.selectedLayers:
	for layer in source.selectedLayers:
 		copyGlyph(layer.parent)
else:
	print "Nothing selected"