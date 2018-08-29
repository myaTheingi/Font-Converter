# -*- coding: utf-8 -*-
import re


def replace(input):
    # replace each zawgyi code point with equivalent code point in unicode
    output = input

    output = output.replace(u'\u106a', u'\u1009')  # nya_lay
    output = re.sub(u'\u106b', u'\u100a', output)  # nya
    output = re.sub(u'\u1090', u'\u101b', output)  # yaguat
    output = re.sub(u'\u1033', u'\u102f', output)  # ta_chuang_ngin
    output = re.sub(u'\u1034', u'\u1030', output)  # na_chuang_ngin
    output = re.sub(u'[\u103d\u1087]', u'\u103e', output)  # hahtoe
    output = re.sub(u'\u103c', u'\u103d', output)  # waswe
    output = re.sub(u'\u1086', u'\u103f', output)  # thagyi
    output = re.sub(u'[\u103b\u107e\u107f\u1080\u1081\u1082\u1083\u1084]', u'\u103c', output)  # yayit
    output = re.sub(u'[\u103a\u107d]', u'\u103b', output)  # yapint
    output = re.sub(u'\u1039', u'\u103a', output)  # nga_that
    output = re.sub(u'\u104e', u'\u104e\u1044\u1004\u103a\u1038', output)  # la_guang
    output = re.sub(u'[\u1037\u1094\u1095]', u'\u1037', output)  # aut_myit
    output = re.sub(u'\u108f', u'\u1014', output)  # na_nge

    return output


def decompose(input):
    # decomposed combined characters to sequenced characters
    output = input

    ## nga_sint
    output = re.sub(u'([\u1000-\u1021])\u1064', u'\u1064\\1', output)
    output = re.sub(u'([\u1000-\u1021])\u108b', u'\u1064\\1\u102d', output) #ngasint_with_Lonegyitin
    output = re.sub(u'([\u1000-\u1021])\u108c', u'\u1064\\1\u102e', output) #ngasint_with_Lonegyitinsankhat
    output = re.sub(u'([\u1000-\u1021])\u108d', u'\u1064\\1\u1036', output) #ngasint_with_thaythaytin
    output = re.sub(u'([\u1000-\u1021])\u108e', u'\u102d\\1\u1036', output) #lonegyitin_with_thaythaytin

    output = re.sub(u'\u1088', u'\u103e\u102f', output)  # ha_toe and ta_chuang_ngin
    output = re.sub(u'\u1089', u'\u103e\u1030', output)  # ha_toe and na_chuang_ngin
    output = re.sub(u'\u105a', u'\u102b\u103a', output)  # yaycha_shayhtoe
    output = re.sub(u'\u108a', u'\u103d\u103e', output)  # waswe_hatoe

    # 2lone_sint
    output = re.sub(u'\u1060', u'\u1039\u1000', output)  # kagyi
    output = re.sub(u'\u1061', u'\u1039\u1001', output)  # kakway
    output = re.sub(u'\u1062', u'\u1039\u1002', output)  # gange
    output = re.sub(u'\u1063', u'\u1039\u1003', output)  # gagyi
    output = re.sub(u'\u1065', u'\u1039\u1005', output)  # salone
    output = re.sub(u'[\u1066\u1067]', u'\u1039\u1006', output)  # salane
    output = re.sub(u'\u1068', u'\u1039\u1007', output)  # zagwe
    output = re.sub(u'\u1069', u'\u1039\u1008', output)  # zamyinzwe
    output = re.sub(u'\u106c', u'\u1039\u100b', output)  # tatalin_gyake
    output = re.sub(u'\u106d', u'\u1039\u100c', output)  # thawen_bae
    output = re.sub(u'\u106e', u'\u100d\u1039\u100d', output)  # da_yin_guat
    output = re.sub(u'\u106f', u'\u100d\u1039\u100e', output)  # da_yin_mot
    output = re.sub(u'\u1070', u'\u1039\u100f', output)  # na_gyi
    output = re.sub(u'[\u1071\u1072]', u'\u1039\u1010', output)  # tawenpu
    output = re.sub(u'[\u1073\u1074]', u'\u1039\u1011', output)  # htasinhtoo
    output = re.sub(u'\u1075', u'\u1039\u1012', output)  # dadway
    output = re.sub(u'\u1076', u'\u1039\u1013', output)  # daauat_chint
    output = re.sub(u'\u1077', u'\u1039\u1014', output)  # ngange
    output = re.sub(u'\u1078', u'\u1039\u1015', output)  # pasaut
    output = re.sub(u'\u1079', u'\u1039\u1016', output)  # phaoat_htop
    output = re.sub(u'\u107a', u'\u1039\u1017', output)  # bahtat_chint
    output = re.sub(u'[\u107b\u1093]', u'\u1039\u1018', output)  # ba_gone
    output = re.sub(u'\u107c', u'\u1039\u1019', output)  # ma
    output = re.sub(u'\u1085', u'\u1039\u101c', output)  # la
    output = re.sub(u'\u1091', u'\u100f\u1039\u100d', output)  # ng_with_dyg
    output = re.sub(u'\u1092', u'\u100b\u1039\u100c', output)  # ttlg_with_twb
    output = re.sub(u'\u1097', u'\u100b\u1039\u100b', output)  # ttlg_with_ttlg

    return output


def visual2logical(input):
    # reorder the sequence of characters from visual to logical
    output = input

    output = re.sub(u'((?:\u1031)?)((?:\u103C)?)([\u1000-\u1021])((?:\u103B)?)((?:\u103D)?)((?:\u103E)?)((?:\u1037)?)'
                    u'((?:\u102C)?)', '\\3\\2\\4\\5\\6\\1\\7\\8', output)
    # 1=thawayhto, 2=waswe, 3=letters, 4=yayit, 5=hahto, 6=patsint, 7=autmyit, 8=yaychar

    output = re.sub(u'(\u102f)([\u102d\u102e])', '\\2\\1', output) #tachaung_lonegyitin/sanke
    output = re.sub(u'(\u1030)([\u102d\u102e])', '\\2\\1', output) #nachaung_lonegyitin/sanke

    output = re.sub(u'\u1064', u'\u1004\u103a\u1039', output) #ngathat

    return output


def convert(input):
    output = input

    output = replace(output)
    output = decompose(output)
    output = visual2logical(output)


    return output
