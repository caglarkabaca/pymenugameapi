"""
conf.py

Bazı matematik işlemlerini yapıcağım kod dosyası
başka bir işlevi yok

"""


"""
possibleCoordinates
desc : butona tıklama sırasında olabilecek kordinatları hesaplar

param :
    x => butonun x konumu
    y => butonun y konumu
    s_x => butonun genişliği
    s_y => butonun yüksekliği

return : olabilecek tüm kordinatları LIST şeklinde döndür

"""
def possibleCoordinates(x, y, s_x, s_y):

    p_x = [x for x in range(x - s_x, x + s_x + 1)]
    p_y = [y for y in range(y - s_y, y + s_y + 1)]

    p_list = []

    for x in p_x:

        for y in p_y:

            p_list.append((x, y))


    return p_list


"""
get_plist
desc : asıl possiblecoordinates bu burası front kısmı

param :
    obj => herhangi bir obje tıklanılacak olan

return : olabilecek tüm kordinatları LIST şeklinde döndür

"""
def get_plist(obj):

    x, y = int(obj.center[0]), int(obj.center[1])
    s_x, s_y = int(obj.size[0] / 2), int(obj.size[1] / 2)

    p_list = possibleCoordinates(x, y, s_x, s_y)

    return p_list
