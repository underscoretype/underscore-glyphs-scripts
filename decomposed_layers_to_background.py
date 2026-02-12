"""
Script to make a decomposed copy of each selected glyph's layer in the background 
layer, and add a rectangle to the background layer to extend the work glyph width.
"""
import math

def metrics_rect(layer, x, y, width, height, angle, xHeight):
	# Create a new path
	rectangle_path = GSPath()

	# Create nodes for the rectangle (clockwise from bottom-left)
	rectangle_path.nodes = [
	    GSNode((x, y), GSLINE),                    # Bottom-left
	    GSNode((x + width, y), GSLINE),           # Bottom-right
	    GSNode((x + width, y + height), GSLINE),  # Top-right
	    GSNode((x, y + height), GSLINE)           # Top-left
	]

	# Close the path
	rectangle_path.closed = True
	
	# Skew the rectangle, offset to the left to match 0,0 origin
	rectangle_path.applyTransform([
		1, # x scale factor
		0, # x skew factor
		math.tan(math.radians(angle)), # y skew factor
		1, # y scale factor
		-math.tan(math.radians(angle))*xHeight/2, # x position
		0  # y position
	])

	# Add the path to the layer
	layer.paths.append(rectangle_path)
	
for g in Glyphs.font.selection:
	g.beginUndo()
	print(f"Making background copy for {g}")
	for l in g.layers:
		l.background = l.copy()
		l.background.decomposeComponents()
		# Adding a rectangle to match the current bounds, so we can compare after
		metrics_rect(l.background, 0, l.bounds.origin.y, l.width, l.bounds.size.height, l.master.italicAngle, l.master.xHeight)

	g.endUndo()