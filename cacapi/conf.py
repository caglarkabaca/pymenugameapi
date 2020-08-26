"""
Tıklanma algılama mekanizmaları falan burada olucak

Burası arka planda çalışıcak
"""


def possibleCoordinates(x, y, s_x, s_y):

    p_x = [x for x in range(x - s_x, x + s_x + 1)]
    p_y = [y for y in range(y - s_y, y + s_y + 1)]

    p_list = []

    for x in p_x:

        for y in p_y:

            p_list.append((x, y))


    return p_list

def get_plist(obj):

    x, y = int(obj.center[0]), int(obj.center[1])
    s_x, s_y = int(obj.size[0] / 2), int(obj.size[1] / 2)

    p_list = possibleCoordinates(x, y, s_x, s_y)

    return p_list
