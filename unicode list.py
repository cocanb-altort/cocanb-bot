import xlsxwriter

workbook = xlsxwriter.Workbook('unicode_python3.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write_string (0, 0, 'U+')

num = 0
for column in range(1,17):
    units = hex(num)[2:]
    worksheet.write(0, column, units.upper())
    num = num + 1

num = 0
for row in range (1,69632):
    for column in range(1,17):
        worksheet.write_string(row, column, str(chr(int(num))))
        num = num + 1

num = 0
for row in range (1,69632):
    response = hex(num)[2:]
    if len (response) == 1:
        response = '00' + response
    elif len (response) == 2:
        response = '0' + response
    else:
        pass
    worksheet.write (row, 0, response.upper()+'x')
    num = num + 1

workbook.close()

