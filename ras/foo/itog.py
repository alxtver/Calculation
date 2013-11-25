from ras.models import ComplektSK, ComplektSKCal

def createbase(self):
    count = ComplektSK.objects.all().count()
    count1 = ComplektSKCal.objects.all().count()
    if count == count1:
        order = ComplektSKCal.objects.all().order_by('id')
        self.maches = list(order)
        return self.maches
    else:
        ComplektSKCal.objects.all().delete()
        i = 1
        while i <= count:
            b = ComplektSK.objects.get(id=i)
            c = ComplektSKCal(name=b.name, number= 0, price=b.price, weight=b.weight)
            c.save()
            i += 1
            order = ComplektSKCal.objects.all().order_by('id')
            self.maches = list(order)
    return self.maches

def deletenull():
    ComplektSKCal.objects.filter(number=0).delete()
    return


def stoyki(list_post, kol_total):
    base_polka = list_post['base_polka']
    kol_125 = int(list_post['kol_125'])
    kol_100 = int(list_post['kol_100'])
    kol_80 = int(list_post['kol_80'])
    kol_65 = int(list_post['kol_65'])
    kol_sku = int(list_post['kol_sku'])
    kol_skun = int(list_post['kol_skun'])
    height_stell = list_post['height_stell']
    dop_stoyka = int(list_post['dop_stoyka'])
    if base_polka == '500':
        base_polka_125 = ComplektSKCal.objects.get(name='Полка 500 СК125')
        base_polka_100 = ComplektSKCal.objects.get(name='Полка 500 СК100')
        base_polka_80 = ComplektSKCal.objects.get(name='Полка 500 СК80')
        base_polka_65 = ComplektSKCal.objects.get(name='Полка 500 СК65')
        base_polka_sku = ComplektSKCal.objects.get(name='Полка 500 СКУ')
        base_polka_skun = ComplektSKCal.objects.get(name='Полка 500 СКУН')
    elif base_polka == '400':
        base_polka_125 = ComplektSKCal.objects.get(name='Полка 400 СК125')
        base_polka_100 = ComplektSKCal.objects.get(name='Полка 400 СК100')
        base_polka_80 = ComplektSKCal.objects.get(name='Полка 400 СК80')
        base_polka_65 = ComplektSKCal.objects.get(name='Полка 400 СК65')
        base_polka_sku = ComplektSKCal.objects.get(name='Полка 400 СКУ')
        base_polka_skun = ComplektSKCal.objects.get(name='Полка 400 СКУН')
    else:
        base_polka_125 = ComplektSKCal.objects.get(name='Полка 600 СК125')
        base_polka_100 = ComplektSKCal.objects.get(name='Полка 600 СК100')
        base_polka_80 = ComplektSKCal.objects.get(name='Полка 600 СК80')
        base_polka_65 = ComplektSKCal.objects.get(name='Полка 600 СК65')
        base_polka_sku = ComplektSKCal.objects.get(name='Полка 600 СКУ')
        base_polka_skun = ComplektSKCal.objects.get(name='Полка 600 СКУН')

    base_polka_125_value = int(base_polka_125.number)
    base_polka_125.number = base_polka_125_value + kol_125
    base_polka_100_value = int(base_polka_100.number)
    base_polka_100.number = base_polka_100_value + kol_100
    base_polka_80_value = int(base_polka_80.number)
    base_polka_80.number = base_polka_80_value + kol_80
    base_polka_65_value = int(base_polka_65.number)
    base_polka_65.number = base_polka_65_value + kol_65
    base_polka_sku_value = int(base_polka_sku.number)
    base_polka_sku.number = base_polka_sku_value + kol_sku
    base_polka_skun_value = int(base_polka_skun.number)
    base_polka_skun.number = base_polka_skun_value + kol_skun

    base_polka_125.save()
    base_polka_100.save()
    base_polka_80.save()
    base_polka_65.save()
    base_polka_sku.save()
    base_polka_skun.save()

    if height_stell == '2200':
        stoika = ComplektSKCal.objects.get(name='Стойка 2200 с опорой')
        value = int(stoika.number)
        stoika.number = value + kol_total+ dop_stoyka
    elif height_stell == '1600':
        stoika = ComplektSKCal.objects.get(name='Стойка 1600 с опорой')
        value = int(stoika.number)
        stoika.number = value + kol_total+ dop_stoyka
    else:
        stoika = ComplektSKCal.objects.get(name='Стойка 2400 с опорой')
        value = int(stoika.number)
        stoika.number = value + kol_total+ dop_stoyka

    if base_polka == '500':
        bokovina = ComplektSKCal.objects.get(name='Боковина 500 с опорой')
        value = int(bokovina.number)
        bokovina.number = value + kol_total+ dop_stoyka
    elif base_polka == '400':
        bokovina = ComplektSKCal.objects.get(name='Боковина 400 с опорой')
        value = int(bokovina.number)
        bokovina.number = value + kol_total + dop_stoyka
    else:
        bokovina = ComplektSKCal.objects.get(name='Боковина 600 с опорой')
        value = int(bokovina.number)
        bokovina.number = value + kol_total + dop_stoyka

    stoika.save()
    bokovina.save()
    pass


