from enum import Enum, unique

class _Color:
    def __init__(self, col):
        r = (col >> 16) & 0xff
        g = (col >>  8) & 0xff
        b = (col >>  0) & 0xff

        self.bgr = (b, g, r)

class Color(_Color):
    def _hexFromString(self, string): 
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

    def _colorFromList(self, lst):
        for i in lst:
            if not isinstance(i, int):
                raise TypeError(f"{i} must be of type int")
        return tuple(lst[::-1])

    def __init__(self, r, g=None, b=None):
        if g == None and b == None:
            if isinstance(r, int):
                red   = (r >> 16) & 0xff
                green = (r >>  8) & 0xff
                blue  = (r >>  0) & 0xff

                self.bgr = (blue, green, red)
            elif isinstance(r, (list, tuple)):
                if len(r) != 3:
                    raise ValueError("Colors should consist of only 3 values.")
                self.bgr = self._colorFromList(r)

            elif isinstance(r, str):
                if r[0] != "#" or (len(r) != 7 and len(r) != 4):
                    raise ValueError("Colors should be in the form '#rrggbb' or '#rgb'\nIf in the form '#rgb' it will automaticallty repeat the r, g, b values.\neg: #345 => #334455")
                if len(r) == 4:
                    red = self._hexFromString(r[1]*2)
                    green = self._hexFromString(r[2]*2)
                    blue = self._hexFromString(r[3]*2)
                else:
                    red = self._hexFromString(r[1:3])
                    green = self._hexFromString(r[3:5])
                    blue = self._hexFromString(r[5:7])
                    
                self.bgr = (blue, green, red)
            else:
                raise TypeError("Unknwon Type " + str(type(r)))

        elif g == None or b == None:
            raise ValueError("This function only accepts either one or three arguments")

        else:
            self.bgr = self._colorFromList([r, g, b])

    AliceBlue = _Color(0xF0F8FF)
    AntiqueWhite = _Color(0xFAEBD7)
    Aquamarine = _Color(0x7FFFD4)
    Azure = _Color(0xF0FFFF)
    Beige = _Color(0xF5F5DC)
    Bisque = _Color(0xFFE4C4)
    Black = _Color(0x000000)
    BlanchedAlmond = _Color(0xFFEBCD)
    Blue = _Color(0x0000FF)
    BlueViolet = _Color(0x8A2BE2)
    Brown = _Color(0xA52A2A)
    BurlyWood = _Color(0xDEB887)
    CadetBlue = _Color(0x5F9EA0)
    Chartreuse = _Color(0x7FFF00)
    Chocolate = _Color(0xD2691E)
    Coral = _Color(0xFF7F50)
    CornflowerBlue = _Color(0x6495ED)
    Cornsilk = _Color(0xFFF8DC)
    Crimson = _Color(0xDC143C)
    Cyan = _Color(0x00FFFF)
    DarkBlue = _Color(0x00008B)
    DarkCyan = _Color(0x008B8B)
    DarkGoldenRod = _Color(0xB8860B)
    DarkGray = _Color(0xA9A9A9)
    DarkGreen = _Color(0x006400)
    DarkKhaki = _Color(0xBDB76B)
    DarkMagenta = _Color(0x8B008B)
    DarkOliveGreen = _Color(0x556B2F)
    DarkOrange = _Color(0xFF8C00)
    DarkOrchid = _Color(0x9932CC)
    DarkRed = _Color(0x8B0000)
    DarkSalmon = _Color(0xE9967A)
    DarkSeaGreen = _Color(0x8FBC8F)
    DarkSlateBlue = _Color(0x483D8B)
    DarkSlateGray = _Color(0x2F4F4F)
    DarkTurquoise = _Color(0x00CED1)
    DarkViolet = _Color(0x9400D3)
    DeepPink = _Color(0xFF1493)
    DeepSkyBlue = _Color(0x00BFFF)
    DimGray = _Color(0x696969)
    DodgerBlue = _Color(0x1E90FF)
    FireBrick = _Color(0xB22222)
    FloralWhite = _Color(0xFFFAF0)
    ForestGreen = _Color(0x228B22)
    Fuchsia = _Color(0xFF00FF)
    Gainsboro = _Color(0xDCDCDC)
    GhostWhite = _Color(0xF8F8FF)
    Gold = _Color(0xFFD700)
    GoldenRod = _Color(0xDAA520)
    Gray = _Color(0x808080)
    Green = _Color(0x008000)
    GreenYellow = _Color(0xADFF2F)
    HoneyDew = _Color(0xF0FFF0)
    HotPink = _Color(0xFF69B4)
    IndianRed = _Color(0xCD5C5C)
    Indigo = _Color(0x4B0082)
    Ivory = _Color(0xFFFFF0)
    Khaki = _Color(0xF0E68C)
    Lavender = _Color(0xE6E6FA)
    LavenderBlush = _Color(0xFFF0F5)
    LawnGreen = _Color(0x7CFC00)
    LemonChiffon = _Color(0xFFFACD)
    LightBlue = _Color(0xADD8E6)
    LightCoral = _Color(0xF08080)
    LightCyan = _Color(0xE0FFFF)
    LightGoldenRodYellow = _Color(0xFAFAD2)
    LightGray = _Color(0xD3D3D3)
    LightGreen = _Color(0x90EE90)
    LightPink = _Color(0xFFB6C1)
    LightSalmon = _Color(0xFFA07A)
    LightSeaGreen = _Color(0x20B2AA)
    LightSkyBlue = _Color(0x87CEFA)
    LightSlateGray = _Color(0x778899)
    LightSteelBlue = _Color(0xB0C4DE)
    LightYellow = _Color(0xFFFFE0)
    Lime = _Color(0x00FF00)
    LimeGreen = _Color(0x32CD32)
    Linen = _Color(0xFAF0E6)
    Maroon = _Color(0x800000)
    MediumAquaMarine = _Color(0x66CDAA)
    MediumBlue = _Color(0x0000CD)
    MediumOrchid = _Color(0xBA55D3)
    MediumPurple = _Color(0x9370DB)
    MediumSeaGreen = _Color(0x3CB371)
    MediumSlateBlue = _Color(0x7B68EE)
    MediumSpringGreen = _Color(0x00FA9A)
    MediumTurquoise = _Color(0x48D1CC)
    MediumVioletRed = _Color(0xC71585)
    MidnightBlue = _Color(0x191970)
    MintCream = _Color(0xF5FFFA)
    MistyRose = _Color(0xFFE4E1)
    Moccasin = _Color(0xFFE4B5)
    NavajoWhite = _Color(0xFFDEAD)
    Navy = _Color(0x000080)
    OldLace = _Color(0xFDF5E6)
    Olive = _Color(0x808000)
    OliveDrab = _Color(0x6B8E23)
    Orange = _Color(0xFFA500)
    OrangeRed = _Color(0xFF4500)
    Orchid = _Color(0xDA70D6)
    PaleGoldenRod = _Color(0xEEE8AA)
    PaleGreen = _Color(0x98FB98)
    PaleTurquoise = _Color(0xAFEEEE)
    PaleVioletRed = _Color(0xDB7093)
    PapayaWhip = _Color(0xFFEFD5)
    PeachPuff = _Color(0xFFDAB9)
    Peru = _Color(0xCD853F)
    Pink = _Color(0xFFC0CB)
    Plum = _Color(0xDDA0DD)
    PowderBlue = _Color(0xB0E0E6)
    Purple = _Color(0x800080)
    RebeccaPurple = _Color(0x663399)
    Red = _Color(0xFF0000)
    RosyBrown = _Color(0xBC8F8F)
    RoyalBlue = _Color(0x4169E1)
    SaddleBrown = _Color(0x8B4513)
    Salmon = _Color(0xFA8072)
    SandyBrown = _Color(0xF4A460)
    SeaGreen = _Color(0x2E8B57)
    SeaShell = _Color(0xFFF5EE)
    Sienna = _Color(0xA0522D)
    Silver = _Color(0xC0C0C0)
    SkyBlue = _Color(0x87CEEB)
    SlateBlue = _Color(0x6A5ACD)
    SlateGray = _Color(0x708090)
    Snow = _Color(0xFFFAFA)
    SpringGreen = _Color(0x00FF7F)
    SteelBlue = _Color(0x4682B4)
    Tan = _Color(0xD2B48C)
    Teal = _Color(0x008080)
    Thistle = _Color(0xD8BFD8)
    Tomato = _Color(0xFF6347)
    Turquoise = _Color(0x40E0D0)
    Violet = _Color(0xEE82EE)
    Wheat = _Color(0xF5DEB3)
    White = _Color(0xFFFFFF)
    WhiteSmoke = _Color(0xF5F5F5)
    Yellow = _Color(0xFFFF00)
    YellowGreen = _Color(0x9ACD32)
