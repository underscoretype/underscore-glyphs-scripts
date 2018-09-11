'''
Some helper functions that can be reused within scripts
'''
import math


# From https://github.com/m4rc1e/mf-glyphs-scripts/tree/master/Fixes
def get_font_extremes(font, *args):
    '''find the tallest and shortest glyphs in all masters'''
    lowest = 0.0
    highest = 0.0
    highest_name = ''
    lowest_name = ''

    masters_count = len(font.masters)

    if args:
        glyphs = [font.glyphs[i] for i in args]
    else:
        glyphs = font.glyphs

    for glyph in glyphs:
        for i in range(masters_count):
            glyph_ymin = glyph.layers[i].bounds[0][-1]
            glyph_ymax = glyph.layers[i].bounds[-1][-1] + glyph.layers[i].bounds[0][-1]
            if glyph_ymin < lowest:
                print "new lowest (%f) %s %s %s" % (glyph_ymin, glyph.name, font.familyName, glyph.layers[i].name)
                lowest = glyph_ymin
            if glyph_ymax > highest:
                print "new highest (%f) %s %s %s" % (glyph_ymax, glyph.name, font.familyName, glyph.layers[i].name)
                highest = glyph_ymax

    return math.ceil(lowest), math.ceil(highest)