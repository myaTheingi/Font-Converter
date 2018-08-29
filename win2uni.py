
# -*- coding: utf-8 -*-

import re


def replace(input):

    output = input

    output = output.replace(u'\u0075', u'\u1000')  # kagyi
    output = output.replace(u'\u0063', u'\u1001')  # khakway
    output = output.replace(u'\u002A', u'\u1002')  # gange
    output = output.replace(u'\u0043', u'\u1003')  # gagyi
    output = output.replace(u'\u0069', u'\u1004')  # nga
    output = output.replace(u'\u0070', u'\u1005')  # salone
    output = output.replace(u'\u0071', u'\u1006')  # salane
    output = output.replace(u'\u005A', u'\u1007')  # zakwe
    output = re.sub(u'\u1005\u103b', u'\u1008', output)  # zamyitzwe
    output = output.replace(u'\u00DA', u'\u1009')  # nyalay
    output = re.sub(u'[\u006E\u00F1]', u'\u100A', output)  # nya
    output = output.replace(u'\u0023', u'\u100B')  # tatalingyake
    output = output.replace(u'\u0058', u'\u100C')  # htawinbal
    output = output.replace(u'\u0021', u'\u100D')  # dayinkauk
    output = output.replace(u'\u00A1', u'\u100E')  # dayinmoke
    output = output.replace(u'\u0050', u'\u100F')  # nagyi
    output = output.replace(u'\u0077', u'\u1010')  # tawinpu
    output = output.replace(u'\u0078', u'\u1011')  # htasinhtoo
    output = output.replace(u'\u0027', u'\u1012')  # dadway
    output = output.replace(u'\u0022', u'\u1013')  # daautchint
    output = re.sub(u'[\u0045\u0065]', u'\u1014', output)  # nange
    output = output.replace(u'\u0079', u'\u1015')  # pasaut
    output = output.replace(u'\u007A', u'\u1016')  # phaoohtok
    output = output.replace(u'\u0041', u'\u1017')  # bahtetchint
    output = output.replace(u'\u0062', u'\u1018')  # bakone
    output = output.replace(u'\u0072', u'\u1019')  # ma
    output = output.replace(u'\u002C', u'\u101A')  # yapatlat
    output = re.sub(u'[\u0026\u00BD]', u'\u101B', output)  # yakaut
    output = output.replace(u'\u0076', u'\u101C')  # la
    output = output.replace(u'\u0030', u'\u101D')  # wa
    output = output.replace(u'\u006F', u'\u101E')  # tha
    output = output.replace(u'\u005B', u'\u101F')  # ha
    output = output.replace(u'\u0056', u'\u1020')  # lagyi
    output = output.replace(u'\u0074', u'\u1021')  # ak

    output = re.sub(u'\u00A3', u'\u1023', output)  # ei(kagyi)
    output = re.sub(u'\u00FE', u'\u1024', output)  # ee
    output = re.sub(u'[\u004F\u00CD]', u'\u1025', output)  # ou
    output = re.sub(u'\u007B', u'\u1027', output)  # a
    output = re.sub(u'\u0067', u'\u102B', output)  # yaychar
    output = re.sub(u'\u006D', u'\u102C', output)  # yaychar
    output = re.sub(u'\u0064', u'\u102D', output)  # lonegyitin
    output = re.sub(u'\u0044', u'\u102E', output)  # lonegyitinsankhat
    output = re.sub(u'\u1025\u102e', u'\u1026', output)  # oo with longyitinsanke
    output = re.sub(u'[\u004B\u006B]', u'\u102F', output)  # tachaung
    output = re.sub(u'[\u004C\u006C]', u'\u1030', output)  # 2chaung
    output = re.sub(u'\u0061', u'\u1031', output)  # thawayhto
    output = re.sub(u'\u004A', u'\u1032', output)  # nathtomyit
    output = re.sub(u'\u0048', u'\u1036', output)  # thaythaytin
    output = re.sub(u'[\u0055\u0059\u0068]', u'\u1037', output)  # autmyit
    output = re.sub(u'\u003B', u'\u1038', output)  # witsapaut
    output = re.sub(u'\u0066', u'\u103A', output)  # athet
    output = re.sub(u'[\u0073\u00DF]', u'\u103B', output)  # yapint
    output = re.sub(u'[\u0042\u004D\u004E\u0060\u006A\u007E]', u'\u103C', output)  # yayit
    output = re.sub(u'\u0047', u'\u103D', output)  # waswe
    output = re.sub(u'[\u0053\u00A7]', u'\u103E', output)  # hahto
    output = re.sub(u'\u00F3', u'\u103F', output)  # thagyi
    output = re.sub(u'\u0031', u'\u1041', output)  # 1
    output = re.sub(u'\u0032', u'\u1042', output)  # 2
    output = re.sub(u'\u0033', u'\u1043', output)  # 3
    output = re.sub(u'\u0034', u'\u1044', output)  # 4
    output = re.sub(u'\u0035', u'\u1045', output)  # 5
    output = re.sub(u'\u0036', u'\u1046', output)  # 6
    output = re.sub(u'\u0037', u'\u1047', output)  # 7
    output = re.sub(u'\u0038', u'\u1048', output)  # 8
    output = re.sub(u'\u0039', u'\u1049', output)  # 9
    output = output.replace(u'\u003F', u'\u104A')  # pokekalay
    output = output.replace(u'\u002F', u'\u104B')  # pokema
    output = output.replace(u'\u00FC', u'\u104C')  # hnigh
    output = output.replace(u'\u00ED', u'\u104D')  # ywat
    output = output.replace(u'\u00A4', u'\u104E')  # lagaung
    output = output.replace(u'\u005c', u'\u104f')  # ei

    return output


