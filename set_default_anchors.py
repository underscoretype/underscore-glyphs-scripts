#!/usr/bin/python
# -*- coding: utf8 -*-
#MenuTitle: Set default anchors
#
# An opinionated to add some default anchors to letters
# - Will only add not yet existing anchors
# - Positions are crude, so mostly top or bottom aligned centered anchor
# - Only adds to the selected Layer(s)
# - Pressumed desired anchor positions: cap height, x height, baseline

font =  Glyphs.font

for layer in font.selectedLayers:
	glyph = layer.parent
	info = glyph.glyphInfo
	
	master = font.masters[layer.associatedMasterId]

	if not master.capHeight or not master.xHeight or not master.descender:
		print "Font master needs to have capHeight, xHeight and descender values."
		continue
	
	if info.category != "Letter":
		continue
	
	if not glyph.glyphInfo.anchors:
		print "Glyph %s has no default anchors defined, skipping." % glyph.name
		continue

	for anchor in glyph.glyphInfo.anchors:
		existingAnchor = anchor in [a.name for a in layer.anchors]
		x = 0
		y = 0
		
		if not existingAnchor:
			# the default font data has some anchors like "bottom@descender"
			# for those, grab only the part before the @ for our new anchor
			# name; it's still available further down for detecting
			anchorName = anchor.split("@", 1)[0]

			layer.anchors[anchorName] = GSAnchor()
			x = layer.width / 2
			
			if info.subCategory == "Uppercase":
				if anchor == "top":
					y = master.capHeight
				elif anchor == "center":
					y = master.capHeight / 2
		
			if info.subCategory == "Lowercase":
				# for lowercase letters with paths at cap height or beyond
				# set "top" anchors to capHeight, not xHeight
				atCapHeight = layer.bounds.size.height + min(0, layer.bounds.origin.y) >= master.capHeight

				if anchor == "top":
					if atCapHeight:
						y = master.capHeight
					else:
						y = master.xHeight
				elif anchor == "center":
					y = master.capHeight / 2
				elif anchor == "bottom@descender":
					y = master.descender

				
			# some anchors we use the same default position regardless of case
			if anchor == "ogonek":
				x = layer.bounds.origin.x + layer.bounds.size.width
			elif anchor == "topleft":
				y = master.capHeight
				x = layer.bounds.origin.x
			elif anchor == "topright":
				y = master.capHeight
				x = layer.bounds.origin.x + layer.bounds.size.width

			print "add missing anchor %s in glyph %s at %d, %d" % (anchor, glyph.name, x, y) 		
			layer.anchors[anchorName].position = NSPoint(x, y)
			
		# else: Could perform sanity checks on existing anchors
		