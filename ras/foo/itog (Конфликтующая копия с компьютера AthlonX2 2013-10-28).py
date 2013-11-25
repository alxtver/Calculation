from ras.foo.SK2200 import *
from ras.models import ComplektSK, ComplektSKCalc

def createbase(self):
    count = ComplektSK.objects.all().count()
    count1 = ComplektSKCalc.objects.all().count()
    if count == count1:
        order = ComplektSKCalc.objects.all().order_by('id')
        self.maches = list(order)
        return self.maches
    else:
        ComplektSKCalc.objects.all().delete()
        i = 1
        while i <= count:
            b = ComplektSK.objects.get(id=i)
            c = ComplektSKCalc(name=b.name, number= 0, price=b.price, weight=b.weight)
            c.save()
            i += 1
            order = ComplektSKCalc.objects.all().order_by('id')
            self.maches = list(order)
    return self.maches

def deletenull():
    ComplektSKCalc.objects.filter(number=0).delete()
    return

def itog_125(kol_125):
    kol_stoika_2200 = kol_125
    kol_bokovina_60 = kol_125
    kol_zad_panel_125 = kol_125*4
    kol_panel_friza_125 = kol_125*2
    stoika_2200 = ComplektSKCalc.objects.get(name='Стойка 2200 с опорой')
    stoika_2200.number = kol_stoika_2200
    stoika_2200.save()
    bokovina_50 = ComplektSKCalc.objects.get(name='Боковина 500 с опорой')
    bokovina_50.number = kol_bokovina_60
    bokovina_50.save()
    zad_panel_125 = ComplektSKCalc.objects.get(name='Панель задняя СК125')
    zad_panel_125.number = kol_zad_panel_125
    zad_panel_125.save()
    panel_friza_125 = ComplektSKCalc.objects.get(name='Панель фриза СК125')
    panel_friza_125.number = kol_panel_friza_125
    panel_friza_125.save()


