# GlyphsApp script to show the text in the current tab in all masters of the font
# (c) 2020 Johannes 'kontur' Neumeier <hello@underscoretype.com>

tab = Glyphs.font.currentTab

# The layers of the text as initially in the tab
initialText = [l.parent for l in tab.composedLayers]

# Skip certain masters (in their order in the font info, first master 0)
# Eg: skipMasters = [1, 3, 5, 7] will skip the second, forth, sixth and eight masters)
skipMasters = []

newLayers = []

# Loop through all masters in the font
for i, master in enumerate(Glyphs.font.masters):
    if i in skipMasters:
        continue

    for g in initialText:
        # Letter by letter append the same text as the initial text in the master
        newLayers.append(g.layers[master.id])

    newLayers.append(GSControlLayer(10))

tab.layers = newLayers
