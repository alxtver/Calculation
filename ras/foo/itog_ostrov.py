from ras.models import ComplektSKCal


def stoyki(kol_total_ostrov, list_post):
    base_polka_ostrov = list_post['base_polka_ostrov']
    kol_125_ostrov = int(list_post['kol_125_ostrov'])
    kol_100_ostrov = int(list_post['kol_100_ostrov'])
    kol_80_ostrov = int(list_post['kol_80_ostrov'])
    kol_65_ostrov = int(list_post['kol_65_ostrov'])
    height_stell_ostrov = list_post['height_stell_ostrov']
    dop_stoyka_ostrov = int(list_post['dop_stoyka_ostrov'])

    if base_polka_ostrov == '500':
        base_polka_125 = ComplektSKCal.objects.get(name='Полка 500 СК125')
        base_polka_100 = ComplektSKCal.objects.get(name='Полка 500 СК100')
        base_polka_80 = ComplektSKCal.objects.get(name='Полка 500 СК80')
        base_polka_65 = ComplektSKCal.objects.get(name='Полка 500 СК65')
    elif base_polka_ostrov == '400':
        base_polka_125 = ComplektSKCal.objects.get(name='Полка 400 СК125')
        base_polka_100 = ComplektSKCal.objects.get(name='Полка 400 СК100')
        base_polka_80 = ComplektSKCal.objects.get(name='Полка 400 СК80')
        base_polka_65 = ComplektSKCal.objects.get(name='Полка 400 СК65')
    else:
        base_polka_125 = ComplektSKCal.objects.get(name='Полка 600 СК125')
        base_polka_100 = ComplektSKCal.objects.get(name='Полка 600 СК100')
        base_polka_80 = ComplektSKCal.objects.get(name='Полка 600 СК80')
        base_polka_65 = ComplektSKCal.objects.get(name='Полка 600 СК65')


    base_polka_125_value = int(base_polka_125.number)
    base_polka_125.number = base_polka_125_value + kol_125_ostrov*2
    base_polka_100_value = int(base_polka_100.number)
    base_polka_100.number = base_polka_100_value + kol_100_ostrov*2
    base_polka_80_value = int(base_polka_80.number)
    base_polka_80.number = base_polka_80_value + kol_80_ostrov*2
    base_polka_65_value = int(base_polka_65.number)
    base_polka_65.number = base_polka_65_value + kol_65_ostrov*2


    base_polka_125.save()
    base_polka_100.save()
    base_polka_80.save()
    base_polka_65.save()

    if height_stell_ostrov == '2200':
        stoika = ComplektSKCal.objects.get(name='Стойка 2200 с опорой')
        value = int(stoika.number)
        stoika.number = value + kol_total_ostrov+ dop_stoyka_ostrov
    elif height_stell_ostrov == '1600':
        stoika = ComplektSKCal.objects.get(name='Стойка 1600 с опорой')
        value = int(stoika.number)
        stoika.number = value + kol_total_ostrov+ dop_stoyka_ostrov
    else:
        stoika = ComplektSKCal.objects.get(name='Стойка 2400 с опорой')
        value = int(stoika.number)
        stoika.number = value + kol_total_ostrov+ dop_stoyka_ostrov

    if base_polka_ostrov == '500':
        bokovina = ComplektSKCal.objects.get(name='Боковина 500 с опорой')
        value = int(bokovina.number)
        bokovina.number = value + kol_total_ostrov*2 + dop_stoyka_ostrov*2
    elif base_polka_ostrov == '400':
        bokovina = ComplektSKCal.objects.get(name='Боковина 400 с опорой')
        value = int(bokovina.number)
        bokovina.number = value + kol_total_ostrov*2 + dop_stoyka_ostrov*2
    else:
        bokovina = ComplektSKCal.objects.get(name='Боковина 600 с опорой')
        value = int(bokovina.number)
        bokovina.number = value + kol_total_ostrov*2 + dop_stoyka_ostrov*2

    stoika.save()
    bokovina.save()
    pass


def zad_panel(list_post):

    kol_125_ostrov = int(list_post['kol_125_ostrov'])
    kol_100_ostrov = int(list_post['kol_100_ostrov'])
    kol_80_ostrov = int(list_post['kol_80_ostrov'])
    kol_65_ostrov = int(list_post['kol_65_ostrov'])
    height_stell_ostrov = list_post['height_stell_ostrov']

    if height_stell_ostrov != '1600':
        kol_zad_panel_125 = kol_125_ostrov*4*2
        kol_zad_panel_100 = kol_100_ostrov*4*2
        kol_zad_panel_80 = kol_80_ostrov*4*2
        kol_zad_panel_65 = kol_65_ostrov*4*2
    else:
        kol_zad_panel_125 = kol_125_ostrov*3*2
        kol_zad_panel_100 = kol_100_ostrov*3*2
        kol_zad_panel_80 = kol_80_ostrov*3*2
        kol_zad_panel_65 = kol_65_ostrov*3*2


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


    zad_panel_125.save()
    zad_panel_100.save()
    zad_panel_80.save()
    zad_panel_65.save()
    pass


