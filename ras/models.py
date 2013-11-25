from django.db import models


class CalcManager(models.Manager): # Наш менеджер, который нам дает возможность менять поведение модели
    def get_query_set(self):
        result=super(CalcManager, self).get_query_set().extra(select={'summ': "price*number"})
        return result

class ComplektSK(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=128,
                            blank=False, null = False,
                            verbose_name = 'Наименование')
    price = models.FloatField(blank = False, null = False, verbose_name = 'Цена')
    weight = models.FloatField( blank = True, verbose_name = 'Вес')

    def __str__(self):
        return '%s %s %s' % (self.name, self.price, self.weight, )


class ComplektSKCalc(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=128,
                            blank=False, null = False,
                            verbose_name = 'Наименование')
    number = models.IntegerField(blank= False, null=False, verbose_name='Количество')
    price = models.FloatField(blank = False, null = False, verbose_name = 'Цена')
    summ = CalcManager()
    weight = models.FloatField( blank = True, verbose_name = 'Вес')

    def __str__(self):
        return '%s %s %s %s' % (self.name, self.number, self.price, self.weight, )


class ComplektSKCal(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=128,
                            blank=False, null = False,
                            verbose_name = 'Наименование')
    number = models.IntegerField(blank= False, null=False, verbose_name='Количество')
    price = models.FloatField(blank = False, null = False, verbose_name = 'Цена')
    summ = models.FloatField( blank = True, verbose_name = 'Сумма')
    weight = models.FloatField( blank = True, verbose_name = 'Вес')

    def __str__(self):
        return '%s %s %s %s %s' % (self.name, self.number, self.summ, self.price, self.weight, )