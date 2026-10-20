from pprint import pprint

import numpy as np
from PIL import Image

from themes.catppuccin import catppuccin_mocha_rgb

with open("sample/puzzle1.txt", "r") as f:
    data = [l.split() for l in f.readlines()]

pprint(data)

r, c = len(data), len(data[0])

img = np.empty((64 * (c//2) + 2, 64 * (r//2) + 2, 3), dtype=np.uint8)

fill_color = catppuccin_mocha_rgb["Crust"]
out_color = catppuccin_mocha_rgb["Overlay 0"]
edge_color = catppuccin_mocha_rgb["Yellow"]
default_edge_color = catppuccin_mocha_rgb["Base"]

edges_with_color = []

for row, row_data in enumerate(data):
    for col, cell_data in enumerate(row_data):
        x, y = 64 * (col//2) + 1, 64 * (row//2) + 1

        # Cell
        if row % 2 and col % 2:
            color = fill_color

            if cell_data.startswith("c"):
                color = out_color

            img[y+1:y+63, x+1:x+63] = color
        
        # Horizontal edge
        if not row % 2 and col % 2:
            color = default_edge_color
            # Forced edge
            if cell_data.startswith("E"):
                color = edge_color
            # First row
            if row == 0:
                if data[row+1][col].startswith("C"):
                    color = edge_color
            # Last row
            elif row == len(data)-1:
                if data[row-1][col].startswith("C"):
                    color = edge_color
            # Mid row
            else:
                if data[row-1][col][0] != data[row+1][col][0]:
                    color = edge_color
            if color == edge_color:
                edges_with_color.append((y-1, x-1, y+1, x+65))
            else:
                img[y-1:y+1, x-1:x+65] = color
        
        # Vertical edge
        if row % 2 and not col % 2:
            color = default_edge_color
            # Forced edge
            if cell_data.startswith("E"):
                color = edge_color
            # First col
            if col == 0:
                if data[row][col+1].startswith("C"):
                    color = edge_color
            # Last row
            elif col == len(data[0])-1:
                if data[row][col-1].startswith("C"):
                    color = edge_color
            # Mid row
            else:
                if data[row][col-1][0] != data[row][col+1][0]:
                    color = edge_color
            if color == edge_color:
                edges_with_color.append((y-1, x-1, y+65, x+1))
            else:
                img[y-1:y+65, x-1:x+1] = color

for y1, x1, y2, x2 in edges_with_color:
    img[y1:y2, x1:x2] = edge_color

Image.fromarray(img).save("img/map.png")