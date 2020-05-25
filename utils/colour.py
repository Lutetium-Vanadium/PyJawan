from enum import Enum, unique

def _hexFromString(string: str): 
    origstr = string[::-1]
    string = origstr.upper()
    val = 0 
    for i in range(len(string)): 
        if string[i].isdigit(): 
            val += 16**i * int(string[i]) 
        elif 65 <= ord(string[i]) <= 70: 
            val += 16**i * (ord(string[i]) - 55) 
        else: 
            raise ValueError("Unknown character " + origstr[i]) 
 
    return val 

def _colourFromList(lst):
    for i in lst:
        if not isinstance(i, int):
            raise TypeError(f"{i} must be of type int")
    return lst[::-1]

def colour(r, g = None, b = None):
    if g == None and b == None:
        if isinstance(r, int):
            red   = (r >> 16) & 0xff
            green = (r >>  8) & 0xff
            blue  = (r >>  0) & 0xff

            return [blue, green, red]   # Numpy uses colours the other way
        if isinstance(r, (list, tuple)):
            if len(r) != 3:
                raise ValueError("Colours should consist of only 3 values.")
            return _colourFromList(r)
        if isinstance(r, str):
            if r[0] != "#" or (len(r) != 7 and len(r) != 4):
                raise ValueError("Colours should be in the form '#rrggbb' or '#rgb'\nIf in the form '#rgb' it will automaticallty repeat the r, g, b values.\neg: #345 => #334455")
            if len(r) == 4:
                red = _hexFromString(r[1])
                green = _hexFromString(r[2])
                blue = _hexFromString(r[3])
            else:
                red = _hexFromString(r[1:3])
                green = _hexFromString(r[3:5])
                blue = _hexFromString(r[5:7])
                
            return [blue, green, red]
        raise TypeError("Unknwon Type " + type(r))
    elif g == None or b == None:
        raise ValueError("This function only accepts either one or three arguments")

    return _colourFromList([r, g, b])

