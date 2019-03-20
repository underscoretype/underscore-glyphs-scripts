#!/usr/bin/python
# -*- coding: utf8 -*-
#MenuTitle: Sync master meta from first to second font
#
# Adds (full copy) or updates (omits italicAngle, stems, guides) the font masters of the current active font to the second font 
source = Glyphs.fonts[0]
target = Glyphs.fonts[1]

def syncMaster(master):
	print "source", master, master.id, master.name
	
	# match source and target masters by name
	
	if master.name in [m.name for m in target.masters]:
		# master exists
		print "Updating master %s" % master.name
		hit = [m for m in target.masters if m.name == master.name][0]
		old = target.masters[hit.id].copy()
		target.masters[hit.id] = master.copy()
		target.masters[hit.id].italicAngle = old.italicAngle
		target.masters[hit.id].verticalStems = old.verticalStems
		target.masters[hit.id].horizontalStems = old.horizontalStems
		target.masters[hit.id].guides = old.guides
		
	else:
		# master doesn't exit
 		print "Adding new master %s" % master.name
 		target.masters.append(master.copy()) 		

for master in source.masters:
	syncMaster(master)