def zad_panel(list_post):

    kol_125 = int(list_post['kol_125'])
    kol_100 = int(list_post['kol_100'])
    kol_80 = int(list_post['kol_80'])
    kol_65 = int(list_post['kol_65'])
    kol_sku = int(list_post['kol_sku'])
    kol_skun = int(list_post['kol_skun'])
    height_stell = list_post['height_stell']

    if height_stell != '1600':
        kol_zad_panel_125 = kol_125*4
        kol_zad_panel_100 = kol_100*4
        kol_zad_panel_80 = kol_80*4
        kol_zad_panel_65 = kol_65*4
        kol_zad_panel_sku = kol_sku*4
        kol_zad_panel_skun = kol_skun*4
    else:
        kol_zad_panel_125 = kol_125*3
        kol_zad_panel_100 = kol_100*3
        kol_zad_panel_80 = kol_80*3
        kol_zad_panel_65 = kol_65*3
        kol_zad_panel_sku = kol_sku*3
        kol_zad_panel_skun = kol_skun*3


    zad_panel_125 = ComplektSKCal.objects.get(name='Панель задняя СК125')
    value = int(zad_panel_125.number)
    zad_panel_125.number = value + kol_zad_panel_125

    zad_panel_100 = ComplektSKCal.objects.get(name='Панель задняя СК100')
    value = int(zad_panel_100.number)
    zad_panel_100.number = value + kol_zad_panel_100

    zad_panel_80 = ComplektSKCal.objects.get(name='Панель задняя СК80')
    value = int(zad_panel_80.number)
    zad_panel_80.number = value + kol_zad_panel_80

    zad_panel_65 = ComplektSKCal.objects.get(name='Панель задняя СК65')
    value = int(zad_panel_65.number)
    zad_panel_65.number = value + kol_zad_panel_65

    zad_panel_sku = ComplektSKCal.objects.get(name='Панель задняя СКУ')
    value = int(zad_panel_sku.number)
    zad_panel_sku.number = value + kol_zad_panel_sku

    zad_panel_skun = ComplektSKCal.objects.get(name='Панель задняя СКУН')
    value = int(zad_panel_skun.number)
    zad_panel_skun.number = value + kol_zad_panel_skun

    zad_panel_125.save()
    zad_panel_100.save()
    zad_panel_80.save()
    zad_panel_65.save()
    zad_panel_sku.save()
    zad_panel_skun.save()
    pass