@unique
class Colours(Enum):
    AliceBlue = colour("#F0F8FF")
    AntiqueWhite = colour("#FAEBD7")
    Aquamarine = colour("#7FFFD4")
    Azure = colour("#F0FFFF")
    Beige = colour("#F5F5DC")
    Bisque = colour("#FFE4C4")
    Black = colour("#000000")
    BlanchedAlmond = colour("#FFEBCD")
    Blue = colour("#0000FF")
    BlueViolet = colour("#8A2BE2")
    Brown = colour("#A52A2A")
    BurlyWood = colour("#DEB887")
    CadetBlue = colour("#5F9EA0")
    Chartreuse = colour("#7FFF00")
    Chocolate = colour("#D2691E")
    Coral = colour("#FF7F50")
    CornflowerBlue = colour("#6495ED")
    Cornsilk = colour("#FFF8DC")
    Crimson = colour("#DC143C")
    Cyan = colour("#00FFFF")
    DarkBlue = colour("#00008B")
    DarkCyan = colour("#008B8B")
    DarkGoldenRod = colour("#B8860B")
    DarkGray = colour("#A9A9A9")
    DarkGreen = colour("#006400")
    DarkKhaki = colour("#BDB76B")
    DarkMagenta = colour("#8B008B")
    DarkOliveGreen = colour("#556B2F")
    DarkOrange = colour("#FF8C00")
    DarkOrchid = colour("#9932CC")
    DarkRed = colour("#8B0000")
    DarkSalmon = colour("#E9967A")
    DarkSeaGreen = colour("#8FBC8F")
    DarkSlateBlue = colour("#483D8B")
    DarkSlateGray = colour("#2F4F4F")
    DarkTurquoise = colour("#00CED1")
    DarkViolet = colour("#9400D3")
    DeepPink = colour("#FF1493")
    DeepSkyBlue = colour("#00BFFF")
    DimGray = colour("#696969")
    DodgerBlue = colour("#1E90FF")
    FireBrick = colour("#B22222")
    FloralWhite = colour("#FFFAF0")
    ForestGreen = colour("#228B22")
    Fuchsia = colour("#FF00FF")
    Gainsboro = colour("#DCDCDC")
    GhostWhite = colour("#F8F8FF")
    Gold = colour("#FFD700")
    GoldenRod = colour("#DAA520")
    Gray = colour("#808080")
    Green = colour("#008000")
    GreenYellow = colour("#ADFF2F")
    HoneyDew = colour("#F0FFF0")
    HotPink = colour("#FF69B4")
    IndianRed = colour("#CD5C5C")
    Indigo = colour("#4B0082")
    Ivory = colour("#FFFFF0")
    Khaki = colour("#F0E68C")
    Lavender = colour("#E6E6FA")
    LavenderBlush = colour("#FFF0F5")
    LawnGreen = colour("#7CFC00")
    LemonChiffon = colour("#FFFACD")
    LightBlue = colour("#ADD8E6")
    LightCoral = colour("#F08080")
    LightCyan = colour("#E0FFFF")
    LightGoldenRodYellow = colour("#FAFAD2")
    LightGray = colour("#D3D3D3")
    LightGreen = colour("#90EE90")
    LightPink = colour("#FFB6C1")
    LightSalmon = colour("#FFA07A")
    LightSeaGreen = colour("#20B2AA")
    LightSkyBlue = colour("#87CEFA")
    LightSlateGray = colour("#778899")
    LightSteelBlue = colour("#B0C4DE")
    LightYellow = colour("#FFFFE0")
    Lime = colour("#00FF00")
    LimeGreen = colour("#32CD32")
    Linen = colour("#FAF0E6")
    Maroon = colour("#800000")
    MediumAquaMarine = colour("#66CDAA")
    MediumBlue = colour("#0000CD")
    MediumOrchid = colour("#BA55D3")
    MediumPurple = colour("#9370DB")
    MediumSeaGreen = colour("#3CB371")
    MediumSlateBlue = colour("#7B68EE")
    MediumSpringGreen = colour("#00FA9A")
    MediumTurquoise = colour("#48D1CC")
    MediumVioletRed = colour("#C71585")
    MidnightBlue = colour("#191970")
    MintCream = colour("#F5FFFA")
    MistyRose = colour("#FFE4E1")
    Moccasin = colour("#FFE4B5")
    NavajoWhite = colour("#FFDEAD")
    Navy = colour("#000080")
    OldLace = colour("#FDF5E6")
    Olive = colour("#808000")
    OliveDrab = colour("#6B8E23")
    Orange = colour("#FFA500")
    OrangeRed = colour("#FF4500")
    Orchid = colour("#DA70D6")
    PaleGoldenRod = colour("#EEE8AA")
    PaleGreen = colour("#98FB98")
    PaleTurquoise = colour("#AFEEEE")
    PaleVioletRed = colour("#DB7093")
    PapayaWhip = colour("#FFEFD5")
    PeachPuff = colour("#FFDAB9")
    Peru = colour("#CD853F")
    Pink = colour("#FFC0CB")
    Plum = colour("#DDA0DD")
    PowderBlue = colour("#B0E0E6")
    Purple = colour("#800080")
    RebeccaPurple = colour("#663399")
    Red = colour("#FF0000")
    RosyBrown = colour("#BC8F8F")
    RoyalBlue = colour("#4169E1")
    SaddleBrown = colour("#8B4513")
    Salmon = colour("#FA8072")
    SandyBrown = colour("#F4A460")
    SeaGreen = colour("#2E8B57")
    SeaShell = colour("#FFF5EE")
    Sienna = colour("#A0522D")
    Silver = colour("#C0C0C0")
    SkyBlue = colour("#87CEEB")
    SlateBlue = colour("#6A5ACD")
    SlateGray = colour("#708090")
    Snow = colour("#FFFAFA")
    SpringGreen = colour("#00FF7F")
    SteelBlue = colour("#4682B4")
    Tan = colour("#D2B48C")
    Teal = colour("#008080")
    Thistle = colour("#D8BFD8")
    Tomato = colour("#FF6347")
    Turquoise = colour("#40E0D0")
    Violet = colour("#EE82EE")
    Wheat = colour("#F5DEB3")
    White = colour("#FFFFFF")
    WhiteSmoke = colour("#F5F5F5")
    Yellow = colour("#FFFF00")
    YellowGreen = colour("#9ACD32")
