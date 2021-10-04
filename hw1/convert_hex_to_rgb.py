import typing


def convert_hex_to_RGB(hex_codes: typing.List[str]) -> typing.List[typing.Tuple[int, int, int]]:
    """
    Converts a list of hex color codes to RGB tuples
    :param hex_codes: a list of hex color codes
    :type hex_codes: List[str]
    :return: list of rgb tuples
    :rtype: List[Tuple[int, int, int]]
    """
    # argument validation
    for code in hex_codes:
        assert isinstance(code, str)
        assert code.startswith("#")
        assert len(code) == 7

    rgb_codes = []
    for code in hex_codes:
        r_hex, g_hex, b_hex = code[1:3], code[3:5], code[5:]
        r, g, b = int(r_hex, 16), int(g_hex, 16), int(b_hex, 16)
        rgb_codes.append((r,g,b))

    return rgb_codes


if __name__ == '__main__':
    hex_codes = ["#000000", "#FFFFFF","#FF0000", "#00FF00","#0000FF"]
    print(convert_hex_to_RGB(hex_codes))