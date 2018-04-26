#!/usr/bin/python
# -*- coding: utf8 -*-
#MenuTitle: Copy kerning for left and right pair in tab from masters 1-3 to 4-6
#
# For MM fonts this code can be used as a template to copy kerning values 
# between masters
#
# TODO: 
#	- iterate the master selection into a dialog box to select arbitrary 
# 	  masters for source target
#
import traceback

font = Glyphs.fonts[0]
tab = font.currentTab

selection = font.selectedLayers[0]
glyph = selection.parent

print selection

	
def copyKerningFromMasterToMaster(source, target):
	type(tab.layers[tab.textCursor+1: tab.textCursor + 2][0]) is GSControlLayer
	
	prev = tab.layers[tab.textCursor-1: tab.textCursor][0]
	curr = tab.layers[tab.textCursor: tab.textCursor + 1][0]
	next = tab.layers[tab.textCursor+1: tab.textCursor + 2][0]
	
	prevGlyph = False
	currGlyph = False
	nextGlyph = False
	
	if type(prev) is not GSControlLayer:
		prevGlyph = prev.parent
		
	if type(curr) is not GSControlLayer:
		currGlyph = curr.parent
		
	if type(next) is not GSControlLayer:
		nextGlyph = next.parent
	
	print "copy left"
	copyKerningFrom(source, target, prevGlyph, currGlyph)
	
	print "copy right"
	copyKerningFrom(source, target, currGlyph, nextGlyph)


def copyKerningFrom(source, target, left, right):
	if not left or not right:
		print "invalid kern pair", left, right
		return
		
	try:
		if left.rightKerningKey and right.leftKerningKey:
			leftKern = left.rightKerningKey
			rightKern = right.leftKerningKey
			kern = font.kerningForPair(source.id, leftKern, rightKern)
			
			# just an arbitrary kern value that is beyond reasonable to be real
			# i.e. will catch Glyph's maxint for "unset"
			if kern > 10000:
				font.removeKerningForPair(target.id, leftKern, rightKern)
				return
								
			font.setKerningForPair(target.id, leftKern, rightKern, kern)
			return
			
		else:
			print "kern groups not found"
	except:
		print traceback.format_exc()


for index, master in enumerate(font.masters):
	print "copy master", index, font.masters[index].name, "to", index + 3, font.masters[index+3].name
 	copyKerningFromMasterToMaster(font.masters[index], font.masters[index+3])
	if index + 1 >= len(font.masters) / 2:
		print "break"
		break
		
		