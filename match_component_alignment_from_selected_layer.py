# Match layer components alignment settings from selected layer!

print(f"Copy component automatic alignment from selected layers to all other layers")

def syncAlignment(selected):
	source = [c.automaticAlignment for c in selected.components]
	print(f"Copy component automatic alignment from layer {selected}: {source}")	
	g = selected.parent
	g.beginUndo()
	for l in g.layers:
		for i, c in enumerate(l.components):
			if c.automaticAlignment != source[i]:
				c.automaticAlignment = source[i]
				print(f"{l}: Update component {c} alignment from selected layer: {source[i]}")
			
	g.endUndo()
	
for selectedLayer in Glyphs.font.selectedLayers:
	syncAlignment(selectedLayer)


print("All components alignment as in selected layer")