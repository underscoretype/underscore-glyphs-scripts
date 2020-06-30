# MenuTitle: Render tab text in all masters
# GlyphsApp script to show the text in the current tab in all masters of the font
# (c) 2020 Johannes 'kontur' Neumeier <hello@underscoretype.com>

tab = Glyphs.font.currentTab

# The layers of the text as initially in the tab
initialText = []

# Skip certain masters (in their order in the font info, first master 0)
# Eg: skipMasters = [1, 3, 5, 7] will skip the second, forth, sixth and eight masters)
skipMasters = []

# Loop through all masters in the font
for i in range(len(Glyphs.font.masters)):
    if i in skipMasters:
        continue

    # For the first master, we transform the current tab content to that master
    if i == 0:
        transformed = []

        # Get the text in the i'th layer, which is the 0'th master, e.g. the first master
        for l in tab.layers:
            masterLayer = [
                l for l in l.parent.layers if l.master == Glyphs.font.masters[i]][0]
            transformed.append(masterLayer)

        # Replace the current tab content with the same text set in the first master
        tab.layers = transformed

        # Add a line break
        tab.layers.append(GSControlLayer(10))

        # Save the initial Text for setting the other masters in that same text
        initialText = list(tab.layers)

    # For all others masters, we transform the current tab content to that master
    else:
        for l in initialText:
            # Letter by letter append the same text as the initial text in the i'th master/layer
            tab.layers.append(l.parent.layers[i])