def decompose(input):

    output = input

    output = re.sub(u'\u003a', u'\u102b\u103a', output)  # yaychar_shayhtoe
    output = output.replace(u'\u0024', u'\u1000\u103b\u1015\u103A')  # kyat
    output = re.sub(u'[\u003c\u003e]', u'\u103c\u103d', output)  # yayit_waswe
    output = re.sub(u'\u0040', u'\u100f\u1039\u100d', output)  # nagyi_sint_tawenbae
    output = re.sub(u'\u0049', u'\u103e\u102f', output)  # hatoe_1chaungngin
    output = re.sub(u'\u0051', u'\u103b\u103e', output)  # yapint_hatoe
    output = re.sub(u'\u0052', u'\u103b\u103d', output)  # yapint_waswe
    output = re.sub(u'\u0054', u'\u103d\u103e', output)  # waswe_hatoe
    output = re.sub(u'\u0057', u'\u103b\u103d\u103e', output)  # yapint_waswe_hatoe
    output = output.replace(u'\u007c', u'\u100b\u1039\u100c')  # ttlg_with_twb
    output = re.sub(u'\u00aa', u'\u103e\u1030', output)  # hatoe_2chaungngin

    # 2lone_sint
    output = re.sub(u'\u00a2', u'\u1039\u1003', output)  # gagyi
    output = re.sub(u'\u00a5', u'\u100b\u1039\u100b', output)  # twice_ttlg
    output = re.sub(u'\u00a6', u'\u1039\u1011', output)  # htasinhtoo
    output = re.sub(u'\u00a8', u'\u1039\u1013', output)  # daautchai
    output = re.sub(u'\u00a9', u'\u1039\u1001', output)  # kakwe
    output = re.sub(u'[\u00ac\u00c7]', u'\u1039\u1018', output)  # bagone
    output = re.sub(u'\u00ae', u'\u1039\u1019', output)  # ma
    output = re.sub(u'\u00b2', u'\u1039\u100c', output)  # thawenbae
    output = re.sub(u'\u00b3', u'\u1039\u100b', output)  # tatalingyake
    output = re.sub(u'\u00b4', u'\u1039\u1012', output)  # dadway
    output = re.sub(u'\u00b9', u'\u100d\u1039\u100e', output)  # dayinmout_with_dayingaut
    output = re.sub(u'\u00be', u'\u1039\u1002', output)  # gange
    output = re.sub(u'\u00c1', u'\u1039\u1017', output)  # balatchai
    output = re.sub(u'[\u00c5\u00e5]', u'\u1039\u1010', output)  # dawenbu
    output = re.sub(u'\u00c6', u'\u1039\u1007', output)  # zagwe
    output = re.sub(u'\u00c9', u'\u1039\u1010\u103d', output)  # twa
    output = re.sub(u'\u00d1', u'\u1039\u1008', output)  # zamyinzwe
    output = re.sub(u'\u00d3', u'\u1009\u102c', output)  # nya_with_yaychar
    output = re.sub(u'\u00d6', u'\u1039\u100f', output)  # nagyi
    output = re.sub(u'\u00d7', u'\u100d\u1039\u100d', output)  # twice_dyg
    output = re.sub(u'\u00dc', u'\u1039\u1015', output)  # pasaut
    output = re.sub(u'\u00e4', u'\u1039\u1006', output)  # salane
    output = re.sub(u'\u00e6', u'\u1039\u1016', output)  # phaoohtoke
    output = re.sub(u'\u00e9', u'\u1039\u1014', output)  # nange
    output = re.sub(u'\u00f6', u'\u1039\u1005', output)  # salone
    output = re.sub(u'\u00fa', u'\u1039\u1000', output)  # kagyi
    output = re.sub(u'\u2019', u'\u1039\u101c', output)  # la

    # nga_sint
    output = re.sub(u'([\u1000-\u1021])\u0046', u'\u0046\\1', output)  # normal
    output = re.sub(u'([\u1000-\u1021])\u00d0', u'\u0046\\1\u102e', output)  # with_longyitin_sanke
    output = re.sub(u'([\u1000-\u1021])\u00d8', u'\u0046\\1\u102d', output)  # with_longyitin
    output = re.sub(u'([\u1000-\u1021])\u00f8', u'\u0046\\1\u1036', output)  # with_taytaytin
    output = re.sub(u'\u0046', u'\u1004\u103a\u1039', output)
    output = re.sub(u'\u00f0', u'\u102d\u1036', output)

    return output


def visual2logical(input):
    # reorder the sequence of characters from visual to logical
    output = input
    ## 1=tawaetoe 2=yayit 3=letter 4=yapint 5=waswe 6=hatoe 7=aumyit 8=yaychar
    output = re.sub(u'((?:\u1031)?)((?:\u103c)?)([\u1000-\u1021])((?:\u103b)?)((?:\u103d)?)((?:\u103e)?)((?:\u1037)?)((?:\u102c)?)', '\\3\\2\\4\\5\\6\\1\\7\\8', output)
    output = re.sub(u'\u00fb([\u1000-\u1021])', u"\\1\u103c\u102f", output)  # yayit_1chaung
    output = re.sub(u'\u00ea([\u1000-\u1021])', u'\\1\u103c\u102f', output)  # yayit_1chaung

    return output


def convert(input):

    output = replace(input)
    output = decompose(output)
    output = visual2logical(output)

    return output