def paneli_friza(list_post):
    kol_125_ostrov = int(list_post['kol_125_ostrov'])
    kol_100_ostrov = int(list_post['kol_100_ostrov'])
    kol_80_ostrov = int(list_post['kol_80_ostrov'])
    kol_65_ostrov = int(list_post['kol_65_ostrov'])
    height_stell_ostrov = list_post['height_stell_ostrov']
    if height_stell_ostrov == '2200':
        kol_frize_125 = kol_125_ostrov*2*2
        kol_frize_100 = kol_100_ostrov*2*2
        kol_frize_80 = kol_80_ostrov*2*2
        kol_frize_65 = kol_65_ostrov*2*2
    elif height_stell_ostrov == '1600':
        kol_frize_125 = kol_125_ostrov*2
        kol_frize_100 = kol_100_ostrov*2
        kol_frize_80 = kol_80_ostrov*2
        kol_frize_65 = kol_65_ostrov*2
    else:
        kol_frize_125 = kol_125_ostrov*3*2
        kol_frize_100 = kol_100_ostrov*3*2
        kol_frize_80 = kol_80_ostrov*3*2
        kol_frize_65 = kol_65_ostrov*3*2

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

    panel_friza_125.save()
    panel_friza_100.save()
    panel_friza_80.save()
    panel_friza_65.save()

    pass