def paneli_friza(list_post):

    kol_125 = int(list_post['kol_125'])
    kol_100 = int(list_post['kol_100'])
    kol_80 = int(list_post['kol_80'])
    kol_65 = int(list_post['kol_65'])
    kol_sku = int(list_post['kol_sku'])
    kol_skun = int(list_post['kol_skun'])
    height_stell = list_post['height_stell']

    if height_stell == '2200':
        kol_frize_125 = kol_125*2
        kol_frize_100 = kol_100*2
        kol_frize_80 = kol_80*2
        kol_frize_65 = kol_65*2
        kol_frize_sku_n = kol_sku
        kol_frize_sku_v = kol_sku
        kol_frize_skun_n = kol_skun
        kol_frize_skun_v = kol_skun
    elif height_stell == '1600':
        kol_frize_125 = kol_125
        kol_frize_100 = kol_100
        kol_frize_80 = kol_80
        kol_frize_65 = kol_65
        kol_frize_sku_n = kol_sku
        kol_frize_sku_v = 0
        kol_frize_skun_n = kol_skun
        kol_frize_skun_v = 0
    else:
        kol_frize_125 = kol_125*3
        kol_frize_100 = kol_100*3
        kol_frize_80 = kol_80*3
        kol_frize_65 = kol_65*3
        kol_frize_sku_n = kol_sku
        kol_frize_sku_v = kol_sku*2
        kol_frize_skun_n = kol_skun
        kol_frize_skun_v = kol_skun*2

    panel_friza_125 = ComplektSKCal.objects.get(name='Панель фриза СК125')
    value = int(panel_friza_125.number)
    panel_friza_125.number = value + (kol_frize_125)

    panel_friza_100 = ComplektSKCal.objects.get(name='Панель фриза СК100')
    value = int(panel_friza_100.number)
    panel_friza_100.number = value + (kol_frize_100)

    panel_friza_80 = ComplektSKCal.objects.get(name='Панель фриза СК80')
    value = int(panel_friza_80.number)
    panel_friza_80.number = value + (kol_frize_80)

    panel_friza_65 = ComplektSKCal.objects.get(name='Панель фриза СК65')
    value = int(panel_friza_65.number)
    panel_friza_65.number = value + (kol_frize_65)

    panel_friza_sku_n = ComplektSKCal.objects.get(name='Панель нижняя СКУ боковина 500')
    panel_friza_sku_v = ComplektSKCal.objects.get(name='Панель задняя верхняя СКУ')
    value = int(panel_friza_sku_n.number)
    value1 = int(panel_friza_sku_v.number)
    panel_friza_sku_n.number = value + (kol_frize_sku_n)
    panel_friza_sku_v.number = value1 + (kol_frize_sku_v)

    panel_friza_skun_n = ComplektSKCal.objects.get(name='Панель нижняя СКУН (боковина 500)')
    panel_friza_skun_v = ComplektSKCal.objects.get(name='Панель задняя верхняя СКУН')
    value = int(panel_friza_skun_n.number)
    value1 = int(panel_friza_skun_v.number)
    panel_friza_skun_n.number = value + (kol_frize_skun_n)
    panel_friza_skun_v.number = value1 + (kol_frize_skun_v)

    panel_friza_125.save()
    panel_friza_100.save()
    panel_friza_80.save()
    panel_friza_65.save()
    panel_friza_sku_n.save()
    panel_friza_sku_v.save()
    panel_friza_skun_n.save()
    panel_friza_skun_v.save()
    pass


def kron(list_post):
    kol_125 = int(list_post['kol_125'])
    kol_100 = int(list_post['kol_100'])
    kol_80 = int(list_post['kol_80'])
    kol_65 = int(list_post['kol_65'])
    kol_sku = int(list_post['kol_sku'])
    kol_skun = int(list_post['kol_skun'])
    kol_125_30 = int(list_post['125_30'])
    kol_100_30 = int(list_post['100_30'])
    kol_80_30 = int(list_post['80_30'])
    kol_65_30 = int(list_post['65_30'])
    kol_sku_30 = int(list_post['sku_30'])
    kol_skun_30 = int(list_post['skun_30'])
    kol_125_40 = int(list_post['125_40'])
    kol_100_40 = int(list_post['100_40'])
    kol_80_40 = int(list_post['80_40'])
    kol_65_40 = int(list_post['65_40'])
    kol_sku_40 = int(list_post['sku_40'])
    kol_skun_40 = int(list_post['skun_40'])
    kol_125_50 = int(list_post['125_50'])
    kol_100_50 = int(list_post['100_50'])
    kol_80_50 = int(list_post['80_50'])
    kol_65_50 = int(list_post['65_50'])
    kol_sku_50 = int(list_post['sku_50'])
    kol_skun_50 = int(list_post['skun_50'])
    kol_125_60 = int(list_post['125_60'])
    kol_100_60 = int(list_post['100_60'])
    kol_80_60 = int(list_post['80_60'])
    kol_65_60 = int(list_post['65_60'])
    kol_sku_60 = int(list_post['sku_60'])
    kol_skun_60 = int(list_post['skun_60'])

    kol_kron_30 = (kol_125 * kol_125_30 + kol_100*kol_100_30 +\
                  kol_80*kol_80_30 +  kol_65*kol_65_30 +\
                  kol_sku*kol_sku_30 + kol_skun*kol_skun_30)*2

    kol_kron_40 = (kol_125 * kol_125_40 + kol_100*kol_100_40 +\
                  kol_80*kol_80_40 + kol_65*kol_65_40 +\
                  kol_sku*kol_sku_40 + kol_skun*kol_skun_40)*2

    kol_kron_50 = (kol_125 * kol_125_50 + kol_100*kol_100_50 +\
                  kol_80*kol_80_50 + kol_65*kol_65_50 +\
                  kol_sku*kol_sku_50 + kol_skun*kol_skun_50)*2

    kol_kron_60 = (kol_125 * kol_125_60 + kol_100*kol_100_60 +\
                  kol_80*kol_80_60 + kol_65*kol_65_60 +\
                  kol_sku*kol_sku_60 + kol_skun*kol_skun_60)*2

    kron_30 = ComplektSKCal.objects.get(name='Кронштейн 300')
    value_30 = int(kron_30.number)
    kron_30.number = value_30 + kol_kron_30

    kron_40 = ComplektSKCal.objects.get(name='Кронштейн 400')
    value_40 = int(kron_40.number)
    kron_40.number = value_40 + kol_kron_40

    kron_50 = ComplektSKCal.objects.get(name='Кронштейн 500')
    value_50 = int(kron_50.number)
    kron_50.number = value_50 + kol_kron_50

    kron_60 = ComplektSKCal.objects.get(name='Кронштейн 600')
    value_60 = int(kron_60.number)
    kron_60.number = value_60 + kol_kron_60

    kron_30.save()
    kron_40.save()
    kron_50.save()
    kron_60.save()
    pass


