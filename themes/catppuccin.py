catppuccin_mocha_hex = {
    "Rosewater": "#f5e0dc",
    "Flamingo":"#f2cdcd",
    "Pink":"#f5c2e7",
    "Mauve":"#cba6f7",
    "Red":"#f38ba8",
    "Maroon":"#eba0ac",
    "Peach":"#fab387",
    "Yellow":"#f9e2af",
    "Green":"#a6e3a1",
    "Teal":"#94e2d5",
    "Sky":"#89dceb",
    "Sapphire":"#74c7ec",
    "Blue":"#89b4fa",
    "Lavender":"#b4befe",
    "Text":"#cdd6f4",
    "Subtext 1":"#bac2de",
    "Subtext 0":"#a6adc8",
    "Overlay 2":"#9399b2",
    "Overlay 1":"#7f849c",
    "Overlay 0":"#6c7086",
    "Surface 2":"#585b70",
    "Surface 1":"#45475a",
    "Surface 0":"#313244",
    "Base":"#1e1e2e",
    "Mantle":"#181825",
    "Crust":"#11111b",
}

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

catppuccin_mocha_rgb = {
    name: hex_to_rgb(color) for name, color in catppuccin_mocha_hex.items()
}