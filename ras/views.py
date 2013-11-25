from django.shortcuts import render_to_response, render
from ras.models import ComplektSK, ComplektSKCal
from datetime import datetime
from ras.foo.excel_out import excel_out
from ras.forms import ContactForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from ras.foo.itog import overall, createbase, deletenull
from ras.foo.itog_ostrov import overall_ostrov

from django.db import transaction



def current_datetime(request):
    now = datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})


def hours_remaning(request):
    current_date = datetime.now()
    year = current_date.year
    month = current_date.month
    day = current_date.day
    b = datetime(year, month, day, 17, 30, 00)
    if current_date < b:
        c = b - current_date
        current_hours = int(c.seconds/60/60)
        current_minutes = int(c.seconds/60) - current_hours*60
        return render_to_response('current_datetime.html',  locals())
    else:
        return render_to_response('go_home.html',  locals())


def catalog(request):
    order = ComplektSK.objects.all().order_by('id')
    maches = list(order)
    return render_to_response('alldb.html', {'maches': maches})


def catalogcalc(self):
    createbase(self)
    return render_to_response('calcdb.html', {'maches': self.maches})


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Введите поисковый запрос!')
        elif len(q) > 20:
            errors.append('Введите не более 20 символов!')
        else:
            names = ComplektSK.objects.filter(name__icontains=q)
            matches = list(names)
            return render_to_response('search_results.html', {'matches': matches, 'query': q})
    return render_to_response('search.html', {'errors': errors})


def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST, auto_id='form_%s') # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
          cd = form.cleaned_data
          send_mail(
                cd['Имя'],
                cd['Сообщение'],
                cd.get('email', 'noreply@example.com'), ['iteowner@example.com'],
                    )
          return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm(auto_id='form_%s') # An unbound form
    return render(request, 'contactform.html', {'form': form})


@transaction.commit_manually
def base(request):
    errors = []
    if request.method == 'POST':

        list_post = request.POST.copy()
        nacenka = int(request.POST['nacenka'])
        discont = int(request.POST['discont'])

        height_stell_ostrov = request.POST['height_stell_ostrov']
        base_polka_ostrov = request.POST['base_polka_ostrov']
        dop_stoyka_ostrov = int(request.POST['dop_stoyka_ostrov'])
        #Колличество пристенных стеллажей
        kol_total = int(request.POST['kol_125']) +\
                    int(request.POST['kol_100']) +\
                    int(request.POST['kol_80']) +\
                    int(request.POST['kol_65']) +\
                    int(request.POST['kol_sku'])+\
                    int(request.POST['kol_skun'])
        #Колличество островных стеллажей
        kol_total_ostrov = int(request.POST['kol_125_ostrov']) +\
                    int(request.POST['kol_100_ostrov']) +\
                    int(request.POST['kol_80_ostrov']) +\
                    int(request.POST['kol_65_ostrov'])

        count = ComplektSK.objects.all().count()
        ComplektSKCal.objects.all().delete()
        #Расчет стоимости с учетом скидки и наценки
        i = 1
        while i <= count:
                 b = ComplektSK.objects.get(id=i)
                 price_i = round(b.price+(b.price/100*nacenka)-(b.price/100*discont), 2)
                 c = ComplektSKCal(name=b.name, number=0, summ=0, price=price_i,  weight=b.weight)
                 c.save()
                 i += 1

        overall(kol_total, list_post)

        overall_ostrov(kol_total_ostrov, list_post)
        #Расчет сумм цены и веса
        i = 1
        itog_price = 0
        itog_weight = 0
        while i <= count:
                 b = ComplektSKCal.objects.get(id=i)
                 b.summ = b.number*b.price
                 weight = ComplektSKCal.objects.get(id=i).weight
                 number = ComplektSKCal.objects.get(id=i).number
                 i_weight = weight*number
                 b.weight = i_weight
                 itog_weight += i_weight
                 itog_price += b.summ
                 b.save()
                 i += 1
        deletenull()
        href = excel_out()
        order = ComplektSKCal.objects.all().order_by('name')
        x = list(order)
        transaction.commit()
        return render_to_response('itogform.html', locals())
    else:
        return render_to_response('baseform.html', {'errors': errors})

