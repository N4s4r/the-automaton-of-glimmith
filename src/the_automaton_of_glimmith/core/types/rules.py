from enum import IntFlag

"""
Glimmith rules that are applied globally, like mismatch or loopy, as a flag array
"""

# 32 bit: 24 (rule), 4(first parameter), 4(second parameter)
# 2 parameters only applicable to range
class Rules(IntFlag):

    Shape_bank = 1 << 8 # if toggled, solution will have to use only shapes from the Shapes map param
    Rose_windows = 1 << 9
    Gemini = 1 << 10
    Delta = 1 << 11
    Precision = 1 << 12 # 1 param
    Polynomio = 1 << 13
    Mingle_shape = 1 << 15
    Area_number = 1 << 16
    Match = 1 << 17
    Palisade = 1 << 18

    Mismatch = 1 << 14 # it knows what it did

    Solitude = 1 << 19
    Range = 1 << 20 # 2 params
    Minimum = 1 << 21 # 1 param
    Maximum = 1 << 22 # 1 param
    Boxy = 1 << 23
    Non_Boxy = 1 << 24
    Size_separation = 1 << 25
    Bricky = 1 << 26
    Loopy = 1 << 27
    Inequality = 1 << 28
    Difference = 1 << 29
    Watchtower = 1 << 30
    Compass = 1 << 31
