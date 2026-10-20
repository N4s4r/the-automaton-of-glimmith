from pprint import pprint

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

with open("sample/puzzle1.txt", "r") as f:
    data = [l.split() for l in f.readlines()]

pprint(data)

fig, ax = plt.subplots()

for row, row_data in enumerate(data):
    for col, cell_data in enumerate(row_data):
        x, y = col // 2, row // 2

        fill_color = "#11111b"
        out_color = "#313244"
        edge_color = "#f9e2af"
        edge_color = "#ff0000"
        default_edge_color = "#181825"

        # Cell
        if row % 2 and col % 2:
            color = fill_color
            plt.plot(x, y)

            if cell_data.startswith("c"):
                color = out_color

            square = Rectangle((x, y), 1, 1, fill=True, color=color)
            ax.add_patch(square)
        
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
            plt.plot([x, x+1], [y, y], color=color)
        
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
            plt.plot([x, x], [y, y+1], color=color)

ax.invert_yaxis()
plt.savefig("img/map.png", dpi=150, bbox_inches="tight")
plt.close()