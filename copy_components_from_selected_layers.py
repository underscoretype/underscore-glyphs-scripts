# For all selected glyphs set the same components as the selected layer, match (delete or add) anchors and paths to match

from copy import copy

print(Glyphs.font.selectedLayers)

for selected in Glyphs.font.selectedLayers:
	print()
	print("selected", selected)
	components = selected.components
	print("selected layer components", selected.components)
	print("selected layer anchors", selected.anchors)
	print("selected layer paths", selected.paths)
	for l in [l for l in selected.parent.layers if l != selected]:
		print("layer", l)
		l.shapes = []
		
		#print(copy(selected.shapes))
		#l.shapes = copy(selected.shapes)
		for s in selected.shapes:
			print(s)
			l.shapes.append(GSComponent(Glyphs.font.glyphs[s.componentName]))
			
			