def kron(list_post):
    kol_125_ostrov = int(list_post['kol_125_ostrov'])
    kol_100_ostrov = int(list_post['kol_100_ostrov'])
    kol_80_ostrov = int(list_post['kol_80_ostrov'])
    kol_65_ostrov = int(list_post['kol_65_ostrov'])
    kol_125_30_ostrov = int(list_post['125_30_ostrov'])
    kol_100_30_ostrov = int(list_post['100_30_ostrov'])
    kol_80_30_ostrov = int(list_post['80_30_ostrov'])
    kol_65_30_ostrov = int(list_post['65_30_ostrov'])
    kol_125_40_ostrov = int(list_post['125_40_ostrov'])
    kol_100_40_ostrov = int(list_post['100_40_ostrov'])
    kol_80_40_ostrov = int(list_post['80_40_ostrov'])
    kol_65_40_ostrov = int(list_post['65_40_ostrov'])
    kol_125_50_ostrov = int(list_post['125_50_ostrov'])
    kol_100_50_ostrov = int(list_post['100_50_ostrov'])
    kol_80_50_ostrov = int(list_post['80_50_ostrov'])
    kol_65_50_ostrov = int(list_post['65_50_ostrov'])
    kol_125_60_ostrov = int(list_post['125_60_ostrov'])
    kol_100_60_ostrov = int(list_post['100_60_ostrov'])
    kol_80_60_ostrov = int(list_post['80_60_ostrov'])
    kol_65_60_ostrov = int(list_post['65_60_ostrov'])

    kol_kron_30 = (kol_125_ostrov * kol_125_30_ostrov +
                   kol_100_ostrov*kol_100_30_ostrov +
                   kol_80_ostrov*kol_80_30_ostrov +
                   kol_65_ostrov*kol_65_30_ostrov)*2

    kol_kron_40 = (kol_125_ostrov * kol_125_40_ostrov +
                   kol_100_ostrov*kol_100_40_ostrov +
                   kol_80_ostrov*kol_80_40_ostrov +
                   kol_65_ostrov*kol_65_40_ostrov) * 2

    kol_kron_50 = (kol_125_ostrov * kol_125_50_ostrov +
                   kol_100_ostrov*kol_100_50_ostrov +
                   kol_80_ostrov*kol_80_50_ostrov +
                   kol_65_ostrov*kol_65_50_ostrov) * 2

    kol_kron_60 = (kol_125_ostrov * kol_125_60_ostrov +
                   kol_100_ostrov*kol_100_60_ostrov +
                   kol_80_ostrov*kol_80_60_ostrov +
                   kol_65_ostrov*kol_65_60_ostrov)*2

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
    kol_125_ostrov = int(list_post['kol_125_ostrov'])
    kol_100_ostrov = int(list_post['kol_100_ostrov'])
    kol_80_ostrov = int(list_post['kol_80_ostrov'])
    kol_65_ostrov = int(list_post['kol_65_ostrov'])
    kol_125_30_ostrov = int(list_post['125_30_ostrov'])
    kol_100_30_ostrov = int(list_post['100_30_ostrov'])
    kol_80_30_ostrov = int(list_post['80_30_ostrov'])
    kol_65_30_ostrov = int(list_post['65_30_ostrov'])
    kol_125_40_ostrov = int(list_post['125_40_ostrov'])
    kol_100_40_ostrov = int(list_post['100_40_ostrov'])
    kol_80_40_ostrov = int(list_post['80_40_ostrov'])
    kol_65_40_ostrov = int(list_post['65_40_ostrov'])
    kol_125_50_ostrov = int(list_post['125_50_ostrov'])
    kol_100_50_ostrov = int(list_post['100_50_ostrov'])
    kol_80_50_ostrov = int(list_post['80_50_ostrov'])
    kol_65_50_ostrov = int(list_post['65_50_ostrov'])
    kol_125_60_ostrov = int(list_post['125_60_ostrov'])
    kol_100_60_ostrov = int(list_post['100_60_ostrov'])
    kol_80_60_ostrov = int(list_post['80_60_ostrov'])
    kol_65_60_ostrov = int(list_post['65_60_ostrov'])

    polka_125_30 = ComplektSKCal.objects.get(name='Полка 300 СК125')
    value = int(polka_125_30.number)
    polka_125_30.number = value + kol_125_30_ostrov*kol_125_ostrov
    polka_125_40 = ComplektSKCal.objects.get(name='Полка 400 СК125')
    value = int(polka_125_40.number)
    polka_125_40.number = value + kol_125_40_ostrov*kol_125_ostrov
    polka_125_50 = ComplektSKCal.objects.get(name='Полка 500 СК125')
    value = int(polka_125_50.number)
    polka_125_50.number = value + kol_125_50_ostrov*kol_125_ostrov
    polka_125_60 = ComplektSKCal.objects.get(name='Полка 600 СК125')
    value = int(polka_125_60.number)
    polka_125_60.number = value + kol_125_60_ostrov*kol_125_ostrov

    polka_100_30 = ComplektSKCal.objects.get(name='Полка 300 СК100')
    value = int(polka_100_30.number)
    polka_100_30.number = value + kol_100_30_ostrov*kol_100_ostrov
    polka_100_40 = ComplektSKCal.objects.get(name='Полка 400 СК100')
    value = int(polka_100_40.number)
    polka_100_40.number = value + kol_100_40_ostrov*kol_100_ostrov
    polka_100_50 = ComplektSKCal.objects.get(name='Полка 500 СК100')
    value = int(polka_100_50.number)
    polka_100_50.number = value + kol_100_50_ostrov*kol_100_ostrov
    polka_100_60 = ComplektSKCal.objects.get(name='Полка 600 СК100')
    value = int(polka_100_60.number)
    polka_100_60.number = value + kol_100_60_ostrov*kol_100_ostrov

    polka_80_30 = ComplektSKCal.objects.get(name='Полка 300 СК80')
    value = int(polka_80_30.number)
    polka_80_30.number = value + kol_80_30_ostrov*kol_80_ostrov
    polka_80_40 = ComplektSKCal.objects.get(name='Полка 400 СК80')
    value = int(polka_80_40.number)
    polka_80_40.number = value + kol_80_40_ostrov*kol_80_ostrov
    polka_80_50 = ComplektSKCal.objects.get(name='Полка 500 СК80')
    value = int(polka_80_50.number)
    polka_80_50.number = value + kol_80_50_ostrov*kol_80_ostrov
    polka_80_60 = ComplektSKCal.objects.get(name='Полка 600 СК80')
    value = int(polka_80_60.number)
    polka_80_60.number = value + kol_80_60_ostrov*kol_80_ostrov

    polka_65_30 = ComplektSKCal.objects.get(name='Полка 300 СК65')
    value = int(polka_65_30.number)
    polka_65_30.number = value + kol_65_30_ostrov*kol_65_ostrov
    polka_65_40 = ComplektSKCal.objects.get(name='Полка 400 СК65')
    value = int(polka_65_40.number)
    polka_65_40.number = value + kol_65_40_ostrov*kol_65_ostrov
    polka_65_50 = ComplektSKCal.objects.get(name='Полка 500 СК65')
    value = int(polka_65_50.number)
    polka_65_50.number = value + kol_65_50_ostrov*kol_65_ostrov
    polka_65_60 = ComplektSKCal.objects.get(name='Полка 600 СК65')
    value = int(polka_65_60.number)
    polka_65_60.number = value + kol_65_60_ostrov*kol_65_ostrov

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
    pass


def overall_ostrov(kol_total_ostrov, list_post):
    paneli_friza(list_post)
    kron(list_post)
    stoyki(kol_total_ostrov, list_post)
    zad_panel(list_post)
    polki(list_post)
    pass