def polki(list_post):
    kol_125 = int(list_post['kol_125'])
    kol_100 = int(list_post['kol_100'])
    kol_80 = int(list_post['kol_80'])
    kol_65 = int(list_post['kol_65'])
    kol_sku = int(list_post['kol_sku'])
    kol_skun = int(list_post['kol_skun'])
    kol_125_30 = int(list_post['125_30'])
    kol_100_30 = int(list_post['100_30'])
    kol_80_30 = int(list_post['80_30'])
    kol_65_30 = int(list_post['65_30'])
    kol_sku_30 = int(list_post['sku_30'])
    kol_skun_30 = int(list_post['skun_30'])
    kol_125_40 = int(list_post['125_40'])
    kol_100_40 = int(list_post['100_40'])
    kol_80_40 = int(list_post['80_40'])
    kol_65_40 = int(list_post['65_40'])
    kol_sku_40 = int(list_post['sku_40'])
    kol_skun_40 = int(list_post['skun_40'])
    kol_125_50 = int(list_post['125_50'])
    kol_100_50 = int(list_post['100_50'])
    kol_80_50 = int(list_post['80_50'])
    kol_65_50 = int(list_post['65_50'])
    kol_sku_50 = int(list_post['sku_50'])
    kol_skun_50 = int(list_post['skun_50'])
    kol_125_60 = int(list_post['125_60'])
    kol_100_60 = int(list_post['100_60'])
    kol_80_60 = int(list_post['80_60'])
    kol_65_60 = int(list_post['65_60'])
    kol_sku_60 = int(list_post['sku_60'])
    kol_skun_60 = int(list_post['skun_60'])

    polka_125_30 = ComplektSKCal.objects.get(name='Полка 300 СК125')
    value = int(polka_125_30.number)
    polka_125_30.number = value + kol_125_30*kol_125
    polka_125_40 = ComplektSKCal.objects.get(name='Полка 400 СК125')
    value = int(polka_125_40.number)
    polka_125_40.number = value + kol_125_40*kol_125
    polka_125_50 = ComplektSKCal.objects.get(name='Полка 500 СК125')
    value = int(polka_125_50.number)
    polka_125_50.number = value + kol_125_50*kol_125
    polka_125_60 = ComplektSKCal.objects.get(name='Полка 600 СК125')
    value = int(polka_125_60.number)
    polka_125_60.number = value + kol_125_60*kol_125

    polka_100_30 = ComplektSKCal.objects.get(name='Полка 300 СК100')
    value = int(polka_100_30.number)
    polka_100_30.number = value + kol_100_30*kol_100
    polka_100_40 = ComplektSKCal.objects.get(name='Полка 400 СК100')
    value = int(polka_100_40.number)
    polka_100_40.number = value + kol_100_40*kol_100
    polka_100_50 = ComplektSKCal.objects.get(name='Полка 500 СК100')
    value = int(polka_100_50.number)
    polka_100_50.number = value + kol_100_50*kol_100
    polka_100_60 = ComplektSKCal.objects.get(name='Полка 600 СК100')
    value = int(polka_100_60.number)
    polka_100_60.number = value + kol_100_60*kol_100

    polka_80_30 = ComplektSKCal.objects.get(name='Полка 300 СК80')
    value = int(polka_80_30.number)
    polka_80_30.number = value + kol_80_30*kol_80
    polka_80_40 = ComplektSKCal.objects.get(name='Полка 400 СК80')
    value = int(polka_80_40.number)
    polka_80_40.number = value + kol_80_40*kol_80
    polka_80_50 = ComplektSKCal.objects.get(name='Полка 500 СК80')
    value = int(polka_80_50.number)
    polka_80_50.number = value + kol_80_50*kol_80
    polka_80_60 = ComplektSKCal.objects.get(name='Полка 600 СК80')
    value = int(polka_80_60.number)
    polka_80_60.number = value + kol_80_60*kol_80

    polka_65_30 = ComplektSKCal.objects.get(name='Полка 300 СК65')
    value = int(polka_65_30.number)
    polka_65_30.number = value + kol_65_30*kol_65
    polka_65_40 = ComplektSKCal.objects.get(name='Полка 400 СК65')
    value = int(polka_65_40.number)
    polka_65_40.number = value + kol_65_40*kol_65
    polka_65_50 = ComplektSKCal.objects.get(name='Полка 500 СК65')
    value = int(polka_65_50.number)
    polka_65_50.number = value + kol_65_50*kol_65
    polka_65_60 = ComplektSKCal.objects.get(name='Полка 600 СК65')
    value = int(polka_65_60.number)
    polka_65_60.number = value + kol_65_60*kol_65

    polka_sku_30 = ComplektSKCal.objects.get(name='Полка 300 СКУ')
    value = int(polka_sku_30.number)
    polka_sku_30.number = value + kol_sku_30*kol_sku
    polka_sku_40 = ComplektSKCal.objects.get(name='Полка 400 СКУ')
    value = int(polka_sku_40.number)
    polka_sku_40.number = value + kol_sku_40*kol_sku
    polka_sku_50 = ComplektSKCal.objects.get(name='Полка 500 СКУ')
    value = int(polka_sku_50.number)
    polka_sku_50.number = value + kol_sku_50*kol_sku
    polka_sku_60 = ComplektSKCal.objects.get(name='Полка 600 СКУ')
    value = int(polka_sku_60.number)
    polka_sku_60.number = value + kol_sku_60*kol_sku

    polka_skun_30 = ComplektSKCal.objects.get(name='Полка 300 СКУН')
    value = int(polka_skun_30.number)
    polka_skun_30.number = value + kol_skun_30*kol_skun
    polka_skun_40 = ComplektSKCal.objects.get(name='Полка 400 СКУН')
    value = int(polka_skun_40.number)
    polka_skun_40.number = value + kol_skun_40*kol_skun
    polka_skun_50 = ComplektSKCal.objects.get(name='Полка 500 СКУН')
    value = int(polka_skun_50.number)
    polka_skun_50.number = value + kol_skun_50*kol_skun
    polka_skun_60 = ComplektSKCal.objects.get(name='Полка 600 СКУН')
    value = int(polka_skun_60.number)
    polka_skun_60.number = value + kol_skun_60*kol_skun

    polka_125_30.save()
    polka_125_40.save()
    polka_125_50.save()
    polka_125_60.save()
    polka_100_30.save()
    polka_100_40.save()
    polka_100_50.save()
    polka_100_60.save()
    polka_80_30.save()
    polka_80_40.save()
    polka_80_50.save()
    polka_80_60.save()
    polka_65_30.save()
    polka_65_40.save()
    polka_65_50.save()
    polka_65_60.save()
    polka_sku_30.save()
    polka_sku_40.save()
    polka_sku_50.save()
    polka_sku_60.save()
    polka_skun_30.save()
    polka_skun_40.save()
    polka_skun_50.save()
    polka_skun_60.save()
    pass


def overall(kol_total,list_post):
    paneli_friza(list_post)
    kron(list_post)
    stoyki(list_post, kol_total)
    zad_panel(list_post)
    polki(list_post)
    pass












