from ras.foo.SK2200 import stoika_2200_50
from ras.models import ComplektSK


def sk_125_50():
    stoika_2200_50()
    zad_panel_125 = ComplektSK.objects.get(name='Панель задняя СК125')
    return locals()