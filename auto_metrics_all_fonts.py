#MenuTitle: Vertical metrics
'''
This script will set the ascender, descender and vertical metrics
for all open fonts! I.e. this allows you to set vertical metrics 
for an entire family of fonts that should share vertical metrics,
even though not in the same file.

Inspired by Mark Foley's vertical metrics script: https://github.com/m4rc1e/mf-glyphs-scripts

Logic:
- First finds the highest and lowest extreme from all masters to
  base calculations on.
- winAscender and winDescender span the entire height containing paths
- typo vertical metrics match are based off the upm, line gap is set
  to include the overshoots, i.e. span all the way up to winAscender
- hhea values have no linegap, but this is compensated in an ascender 
  tall enough to span all the way up to winAscender
'''

import math
from helpers import get_font_extremes

def main():
    Glyphs.showMacroWindow()
    new_win_desc = 0
    new_win_asc = 0

    # find the common highest and lowest points of all open fonts
    for font in Glyphs.fonts:
        new_desc, new_asc = get_font_extremes(font)
        if new_desc < new_win_desc:
            new_win_desc = new_desc
        if new_win_asc < new_asc:
            new_win_asc = new_asc

    for font in Glyphs.fonts:
        for master in font.masters:
            vert = master.customParameters

            print 'Updating %s vertical metrics' % master.name

            win_asc = int(new_win_asc)
            win_desc = int(abs(new_win_desc))

            # all descender values are going to sit on the same absolute
            # minimum, independent of actual paths
            master.descender = -win_desc
            # the ascenders filling up the descender to the upm
            master.ascender = font.upm + master.descender

            # include all path areas to prevent clipping
            vert['winAscent'] = win_asc
            vert['winDescent'] = win_desc

            # match real metrics, add line gap from what paths shoot
            # beyond upm
            vert['typoAscender'] = master.ascender
            vert['typoDescender'] = master.descender
            vert['typoLineGap'] = win_asc + win_desc - font.upm

            # include line gap in asender
            vert['hheaAscender'] = win_asc
            vert['hheaDescender'] = master.descender
            vert['hheaLineGap'] = 0

    print 'Done. Updated all masters vertical metrics of all open fonts'


if __name__ == '__main__':
    main()

