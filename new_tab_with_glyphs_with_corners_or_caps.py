#MenuTitle: Tab with glyphs containing corners or caps
'''
Simple script to open a new tab with all glyphs that have 
corners or caps in any of their layers
'''
font = Glyphs.fonts[0]
glyphsWithCornersOrCaps = []

for glyph in font.glyphs:
    for layer in glyph.layers:
        for hint in layer.hints:
            if hint.type == 16 or hint.type == 17: # 16-corner 17-cap
                glyphsWithCornersOrCaps.append(glyph)

glyphsWithCornersOrCaps = set(glyphsWithCornersOrCaps)
font.newTab(" ".join(["/" + g.name for g in glyphsWithCornersOrCaps]))
