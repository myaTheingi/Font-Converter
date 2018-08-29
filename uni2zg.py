# -*- coding: utf-8 -*-


import re


def replace(input):
    output = input

    output = re.sub(u'\u103a', u'\u1039', output)  # ngathat
    output = re.sub(u'\u103b', u'\u103a', output)  # yapint
    output = re.sub(u'\u103c', u'\u103b', output)  # yayit
    output = re.sub(u'\u103d', u'\u103c', output)  # waswe
    output = re.sub(u'\u103e', u'\u103d', output)  # hahtoe
    output = re.sub(u'\u103f', u'\u1086', output)  # thagyi

    return output


def precompose(input):
    output = input

    # nga_sint
    output = re.sub(u'\u1004\u103a\u1039', u'\u1064', output)
    output = re.sub(u'(\u1064)([\u1000-\u1021])', '\\2\\1', output)
    output = re.sub(u'([\u1000-\u1021])\u1064\u102d', u'\\1\u108b', output)
    output = re.sub(u'([\u1000-\u1021])\u1064\u102e', u'\\1\u108c', output)
    output = re.sub(u'([\u1000-\u1021])\u1064\u1036', u'\\1\u108d', output)
    output = re.sub(u'\u102d\u1036', u'\u108e', output)  # lonegyitin_sanke

    # 2lone_sint
    output = re.sub(u'\u1039\u1000', u'\u1060', output)  # kagyi
    output = re.sub(u'\u1039\u1001', u'\u1061', output)  # khakway
    output = re.sub(u'\u1039\u1002', u'\u1062', output)  # gange
    output = re.sub(u'\u1039\u1003', u'\u1063', output)  # gagyi
    output = re.sub(u'\u1039\u1005', u'\u1065', output)  # salone
    output = re.sub(u'\u1039\u1006', u'\u1066', output)  # salane
    output = re.sub(u'\u1039\u1007', u'\u1068', output)  # sagwe
    output = re.sub(u'\u1039\u1008', u'\u1069', output)  # samyinzwe
    output = re.sub(u'\u1039\u100b', u'\u106c', output)  # tatalin_gyake
    output = re.sub(u'\u1039\u100c', u'\u106d', output)  # htawenbae
    output = re.sub(u'\u100d\u1039\u100d', u'\u106e', output)  # dayinguat
    output = re.sub(u'\u100d\u1039\u100e', u'\u106f', output)  # dayinmot
    output = re.sub(u'\u1039\u100f', u'\u1070', output)  # nagyi
    output = re.sub(u'\u1039\u1010', u'\u1071', output)  # tawenbu
    output = re.sub(u'\u1039\u1011', u'\u1073', output)  # htasinhtoo
    output = re.sub(u'\u1039\u1012', u'\u1075', output)  # dadway
    output = re.sub(u'\u1039\u1013', u'\u1076', output)  # daautchai
    output = re.sub(u'\u1039\u1014', u'\u1077', output)  # ngange
    output = re.sub(u'\u1039\u1015', u'\u1078', output)  # pasaut
    output = re.sub(u'\u1039\u1016', u'\u1079', output)  # paothtop
    output = re.sub(u'\u1039\u1017', u'\u107a', output)  # bahtat_chai
    output = re.sub(u'\u1039\u1018', u'\u107b', output)  # bagone
    output = re.sub(u'\u1039\u1019', u'\u107c', output)  # ma
    output = re.sub(u'\u1039\u101c', u'\u1085', output)  # la
    output = re.sub(u'\u100f\u1039\u100d', u'\u1091', output)  # nagyi_dayingaut
    output = re.sub(u'\u100b\u106d', u'\u1092', output)  # tatalingyake_htawenbae
    output = re.sub(u'\u100b\u1039\u100b', u'\u1097', output)  # tatalingyake_2lone
    output = re.sub(u'\u102b\u103a', u'\u105a', output)  # yaycha_shayhtoe
    output = re.sub(u'\u103d\u103e', u'\u108a', output)  # waswe_hatoe

    return output


def logical2visual(input):
    output = input

    output = re.sub(
        u'([\u1000-\u1021])((?:[\u1060-\u1090])?)((?:\u103b)?)((?:\u103a)?)((?:\u103c)?)((?:\u103d)?)((?:\u108a)?)((?:\u1031)?)((?:\u1039)?)((?:\u1037)?)((:\u102c)?)',
        '\\8\\3\\1\\4\\5\\6\\2\\7\\9\\10\\11', output)
    # 1=letters 2=pr_sint 3=yayit 4=yapint 5=waswe 6=hatoe 7=waswe_hatoe 8=tawaetoe 9=nga_tat 10=aumyit 11=yaychar

    output = re.sub(u'\u1038\u1039', u'\u1039\u1038', output) #ngathat_wasapaut

    return output


