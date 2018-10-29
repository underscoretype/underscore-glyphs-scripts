#!/usr/bin/python
# -*- coding: utf8 -*-
#MenuTitle: Copy selected layer to other layers
#
import copy

font = Glyphs.fonts[0]
selection = font.selectedLayers

print ""
print ""
print "selection", selection
print "selectedFontMaster", font.selectedFontMaster.id, font.selectedFontMaster.name
print "font masters", [m.id for m in font.masters]
print "masterIndex", font.masterIndex
print ""

masters = [m.id for m in font.masters]

"""
Find all kerning pairs for glyph in master and return them as dict equal to font.kerning, but
specific to the passed in master
"""
def kerningOccurances(glyph, master):
	masterKerning = font.kerning[master]
		
	syncKernings = {}
	for key in masterKerning:
		
		if key == glyph.id or key == glyph.leftKerningKey or key == glyph.rightKerningKey:
			print "glyph %s appears as first in kern pair" % glyph.name
			
		for value in masterKerning[key]:			
			if value == glyph.id or value == glyph.leftKerningKey or value == glyph.rightKerningKey:
				print "glyph %s appears as second in kern pair" % glyph.name
				
				if key not in syncKernings:
					syncKernings[key] = {}
				syncKernings[key][value] = masterKerning[key][value]
				
	print "syncKernings in master %s" % font.masters[master].name, syncKernings
				
	return syncKernings

"""
The kern table contains a dictionary with keys either being a glyph name or a kerning group name
This helper returns either the kerning group or the glyph.name such as font.setKerningForPair takes
"""
def glyphNameOrGroup(nameOrGroup):
	if "@" not in nameOrGroup:
		return [g.name for g in font.glyphs if g.id == nameOrGroup].pop()
	else:
		return nameOrGroup

"""
Helper to determine if a given glyph or class id matches the given group
"""
def isGlyphKernGroup(glyph, group):
	return glyph.id == group or glyph.leftKerningKey == group or glyph.rightKerningKey == group	


if selection:
	for selected in selection:
		glyph = selected.parent
		
		source = glyph.layers[selected.associatedMasterId]		
		otherLayers = [l for l in glyph.layers if l != source and l.layerId in masters]
		otherMasters = [m.id for m in font.masters if m.id != selected.associatedMasterId]
		print "SOURCE", source
		
		for layer in otherLayers:
			cp = copy.copy(source)
			cp.name = layer.name			
			glyph.layers[layer.layerId] = cp
			
		for layer in glyph.layers:
			layer.syncMetrics()
			
		for masterId in otherMasters:
			master = font.masters[masterId]
			print "remove all kerning for glyph %s in master %s" % (glyph.name, master.name)
			print "glyph kernings found in"
			print kerningOccurances(glyph, masterId)
			kerns = kerningOccurances(glyph, masterId)
			if kerns:
				for left in kerns:
					for right in kerns[left]:					
						if isGlyphKernGroup(glyph, left) or isGlyphKernGroup(glyph, right):
							print "remove kerning pair %s : %s" % (left, right)
							font.removeKerningForPair(masterId, left, right)
						
			
		# todo remove removed kerns in other masters
		updateKerns = kerningOccurances(glyph, font.selectedFontMaster.id)
		if updateKerns:
			print "updateKerns for glyph", glyph.name, updateKerns
			for master in font.kerning:
				if master in otherMasters:
					print "update kerns for master", font.masters[master].name
					
					for left in updateKerns:
						if isGlyphKernGroup(glyph, left):
							print "glyph in left kern key"
							
							# update all the passed in right keys & values
							for right in updateKerns[left]:
								value = updateKerns[left][right]
								print "set kerning in master %s for %s : %s = %d" % (font.masters[master].name, glyphNameOrGroup(left), glyphNameOrGroup(right), value)
								font.setKerningForPair(master, glyphNameOrGroup(left), glyphNameOrGroup(right), value)
						
						for right in updateKerns[left]:
							if isGlyphKernGroup(glyph, right):
								print "glyph in right kern key"
								# update all the pair values for this combo
								value = updateKerns[left][right]
								
								print "set kerning in master %s for %s : %s = %d" % (font.masters[master].name, glyphNameOrGroup(left), glyphNameOrGroup(right), value)
								font.setKerningForPair(master, glyphNameOrGroup(left), glyphNameOrGroup(right), value) 