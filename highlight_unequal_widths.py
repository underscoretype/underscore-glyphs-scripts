#MenuTitle: Highlight unequal widths master 1-3 to 4-6
'''
Simple script to compare the width of glyphs in the font across masters
'''
import traceback

font = Glyphs.fonts[0]

for glyph in font.glyphs:
	if glyph.layers[0].width != glyph.layers[3].width or glyph.layers[1].width != glyph.layers[4].width or glyph.layers[2].width != glyph.layers[5].width:
		glyph.color = 9
		print glyph
	else:
		if glyph.color == 9:
			glyph.color = 9223372036854775807