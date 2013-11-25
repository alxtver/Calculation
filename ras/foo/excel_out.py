import xlsxwriter, datetime
from ras.models import ComplektSKCal


def excel_out():
    date = datetime.datetime.now()
    name = date.strftime('./ras/static/xls/%H_%M_%S_%d_%m_%Y.xlsx')
    href = date.strftime('/static/xls/%H_%M_%S_%d_%m_%Y.xlsx')

    workbook = xlsxwriter.Workbook(name)
    worksheet = workbook.add_worksheet()

    bold = workbook.add_format({'bold': 1,
                                'font_size': 16})
    format = workbook.add_format({'border': 2,
                                   'bold': 1})
    format1 = workbook.add_format({'border': 1})
    format2 = workbook.add_format({'right': 2,
                                   'bottom': 1})
    worksheet.set_column('A:A', 5)
    worksheet.set_column('B:B', 30)
    worksheet.set_column('C:C', 13)
    i = 0
    worksheet.write(0, 1, 'Расчет стеллажей', bold)
    worksheet.write(2, 1, 'Наименование', format)
    worksheet.write(2, 2, 'Колличество', format)
    worksheet.write(2, 3, 'Цена', format)
    worksheet.write(2, 4, 'Сумма', format)
    worksheet.write(2, 5, 'Вес', format)
    row = 3
    col = 1
    values = ComplektSKCal.objects.all()
    for value in values:
        worksheet.write(row, col, value.name, format)
        worksheet.write(row, col + 1, value.number, format1)
        worksheet.write(row, col + 2, value.price, format1)
        worksheet.write(row, col + 3, value.summ, format1)
        worksheet.write(row, col + 4, value.weight, format2)
        i += 1
        row += 1
    strrow = str(row)
    formsumm ='=SUM(E4:E' + strrow + ')'
    formweight ='=SUM(F4:F' + strrow + ')'
# Write a total using a formula.
    worksheet.write(row, 1, 'Итого', format)
    worksheet.write(row, 2, '', format)
    worksheet.write(row, 3, '', format)
    worksheet.write(row, 4, formsumm, format)
    worksheet.write(row, 5, formweight, format)
    workbook.close()
    return href