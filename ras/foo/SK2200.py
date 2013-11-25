from ras.models import ComplektSK




def stoika_2200_40():
    bokovina_40 = ComplektSK.objects.get(name='Боковина 400 с опорой')
    stoika_2200 = ComplektSK.objects.get(name='Стойка 2200 с опорой')
    return stoika_2200, bokovina_40


def stoika_2200_50():
    bokovina_50 = ComplektSK.objects.get(name='Боковина 500 с опорой')
    stoika_2200 = ComplektSK.objects.get(name='Стойка 2200 с опорой')
    return stoika_2200, bokovina_50


def stoika_2200_60():
    bokovina_60 = ComplektSK.objects.get(name='Боковина 600 с опорой')
    stoika_2200 = ComplektSK.objects.get(name='Стойка 2200 с опорой')
    return stoika_2200, bokovina_60


def sk_125_50(kol_125):
    stoika_2200 = ComplektSK.objects.get(name='Стойка 2200 с опорой')
    bokovina_50 = ComplektSK.objects.get(name='Боковина 500 с опорой')
    zad_panel_125 = ComplektSK.objects.get(name='Панель задняя СК125')
    kol_stoika_2200 = int(kol_125)
    kol_bokovina_50 = int(kol_125)
    kol_zad_panel_125 = int(kol_125)*4
    return   stoika_2200, bokovina_50, zad_panel_125, kol_stoika_2200,\
             kol_bokovina_50,  kol_zad_panel_125

def sk_125_60(kol_125):
    stoika_2200 = ComplektSK.objects.get(name='Стойка 2200 с опорой')
    bokovina_60 = ComplektSK.objects.get(name='Боковина 600 с опорой')
    zad_panel_125 = ComplektSK.objects.get(name='Панель задняя СК125')
    kol_stoika_2200 = int(kol_125)
    kol_bokovina_60 = int(kol_125)
    kol_zad_panel_125 = int(kol_125)*4
    return   stoika_2200, bokovina_60, zad_panel_125, kol_stoika_2200,\
             kol_bokovina_60,  kol_zad_panel_125