def shape(input):
    output = input

    output = re.sub(u'\u103b([\u1000\u1003\u1006\u100f\u1010\u1011\u1018\u101a\u101c\u101e\u101f\u1021])', u'\u107e\\1',
                    output)  # yayit_agyi
    output = re.sub(u'\u103b([\u1000-\u1021])([\u102d\u102e\u1036])', u'\u107f\\1\\2',
                    output)  # yayit with longgyidin/sanke
    output = re.sub(u'\u107e([\u1000-\u1021])([\u102d\u102e\u1036])', u'\u1080\\1\\2',
                    output)  # yayit_agi with longgyidin/sanke
    output = re.sub(u'\u103b([\u1000-\u1021])(\u103c)', u'\u1081\\1\\2', output)  # yayit with waswe
    output = re.sub(u'\u107e([\u1000-\u1021])(\u103c)', u'\u1082\\1\\2', output)  # yayit_agyi with waswe
    output = re.sub(u'\u103b([\u1000-\u1021])([\u1060-\u1093])', u'\u1081\\1\\2', output)  # yayit with pr_sint
    output = re.sub(u'\u107e([\u1000-\u1021])([\u1060-\u1093])', u'\u1082\\1\\2', output)  # yayit_agyi with pr_sint
    output = re.sub(u'\u107f([\u1000-\u1021])([\u102d\u102e\u1036])(\u103c)', u'\u1083\\1\\2\\3', output)  # yayit apyat
    output = re.sub(u'\u1080([\u1000-\u1021])([\u102d\u102e\u1036])(\u103c)', u'\u1084\\1\\2\\3',
                    output)  # yayit_agi apyat

    output = re.sub(u'([\u1008\u100b\u100c\u100d\u1020])\u102f', u'\\1\u1033', output)  # 1chaung_agyi
    output = re.sub(u'([\u1008\u100b\u100c\u100d\u1020])\u1030', u'\\1\u1034', output)  # 2chaung_agyi
    output = re.sub(u'([\u103b\u107e\u107f\u1080])([\u1000-\u1021])((?:[\u102d\u102e\u1036])?)\u102f',
                    u'\\1\\2\\3\u1033', output)  # yayit_with_1chaung
    output = re.sub(u'([\u103b\u107e\u107f\u1080])([\u1000-\u1021])((?:[\u102d\u102e\u1036])?)\u1030',
                    u'\\1\\2\\3\u1034', output)  # yayit_with_2chaung
    output = re.sub(u'(\u103a)((?:[\u102d\u102e])?)\u102f', u'\\1\\2\u1033', output)  # yapint_wiht_1chaung
    output = re.sub(u'(\u103a)((?:[\u102d\u102e])?)\u1030', u'\\1\\2\u1034', output)  # yapint_with_2chaung
    output = re.sub(u'([\u1060-\u1063])((?:[\u102d\u102e])?)\u102f', u'\\1\\2\u1033',
                    output)  # 1cn with prsint from kagyi to gagyi
    output = re.sub(u'([\u1065-\u1069])((?:[\u102d\u102e])?)\u102f', u'\\1\\2\u1033',
                    output)  # 1cn with prsint before salone to samyintswe
    output = re.sub(u'([\u106c-\u107c])((?:[\u102d\u102e])?)\u102f', u'\\1\\2\u1033',
                    output)  # 1cn with prsint from ttlg to ma
    output = re.sub(u'([\u1085\u1093])((?:[\u102d\u102e])?)\u102f', u'\\1\\2\u1033',
                    output)  # 1cn with prsint from la to bagone
    output = re.sub(u'([\u1060-\u1063])((?:[\u102d\u102e])?)\u1030', u'\\1\\2\u1034',
                    output)  # 2cn with prsint from kagyi to gagyi
    output = re.sub(u'([\u1065-\u1069])((?:[\u102d\u102e])?)\u1030', u'\\1\\2\u1034',
                    output)  # 2cn with prsint from salone to samyintswe
    output = re.sub(u'([\u106c-\u107c])((?:[\u102d\u102e])?)\u1030', u'\\1\\2\u1034',
                    output)  # 2cn with prsint from ttlg to ma
    output = re.sub(u'([\u1085\u1093])((?:[\u102d\u102e])?)\u1030', u'\\1\\2\u1034',
                    output)  # 2cn with prsint before la and bagone

    output = re.sub(u'\u100a\u103d', u'\u100a\u1087', output)  # nya with hatoe

    output = re.sub(u'\u1009(\u1039)', u'\u1025\\1', output)  # nyapyat_to_oo

    output = re.sub(u'\u103a([\u103c\u103d])', u'\u107d\\1', output)  # yapintapyat_with_waswehatoe


    # nange_apyat
    output = re.sub(u'\u1014([\u103d\u103c])', u'\u108f\\1', output)
    output = re.sub(u'\u1014([\u1060-\u1063])', u'\u108f\\1', output)
    output = re.sub(u'\u1014([\u1065-\u1069])', u'\u108f\\1', output)
    output = re.sub(u'\u1014([\u106c-\u107c])', u'\u108f\\1', output)
    output = re.sub(u'\u1014([\u1085\u1093])', u'\u108f\\1', output)

    # aut_myit
    output = re.sub(u'([\u1014\u102f\u1030])((?:[\u1032\u1036])?)\u1037', u'\\1\\2\u1094', output)
    output = re.sub(u'([\u103c\u103d\u108a\u1033\u1034\u1088\u1089])((?:[\u1032\u1036])?)\u1037', u'\\1\\2\u1095',
                    output)

    output = re.sub(u'\u101b([\u102f\u1030])', u'\u1090\\1', output)  # ygapyat_with_1/2 chaung

    output = re.sub(u'\u100a(\u108a)', u'\u106b\\1', output)  # nyapyat_with_waswehatoe

    return output


def convert(input):
    output = input

    output = precompose(output)
    output = replace(output)
    output = logical2visual(output)
    output = shape(output)


    return output
