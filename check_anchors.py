#!/usr/bin/python
# -*- coding: utf8 -*-
#MenuTitle: Check for self referential anchors
#
# Find glyphs that have both a _xxx and xxx anchor (possible from accidental decomposition)

font = Glyphs.fonts[0]
review = []

for g in font.glyphs:
	for l in g.layers:
		if len(l.anchors) > 1:
			all = [a.name.replace("_", "") for a in l.anchors]
			count = len(all)
			unique = len(list(set(all)))
			if count != unique and g not in review:
				review.append(g)
				
if len(review) > 0:
	# either review manually
	font.newTab(" ".join(["/" + str(g.name) for g in review]))

	# or remove a specific anchor, uncomment:
	# for g in review:
	# 	for l in g.layers:
	# 		l.anchors = [a for a in l.anchors if a.name != "_top"]
	
			